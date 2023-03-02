import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import sensor_msgs
from cv_bridge import CvBridge
import cv2

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.subscription2 = self.create_subscription(
            sensor_msgs.msg.CompressedImage,
            '/image_raw/compressed',
            self.listener_callback2,
            10)
        self.subscription2  # prevent unused variable warning
        return

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        return
    def listener_callback2(self, msg):
        bridge = CvBridge()
        cv_image = bridge.compressed_imgmsg_to_cv2(msg, desired_encoding='passthrough')
        cv2.imwrite("/home/levin/temp/2.jpg", cv_image)
        return



def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()