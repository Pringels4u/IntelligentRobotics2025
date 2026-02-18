cmake_minimum_required(VERSION 3.5)
project(uw_pkg)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# Add your node
add_executable(battery_pub src/battery_pub.cpp)
ament_target_dependencies(battery_pub rclcpp std_msgs)
install(TARGETS battery_pub DESTINATION lib/${PROJECT_NAME})

ament_package()