# RealSense node

This module integrates an Intel RealSense D435i camera with ROS 2 using Python. The camera streams color frames, which are published to a ROS 2 topic, making them accessible to other nodes for further processing or visualization.

## Features
- Streams color frames from the RealSense D435i camera.
- Publishes frames as *sensor_msgs/Image* messages on the */realsense/color_image* topic.
- Containerized setup for ease of deployment.

## Prerequisites
1. Docker Installed
Ensure you have Docker installed and configured on your system.

2. ROS 2 Installed (Optional for Subscribers)
If you plan to interact with the topic outside the container, install ROS 2 Humble.

## How to Build the Docker Container
Build the container from the provided *Dockerfile*:

```bash
docker build -t ros2-realsense .
```

## How to Run the Docker Container
Run the container with the required permissions to access the RealSense camera:

```bash
docker run --rm --net=host --privileged ros2-realsense
```

### Explanation:
- *--rm*: Automatically cleans up the container after it stops.
- *--net=host*: Shares the host's network to ensure ROS 2 topics are discoverable.
- *--privileged*: Grants the container access to the host’s hardware (e.g., USB devices).

## How to Subscribe to the Camera Topic
You can subscribe to the */realsense/color_image* topic using the following command:

```bash
ros2 topic echo /realsense/color_image
```

### Visualizing Images in RViz
To visualize the camera feed:

1. Launch RViz:
```bash
rviz2
```

2. Add an Image display.
3. Set the topic to */realsense/color_image*.

## Notes
- The container assumes the RealSense camera is connected to the host. Ensure the device is accessible using lsusb or similar tools before running the container.
- Modify the Python script or the Dockerfile as needed to support additional camera streams (e.g., depth or infrared).

## Troubleshooting
- No Data on /realsense/color_image:
    Check if the camera is properly connected.
    Ensure the container has access to /dev/video* and /dev/bus/usb.

- Permission Errors:
    Run sudo chmod 666 /dev/video* or adjust USB permissions for the RealSense camera.

- ROS 2 Topics Not Discoverable:
    Verify network setup and ROS 2 domain ID compatibility between nodes.
