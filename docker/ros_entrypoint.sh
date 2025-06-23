#!/bin/bash
set -e

# Source ROS 2 setup
source /opt/ros/humble/setup.bash
exec "$@"
