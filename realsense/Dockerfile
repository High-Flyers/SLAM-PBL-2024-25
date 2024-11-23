FROM ros:humble

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-pip python3-opencv && \
    pip3 install pyrealsense2 cv_bridge

RUN sudo apt-get install ros-humble-realsense-camera

# Copy the RealSense node script
COPY realsense_node.py /realsense_node.py

# Run the node
# CMD ["python3", "/realsense_node.py"]
