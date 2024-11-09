# Wybierz bazowy obraz ROS 2
FROM osrf/ros:humble-desktop

# Aktualizuj i instaluj niezbędne narzędzia
RUN apt-get update && apt-get install -y \
    software-properties-common

# Dodaj ROS 2 repozytoria i klucze GPG
RUN add-apt-repository universe && \
    apt-get update && \
    apt-get install -y curl gnupg2 lsb-release && \
    curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key | apt-key add - && \
    sh -c 'echo "deb http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list' && \
    apt-get update

# Instaluj narzędzia ROS 2, PX4 i inne zależności
RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions \
    build-essential \
    git \
    wget \
    vim \
    python3-pip \
    ros-humble-rviz2 \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-px4

# Skonfiguruj środowisko ROS 2 
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

# Instaluj PX4
WORKDIR /root
RUN git clone https://github.com/PX4/PX4-Autopilot.git --recursive
WORKDIR /root/PX4-Autopilot
RUN DONT_RUN=1 make px4_sitl_default gazebo

# Skonfiguruj środowisko PX4
RUN echo "source /root/PX4-Autopilot/Tools/setup_gazebo.bash /root/PX4-Autopilot /root/PX4-Autopilot/build/px4_sitl_default" >> ~/.bashrc

# Ustaw domyślny katalog roboczy
WORKDIR /root
CMD ["/bin/bash"]
