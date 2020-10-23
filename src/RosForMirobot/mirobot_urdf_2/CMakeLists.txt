cmake_minimum_required(VERSION 2.8.3)

project(mirobot_urdf_2)

find_package(catkin REQUIRED)

catkin_package()

find_package(
  catkin REQUIRED COMPONENTS
  roslaunch
  roscpp
  rospy
  serial
  sensor_msgs
  geometry_msgs
)

include_directories(include ${catkin_INCLUDE_DIRS} ${PCL_INCLUDE_DIRS})

add_executable(mirobot_write_node src/mirobot_write_node.cpp)
target_link_libraries(mirobot_write_node ${catkin_LIBRARIES})

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
