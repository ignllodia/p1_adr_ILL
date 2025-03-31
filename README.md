# Drone Position Communication

This project implements a ROS2 package for communicating the position of a drone using the `NavSatFix` message type. It includes a publisher that sends the drone's position at regular intervals and a subscriber that receives this position data.

## Project Structure

```
ros2_ws
├── src
│   ├── drone_position_communication
│   │   ├── drone_position_communication
│   │   │   ├── __init__.py
│   │   │   ├── publisher.py
│   │   │   └── subscriber.py
│   │   ├── package.xml
│   │   └── setup.py
├── README.md
└── .colcon_ignore
```

## Dependencies

- ROS2 (Foxy or later)
- `sensor_msgs` for the `NavSatFix` message type

## Installation

1. **Install ROS2**: Follow the official ROS2 installation guide for your operating system.
2. **Create a ROS2 workspace**:
   ```bash
   mkdir -p ~/ros2_ws/src
   cd ~/ros2_ws/src
   ```
3. **Clone the package**:
   ```bash
   git clone <repository-url> drone_position_communication
   ```
4. **Build the workspace**:
   ```bash
   cd ~/ros2_ws
   colcon build
   ```

## Running the Nodes

1. **Source the workspace**:
   ```bash
   source ~/ros2_ws/install/setup.bash
   ```
2. **Run the publisher**:
   ```bash
   ros2 run drone_position_communication publisher
   ```
3. **Run the subscriber**:
   ```bash
   ros2 run drone_position_communication subscriber
   ```

## Usage

The publisher will start sending `NavSatFix` messages containing the drone's position, while the subscriber will listen for these messages and process them accordingly.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.