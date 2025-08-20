# syntax=docker/dockerfile:1.4
# Dockerfile for Ubuntu 22.04 model training with GPU, network, display, and host folder access
FROM ubuntu:18.04

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install basic utilities and Python (for ML)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        wget git curl ca-certificates \
        sudo \
        gdb \
        openssh-client \
        nano \
        cmake \
        && rm -rf /var/lib/apt/lists/*


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
