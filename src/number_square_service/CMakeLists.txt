# filepath: ~/ros2_ws/src/number_square_service/CMakeLists.txt
cmake_minimum_required(VERSION 3.5)
project(number_square_service)

# Encuentra las dependencias necesarias
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(example_interfaces REQUIRED)

# Instala los scripts de Python
install(
  PROGRAMS
    number_square_service/service.py
    number_square_service/client.py
  DESTINATION lib/${PROJECT_NAME}
)

# Instala otros archivos necesarios
install(
  DIRECTORY number_square_service
  DESTINATION lib/python3.10/site-packages
)

ament_package()