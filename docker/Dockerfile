# Ubuntu 22.04 with ROS 2 Humble, GUI, and host networking
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# 1. Install system dependencies (no ROS/colcon/rosdep yet)
RUN apt-get update && apt-get install -y \
    locales \
    lsb-release \
    gnupg2 \
    curl \
    wget \
    git \
    build-essential \
    python3-pip \
    x11-apps \
    libgl1-mesa-glx \
    libxrender1 \
    libsm6 \
    libxext6 \
    pciutils \
    && rm -rf /var/lib/apt/lists/*

# Install NVIDIA Container Toolkit (for GPU access)
RUN apt-get update && \
    apt-get install -y ca-certificates gnupg && \
    curl -s -L https://nvidia.github.io/libnvidia-container/gpgkey | apt-key add - && \
    curl -s -L https://nvidia.github.io/libnvidia-container/ubuntu22.04/libnvidia-container.list | tee /etc/apt/sources.list.d/nvidia-container-toolkit.list && \
    apt-get update && \
    apt-get install -y nvidia-container-toolkit && \
    rm -rf /var/lib/apt/lists/*

# 2. Set locale
RUN locale-gen en_US en_US.UTF-8 && \
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 && \
    export LANG=en_US.UTF-8

# 3. Add ROS 2 GPG key and repo
RUN apt-get update && \
    apt-get install -y software-properties-common curl gnupg2 && \
    add-apt-repository universe && \
    curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key | gpg --dearmor -o /usr/share/keyrings/ros-archive-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list

# 4. Install ROS 2 Humble and ROS tools
RUN apt-get update && apt-get install -y \
    ros-humble-desktop \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-argcomplete \
    && rm -rf /var/lib/apt/lists/*

# 5. Source ROS 2 setup on login
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

# 6. Set up entrypoint
COPY ./ros_entrypoint.sh /ros_entrypoint.sh
RUN chmod +x /ros_entrypoint.sh
ENTRYPOINT ["/ros_entrypoint.sh"]

# 7. Set default command
CMD ["bash"]

# 8. For GUI: set DISPLAY and allow X11 forwarding
ENV DISPLAY=${DISPLAY}
ENV QT_X11_NO_MITSHM=1

# 9. For ROS 2 networking: recommend running with --network=host and --gpus all
# Example run command:
# docker run -it --rm --gpus all --network=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v /home/levin:/home/levin <image_name>

# 10. Create /home/levin directory in the container
RUN mkdir -p /home/levin && chown root:root /home/levin
WORKDIR /home/levin
