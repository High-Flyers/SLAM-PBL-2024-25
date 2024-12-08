# README: Gazebo Work in Progress

## Overview
This project integrates Gazebo, Nav2, and SLAM Toolbox to simulate and navigate the `salamanca` robot. It requires setup and configuration to achieve a working navigation stack with joystick support. This README provides the steps to run the simulation, current issues, and a to-do list for further improvements.

---

## How to Run

### Step 1: Build the Workspace
Ensure the workspace is built and sourced.
```bash
colcon build --symlink-install
source install/setup.bash
```

### Step 2: Launch the Simulation
1. **Start the simulation environment** (First terminal):
   ```bash
   ros2 launch pbl_bringup pbl_bringup.launch.xml
   ```

2. **Launch Navigation** (Second terminal):
   ```bash
   ros2 launch nav2_bringup navigation_launch.py use_sim_time:=True
   ```

3. **Launch SLAM Toolbox** (Third terminal):
   ```bash
   ros2 launch slam_toolbox online_async_launch.py use_sim_time:=True
   ```

---

## Current Issues

1. **Lack of Unified Launch File**:
   - Currently, launching requires multiple terminals and commands. A single unified launch file would simplify this process.

2. **TF Frames Misaligned**:
   - The robot’s TF frames are misaligned and appear below the ground.
   - This causes improper navigation behavior as `/cmd_vel` publishes only z-axis movement.

3. **Navigation Issues**:
   - Nav2 is not fully functional due to the TF alignment problem.

4. **Joystick Configuration**:
   - Joystick control via `/joy` works with the PS3 controller but has incorrect axis mappings.
   - Movement is currently restricted to z-axis rotation; proper mappings are needed.
   - **Press R1** to enable movement.

---

## To-Do List

### 1. Unified Launch File
- Create a single launch file that:
  - Starts Gazebo with the robot.
  - Launches Nav2.
  - Launches SLAM Toolbox.
  - Enables `use_sim_time` for all nodes.

### 2. Fix TF Frames
- Update the URDF/Xacro of the `salamanca` robot to:
  - Correct link and collision poses.
  - Ensure TF frames are aligned above the ground.

### 3. Verify Navigation
- After fixing TF alignment, confirm that Nav2 operates as expected.
- Test `/cmd_vel` to ensure proper movement.

### 4. Correct Joystick Mapping
- Update joystick parameters to:
  - Fix axis mappings for full control.
  - Ensure linear and angular velocities are correctly mapped.

---

## Notes
- All nodes must use `use_sim_time:=True` for proper synchronization in simulation.
- Verify topics like `/cmd_vel`, `/odom`, and `/scan` to ensure data flow between nodes.




