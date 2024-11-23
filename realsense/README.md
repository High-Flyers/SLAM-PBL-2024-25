# RealSense node

This module integrates an Intel RealSense D435i camera with ROS 2 using Python. The camera streams color frames, which are published to a ROS 2 topic, making them accessible to other nodes for further processing or visualization.

```bash
docker run -it --rm \
    --device /dev/bus/usb:/dev/bus/usb \
    --privileged \
    --net=host \
    --device-cgroup-rule "c 81:* rmw" \
    --device-cgroup-rule "c 189:* rmw" \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --name ros2 \
    -v /home/opg/Github/PBL2024-25-SLAM/realsense/ws:/ws \
    ros2-realsense
```
