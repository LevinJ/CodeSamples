import os
import urllib.request
import zipfile

# Function to download a file
def download_file(url, output_path):
    print(f"Downloading {url}...")
    urllib.request.urlretrieve(url, output_path)
    print(f"Saved to {output_path}")

# Function to extract a zip file
def extract_zip(zip_path, extract_to):
    print(f"Extracting {zip_path}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted to {extract_to}")

if __name__ == "__main__":
    # URLs for the ONNX model and calibration dataset
    model_url = "https://github.com/onnx/models/raw/main/vision/classification/resnet/model/resnet50-v2-7.onnx"
    dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"

    # Update paths to save the downloaded files
    model_path = "temp/resnet50-v2-7.onnx"
    dataset_zip_path = "temp/flower_photos.tgz"
    dataset_dir = "temp/flower_photos"

    # Ensure the temp directory exists
    os.makedirs("temp", exist_ok=True)

    # Download the ONNX model
    if not os.path.exists(model_path):
        download_file(model_url, model_path)

    # Download and extract the calibration dataset
    if not os.path.exists(dataset_dir):
        if not os.path.exists(dataset_zip_path):
            download_file(dataset_url, dataset_zip_path)
        print("Extracting dataset...")
        os.system(f"tar -xvzf {dataset_zip_path}")
        print("Dataset extracted.")
