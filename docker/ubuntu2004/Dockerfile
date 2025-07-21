# syntax=docker/dockerfile:1.4
# Dockerfile for Ubuntu 22.04 model training with GPU, network, display, and host folder access
FROM ubuntu:20.04

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




# Make 'python' refer to 'python3'
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install CUDA and cuDNN (NVIDIA GPU support)
# Note: This assumes you will use the NVIDIA Container Toolkit (nvidia-docker)
# and the host has the correct drivers. For more control, add CUDA install steps here if needed.

# Install ROS Noetic
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl gnupg2 lsb-release && \
    sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros-latest.list' && \
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        ros-noetic-desktop-full && \
    rm -rf /var/lib/apt/lists/*

# Source ROS setup script
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc && \
    /bin/bash -c "source /opt/ros/noetic/setup.bash"

# Install dependencies for building ROS packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        python3-catkin-tools \
        python3-rosdep \
        python3-rosinstall \
        python3-rosinstall-generator \
        python3-wstool \
        libboost-all-dev \
        && rm -rf /var/lib/apt/lists/*

# Initialize rosdep
RUN rosdep init && \
    rosdep update

# Set up a working directory
# WORKDIR /workspace


# Install Visual Studio Code
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        software-properties-common apt-transport-https && \
    wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" && \
    apt-get update && \
    apt-get install -y code && \
    rm -rf /var/lib/apt/lists/*

# Set the DISPLAY environment variable to connect to the host's X server
ENV DISPLAY=:0

# Add a non-root user for better security
RUN useradd -m dockeruser && echo "dockeruser:dockeruser" | chpasswd && adduser dockeruser sudo
USER dockeruser

# Set the working directory
WORKDIR /home/dockeruser

# Copy any necessary files into the container
# COPY . /home/dockeruser

# Default command
CMD ["/bin/bash"]
