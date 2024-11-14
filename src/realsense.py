import pyrealsense2.pyrealsense2 as rs
import numpy as np
import cv2

class RealSenseController:
    def __init__(self, width=640, height=480, fps=30):
        # Initialize the RealSense pipeline and configuration
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.color, width, height, rs.format.bgr8, fps)
        self.profile = None

    def start_stream(self):
        # Start the RealSense camera stream
        try:
            self.profile = self.pipeline.start(self.config)
            print("RealSense camera has started")
        except RuntimeError as e:
            print(f"Error starting the camera: {e}")

    def capture_frames(self):
        # Capture and display frames from the camera
        try:
            while True:
                frames = self.pipeline.wait_for_frames()
                color_frame = frames.get_color_frame()
                
                if not color_frame:
                    print("No color frame available")
                    continue
                
                # Convert the frame to a numpy array and display it
                color_image = np.asanyarray(color_frame.get_data())
                cv2.imshow('RealSense RGB Camera View', color_image)

                # Break the loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("Preview stopped")
                    break

        except RuntimeError as e:
            print(f"Camera error while capturing frames: {e}")

    def stop_stream(self):
        # Stop the RealSense camera stream
        if self.profile:
            self.pipeline.stop()
            cv2.destroyAllWindows()
            print("RealSense camera has stopped")

# Example usage
if __name__ == "__main__":
    camera = RealSenseController()
    camera.start_stream()
    camera.capture_frames()
    camera.stop_stream()
