
from keyboard import WheelController
from realsense import RealSenseController
import threading

def start_camera():
    # Initialize and start the RealSense camera stream
    camera = RealSenseController()
    camera.start_stream()
    camera.capture_frames()
    camera.stop_stream()

def start_wheel_control():
    # Initialize the WheelController with the serial numbers of the ODrive devices
    wheel_controller = WheelController("3946354F3231", "397135683231")
    wheel_controller.control_loop()

if __name__ == "__main__":
    # Create threads for the camera and wheel control so they can run simultaneously
    camera_thread = threading.Thread(target=start_camera)
    wheel_control_thread = threading.Thread(target=start_wheel_control)

    # Start both threads
    camera_thread.start()
    wheel_control_thread.start()

    # Wait for both threads to complete
    camera_thread.join()
    wheel_control_thread.join()
