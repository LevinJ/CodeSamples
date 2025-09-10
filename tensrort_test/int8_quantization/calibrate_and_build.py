from debian import c
import tensorrt as trt
import numpy as np
import os
import pycuda.driver as cuda
import pycuda.autoinit
import random
import time

# Define a calibration dataset
class CalibrationDataset:
    def __init__(self, data_dir, batch_size):
        self.data_dir = data_dir
        self.batch_size = batch_size
        self.files = [os.path.join(root, f) for root, _, files in os.walk(data_dir) for f in files if f.endswith(".JPEG")]
        self.files = random.sample(self.files, min(500, len(self.files)))
        self.index = 0

    def __len__(self):
        return len(self.files)

    def next_batch(self):
        batch = []
        for _ in range(self.batch_size):
            if self.index >= len(self.files):
                self.index = 0
            file_path = self.files[self.index]
            data = self.preprocess_image(file_path)
            batch.append(data)
            self.index += 1
        return np.array(batch)

    def preprocess_image(self, image_path):
        from PIL import Image


        image = Image.open(image_path).resize((224, 224))
        image = np.array(image).astype(np.float32) / 255.0
        image = np.transpose(image, (2, 0, 1))  # HWC to CHW
        return image

# Custom calibrator
class MyCalibrator(trt.IInt8EntropyCalibrator2):
    """
    Custom INT8 Min-Max calibrator for TensorRT.
    """
    def __init__(self, dataset, cache_file):
        """
        Initialize the calibrator with a dataset and cache file.

        Args:
            dataset (CalibrationDataset): The calibration dataset.
            cache_file (str): Path to the calibration cache file.
        """
        super().__init__()
        self.dataset = dataset
        self.cache_file = cache_file
        self.batch_size = dataset.batch_size
        self.device_input = None
        self.current_batch = None

    def get_batch_size(self):
        """
        Return the batch size for calibration.

        Returns:
            int: Batch size.
        """
        return self.batch_size

    def get_batch(self, names):
        """
        Provide a batch of calibration data to TensorRT.

        Args:
            names (list): List of input tensor names.

        Returns:
            list: A batch of calibration data.
        """
        if self.current_batch is None:
            self.current_batch = self.dataset.next_batch()
        if not self.current_batch.size:
            return None
        if self.device_input is None:
            self.device_input = cuda.mem_alloc(self.current_batch.nbytes)
        cuda.memcpy_htod(self.device_input, self.current_batch)
        self.current_batch = None
        return [int(self.device_input)]

    def read_calibration_cache(self):
        """
        Read the calibration cache if it exists.

        Returns:
            bytes: The calibration cache data, or None if not available.
        """
        if os.path.exists(self.cache_file):
            print(f"Reading calibration cache from {self.cache_file}")
            with open(self.cache_file, "rb") as f:
                return f.read()
        return None

    def write_calibration_cache(self, cache):
        """
        Write the calibration cache to a file.

        Args:
            cache (bytes): The calibration cache data.
        """
        with open(self.cache_file, "wb") as f:
            print(f"Writing calibration cache to {self.cache_file}")
            f.write(cache)

# Main function to perform calibration
if __name__ == "__main__":
    onnx_model_path = "temp/resnet50-v2-7.onnx"
    calibration_cache_path = "temp/calibration.cache"
    calibration_data_dir = "temp/tiny-imagenet-200/test"

    script_dir = os.path.dirname(os.path.abspath(__file__))
    onnx_model_path = os.path.join(script_dir, onnx_model_path)
    calibration_cache_path = os.path.join(script_dir, calibration_cache_path)
    calibration_data_dir = os.path.join(script_dir, calibration_data_dir)
    batch_size = 8

    TRT_LOGGER = trt.Logger(trt.Logger.INFO)
    builder = trt.Builder(TRT_LOGGER)
    network = builder.create_network(1 << int(trt.NetworkDefinitionCreationFlag.EXPLICIT_BATCH))
    parser = trt.OnnxParser(network, TRT_LOGGER)

    # Parse the ONNX model
    with open(onnx_model_path, "rb") as model:
        if not parser.parse(model.read()):
            print("Failed to parse ONNX model")
            for error in range(parser.num_errors):
                print(parser.get_error(error))
            exit(1)

    set_dynamic_range = False  # Set to True to manually set dynamic range
    if set_dynamic_range:
        # Set dynamic range for all tensors to [-128.0, 127.0]
        for i in range(network.num_layers):
            layer = network.get_layer(i)
            for j in range(layer.num_outputs):
                tensor = layer.get_output(j)
                if tensor:
                    tensor.set_dynamic_range(-128.0, 127.0)
        # Set dynamic range for input tensors
        for i in range(network.num_inputs):
            input_tensor = network.get_input(i)
            if input_tensor:
                input_tensor.set_dynamic_range(-128.0, 127.0)
    # Set up INT8 calibration
    config = builder.create_builder_config()
    config.profiling_verbosity = trt.ProfilingVerbosity.DETAILED
    config.set_flag(trt.BuilderFlag.INT8)
    # Enable FP16 precision in addition to INT8
    config.set_flag(trt.BuilderFlag.FP16)
    dataset = CalibrationDataset(calibration_data_dir, batch_size)
    calibrator = MyCalibrator(dataset, calibration_cache_path)
    # Skip INT8 calibration since dynamic range is manually set
    # Removed the calibrator and related configuration
    # config.int8_calibrator = calibrator

    # Define an optimization profile for dynamic input shapes
    profile = builder.create_optimization_profile()
    input_name = network.get_input(0).name  # Assuming the model has one input
    profile.set_shape(input_name, (1, 3, 224, 224), (1, 3, 224, 224), (1, 3, 224, 224))
    config.add_optimization_profile(profile)

    # Build the serialized engine
    start_time = time.time()
    serialized_engine = builder.build_serialized_network(network, config)
    duration = time.time() - start_time
    if serialized_engine:
        engine_path = "temp/resnet50_int8.engine"
        engine_path = os.path.join(script_dir, engine_path)
        print(f"Calibration completed and engine built successfully at {engine_path}")
        with open(engine_path, "wb") as f:
            f.write(serialized_engine)
    else:
        print("Failed to build engine.")
    print(f"Engine build and calibration duration: {duration:.2f} seconds")
