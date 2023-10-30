cmake_minimum_required(VERSION 3.0.2)
project(cannybot_teleop)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  rospy
)

################################################################################
# Setup for python modules and scripts
################################################################################
catkin_python_setup()

################################################################################
# Declare ROS messages, services and actions
################################################################################

################################################################################
# Declare ROS dynamic reconfigure parameters
################################################################################

################################################################################
# Declare catkin specific configuration to be passed to dependent projects
################################################################################
catkin_package(
  CATKIN_DEPENDS rospy geometry_msgs
)

################################################################################
# Build
################################################################################

################################################################################
# Install
################################################################################
catkin_install_python(
  PROGRAMS  nodes/cannybot_teleop_key.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)