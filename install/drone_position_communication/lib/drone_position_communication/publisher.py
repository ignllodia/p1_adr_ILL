#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix

class PositionPublisher(Node):
    def __init__(self):
        super().__init__('position_publisher')
        self.publisher_ = self.create_publisher(NavSatFix, 'drone_position', 10)
        self.timer = self.create_timer(1.0, self.publish_position)

    def publish_position(self):
        msg = NavSatFix()
        msg.latitude = 37.7749  # Example latitude
        msg.longitude = -122.4194  # Example longitude
        msg.altitude = 30.0  # Example altitude
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published position: Latitude: {msg.latitude}, Longitude: {msg.longitude}, Altitude: {msg.altitude}')

def main(args=None):
    rclpy.init(args=args)
    node = PositionPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()