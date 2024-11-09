# PBL2024-25-SLAM
https://github.com/ReconCycle/urdf-from-step-docker


```bash
docker run -it --rm \
  --net=host \
  --env="DISPLAY" \
  --env="QT_X11_NO_MITSHM=1" \
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  --name ros2 \
  -v <path>:/ws \
  ros2
```