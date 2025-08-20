import onnxruntime as ort
import numpy as np
from PIL import Image
import os
import onnx

# Function to preprocess an image
def preprocess_image(image_path):
    image = Image.open(image_path).resize((224, 224))  # Resize to 224x224
    image = np.array(image).astype(np.float32) / 255.0  # Normalize to [0, 1]
    image = np.transpose(image, (2, 0, 1))  # HWC to CHW
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Function to display the ONNX model's data types
def show_model_data_types(model_path):
    # 打印输入信息
    model = onnx.load(model_path)
    for input in model.graph.input:
        print(f"Input name: {input.name}")
        # 获取维度信息
        shape = []
        for dim in input.type.tensor_type.shape.dim:
            dim_value = dim.dim_value if dim.dim_value != 0 else "?"
            shape.append(dim_value)
        print(f"Shape: {shape}")  # 例如 ['?', 3, 224, 224] 表示动态batch

    for input in model.graph.input:
        print(f"Input: {input.name}")
        print(f"Data type: {onnx.TensorProto.DataType.Name(input.type.tensor_type.elem_type)}")

    for output in model.graph.output:
        print(f"Output: {output.name}")
        print(f"Data type: {onnx.TensorProto.DataType.Name(output.type.tensor_type.elem_type)}")

    # 检查权重参数的数据类型
    for initializer in model.graph.initializer:
        print(f"Weight: {initializer.name}")
        print(f"Data type: {onnx.TensorProto.DataType.Name(initializer.data_type)}")

# Function to load ONNX model and perform inference
def classify_images(model_path, image_dir):
    # Load the ONNX model
    session = ort.InferenceSession(model_path)
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name

    # Update to recursively find images in subfolders
    for root, _, files in os.walk(image_dir):
        for image_name in files[:4]:  # Limit to 5 images
            image_path = os.path.join(root, image_name)
            if not image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                continue

            # Preprocess the image
            input_data = preprocess_image(image_path)

            # Perform inference
            outputs = session.run([output_name], {input_name: input_data})
            predictions = np.squeeze(outputs[0])

            # # Print the top-5 predictions
            # top_5_indices = predictions.argsort()[-5:][::-1]
            # print(f"Image: {image_name}")
            # print("Top-5 Predictions:")
            # for idx in top_5_indices:
            #     print(f"  Class {idx}: {predictions[idx]:.4f}")
            import matplotlib.pyplot as plt

            # Show the original image and its top prediction
            top_idx = predictions.argmax()
            class_text = f"Class {top_idx}: {predictions[top_idx]:.4f}"

            # Load the image for display
            img_display = Image.open(image_path)

            plt.figure(figsize=(5, 5))
            plt.imshow(img_display)
            plt.title(class_text)
            plt.axis('off')
            plt.show()

if __name__ == "__main__":
    model_path = "temp/resnet50-v2-7.onnx"  # Path to the ONNX model
    image_dir = "temp/flower_photos"  # Path to the image directory

    # Show model data types
    show_model_data_types(model_path)

    # Perform image classification
    classify_images(model_path, image_dir)
