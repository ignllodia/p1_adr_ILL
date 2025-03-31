#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix

class PositionSubscriber(Node):
    def __init__(self):
        super().__init__('position_subscriber')
        self.subscription = self.create_subscription(
            NavSatFix,
            'drone_position',
            self.callback,
            10
        )

    def callback(self, msg):
        latitude = msg.latitude
        longitude = msg.longitude
        altitude = msg.altitude
        self.get_logger().info(f'Received position: Latitude: {latitude}, Longitude: {longitude}, Altitude: {altitude}')

def main(args=None):
    rclpy.init(args=args)
    node = PositionSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()