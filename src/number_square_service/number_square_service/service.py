#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts  # Usaremos este servicio como base

class SquareService(Node):
    def __init__(self):
        super().__init__('square_service')
        self.srv = self.create_service(AddTwoInts, 'calculate_square', self.calculate_square_callback)
        self.get_logger().info('Service ready to calculate square of a number.')

    def calculate_square_callback(self, request, response):
        response.sum = request.a * request.a  # Calcula el cuadrado del número
        self.get_logger().info(f'Received request: {request.a}, responding with: {response.sum}')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = SquareService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()