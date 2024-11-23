import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import pyrealsense2.pyrealsense2 as rs
import numpy as np
import cv2

class RealSenseNode(Node):
    def __init__(self, width=640, height=480, fps=30):
        super().__init__('realsense_node')

        # Initialize RealSense pipeline and configuration
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.color, width, height, rs.format.bgr8, fps)

        self.profile = None
        self.bridge = CvBridge()  # For converting OpenCV images to ROS Image messages
        self.publisher = self.create_publisher(Image, 'realsense/color_image', 10)

        self.get_logger().info('RealSense Node initialized.')

    def start_stream(self):
        try:
            self.profile = self.pipeline.start(self.config)
            self.get_logger().info('RealSense camera started.')
        except RuntimeError as e:
            self.get_logger().error(f'Error starting the camera: {e}')

    def capture_frames(self):
        try:
            while rclpy.ok():
                frames = self.pipeline.wait_for_frames()
                color_frame = frames.get_color_frame()

                if not color_frame:
                    self.get_logger().warn('No color frame available')
                    continue

                # Convert to numpy array
                color_image = np.asanyarray(color_frame.get_data())

                # Publish the image to the topic
                ros_image = self.bridge.cv2_to_imgmsg(color_image, encoding="bgr8")
                self.publisher.publish(ros_image)
                self.get_logger().info('Published a frame.')

        except RuntimeError as e:
            self.get_logger().error(f'Camera error while capturing frames: {e}')

    def stop_stream(self):
        if self.profile:
            self.pipeline.stop()
            self.get_logger().info('RealSense camera stopped.')

def main(args=None):
    rclpy.init(args=args)

    node = RealSenseNode()
    node.start_stream()

    try:
        node.capture_frames()
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down node.')

    node.stop_stream()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
