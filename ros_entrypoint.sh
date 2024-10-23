#!/bin/bash
set -e

# source the ROS 2 setup script
source "/opt/ros/humble/setup.bash"
source "/home/docker/ws/install/setup.bash"

exec "$@"