cmake_minimum_required(VERSION 3.5)
project(drone_position_communication)

# Encuentra las dependencias necesarias
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)

# Instala los scripts de Python
install(
  PROGRAMS
    drone_position_communication/publisher.py
    drone_position_communication/subscriber.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()