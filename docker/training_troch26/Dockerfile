# syntax=docker/dockerfile:1.4
# Dockerfile for Ubuntu 22.04 model training with GPU, network, display, and host folder access
FROM ubuntu:22.04

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install basic utilities and Python (for ML)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 python3-pip python3-dev \
        build-essential \
        wget git curl ca-certificates \
        libgl1-mesa-glx \
        libglib2.0-0 \
        sudo \
        openssh-client \
        nano \
        && rm -rf /var/lib/apt/lists/*


# Copy requirements file and install Python packages
COPY requirements_v2.txt /tmp/requirements_v2.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install --no-cache-dir -r /tmp/requirements_v2.txt

# Make 'python' refer to 'python3'
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install CUDA and cuDNN (NVIDIA GPU support)
# Note: This assumes you will use the NVIDIA Container Toolkit (nvidia-docker)
# and the host has the correct drivers. For more control, add CUDA install steps here if needed.

# Set up a working directory
# WORKDIR /workspace

# Default command
CMD ["/bin/bash"]
