FROM osrf/ros:humble-desktop

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y nano \
    ros-humble-rviz2 \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-urdf-tutorial \
    ros-humble-tf2-tools \
    && rm -rf /var/lib/apt/lists/*

RUN rosdep update

RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc \
    && echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc \
    && echo "source ~/ws/install/setup.bash" >> ~/.bashrc \
    && echo "source /usr/share/gazebo/setup.bash" >> ~/.bashrc

RUN /bin/bash -c "source ~/.bashrc"

CMD ["/bin/bash"]