# Podstawowy obraz bazowy
FROM osrf/ros:humble-desktop

# Aktualizacja i instalacja podstawowych pakietów
RUN apt-get update && apt-get upgrade -y

# Dodanie repozytorium ROS 2
RUN apt-get install -y curl gnupg2 lsb-release && \
    mkdir -p /etc/apt/keyrings && \
    curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | gpg --dearmor -o /etc/apt/keyrings/ros2-archive-keyring.gpg && \
    echo "deb [signed-by=/etc/apt/keyrings/ros2-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros2-latest.list

# Instalacja ROS2 zależności i narzędzi
RUN apt-get update && apt-get install -y \
    nano \
    ros-humble-rviz2 \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-urdf-tutorial \
    ros-humble-tf2-tools \
    ros-humble-cv-bridge \
    ros-humble-librealsense2* \
    ros-humble-realsense2-* \
    && rm -rf /var/lib/apt/lists/*

# Instalacja Pythona i wymaganych bibliotek
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-opencv \
    python3-colcon-common-extensions \
    ros-humble-sensor-msgs \
    libopencv-dev \
    libusb-1.0-0-dev \
    && rm -rf /var/lib/apt/lists/*

# Zaktualizowanie rosdep
RUN rosdep update

# Dodanie źródeł do .bashrc
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc && \
    echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc && \
    echo "source ~/ws/install/setup.bash" >> ~/.bashrc && \
    echo "source /usr/share/gazebo/setup.bash" >> ~/.bashrc

# Załadowanie .bashrc, aby zmiany były aktywne
RUN /bin/bash -c "source ~/.bashrc"

# Ustawienie domyślnego polecenia
CMD ["/bin/bash"]
