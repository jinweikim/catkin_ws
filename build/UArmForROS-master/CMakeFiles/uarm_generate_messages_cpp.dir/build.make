# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/jinwei/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/jinwei/catkin_ws/build

# Utility rule file for uarm_generate_messages_cpp.

# Include the progress variables for this target.
include UArmForROS-master/CMakeFiles/uarm_generate_messages_cpp.dir/progress.make

UArmForROS-master/CMakeFiles/uarm_generate_messages_cpp: /home/jinwei/catkin_ws/devel/include/uarm/Coords.h
UArmForROS-master/CMakeFiles/uarm_generate_messages_cpp: /home/jinwei/catkin_ws/devel/include/uarm/CoordsWithTS4.h
UArmForROS-master/CMakeFiles/uarm_generate_messages_cpp: /home/jinwei/catkin_ws/devel/include/uarm/CoordsWithTime.h
UArmForROS-master/CMakeFiles/uarm_generate_messages_cpp: /home/jinwei/catkin_ws/devel/include/uarm/Angles.h


/home/jinwei/catkin_ws/devel/include/uarm/Coords.h: /opt/ros/kinetic/lib/gencpp/gen_cpp.py
/home/jinwei/catkin_ws/devel/include/uarm/Coords.h: /home/jinwei/catkin_ws/src/UArmForROS-master/msg/Coords.msg
/home/jinwei/catkin_ws/devel/include/uarm/Coords.h: /opt/ros/kinetic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/jinwei/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating C++ code from uarm/Coords.msg"
	cd /home/jinwei/catkin_ws/src/UArmForROS-master && /home/jinwei/catkin_ws/build/catkin_generated/env_cached.sh /usr/bin/python2 /opt/ros/kinetic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/jinwei/catkin_ws/src/UArmForROS-master/msg/Coords.msg -Iuarm:/home/jinwei/catkin_ws/src/UArmForROS-master/msg -Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg -p uarm -o /home/jinwei/catkin_ws/devel/include/uarm -e /opt/ros/kinetic/share/gencpp/cmake/..

/home/jinwei/catkin_ws/devel/include/uarm/CoordsWithTS4.h: /opt/ros/kinetic/lib/gencpp/gen_cpp.py
/home/jinwei/catkin_ws/devel/include/uarm/CoordsWithTS4.h: /home/jinwei/catkin_ws/src/UArmForROS-master/msg/CoordsWithTS4.msg
/home/jinwei/catkin_ws/devel/include/uarm/CoordsWithTS4.h: /opt/ros/kinetic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/jinwei/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Generating C++ code from uarm/CoordsWithTS4.msg"
	cd /home/jinwei/catkin_ws/src/UArmForROS-master && /home/jinwei/catkin_ws/build/catkin_generated/env_cached.sh /usr/bin/python2 /opt/ros/kinetic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/jinwei/catkin_ws/src/UArmForROS-master/msg/CoordsWithTS4.msg -Iuarm:/home/jinwei/catkin_ws/src/UArmForROS-master/msg -Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg -p uarm -o /home/jinwei/catkin_ws/devel/include/uarm -e /opt/ros/kinetic/share/gencpp/cmake/..

/home/jinwei/catkin_ws/devel/include/uarm/CoordsWithTime.h: /opt/ros/kinetic/lib/gencpp/gen_cpp.py
/home/jinwei/catkin_ws/devel/include/uarm/CoordsWithTime.h: /home/jinwei/catkin_ws/src/UArmForROS-master/msg/CoordsWithTime.msg
/home/jinwei/catkin_ws/devel/include/uarm/CoordsWithTime.h: /opt/ros/kinetic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/jinwei/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Generating C++ code from uarm/CoordsWithTime.msg"
	cd /home/jinwei/catkin_ws/src/UArmForROS-master && /home/jinwei/catkin_ws/build/catkin_generated/env_cached.sh /usr/bin/python2 /opt/ros/kinetic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/jinwei/catkin_ws/src/UArmForROS-master/msg/CoordsWithTime.msg -Iuarm:/home/jinwei/catkin_ws/src/UArmForROS-master/msg -Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg -p uarm -o /home/jinwei/catkin_ws/devel/include/uarm -e /opt/ros/kinetic/share/gencpp/cmake/..

/home/jinwei/catkin_ws/devel/include/uarm/Angles.h: /opt/ros/kinetic/lib/gencpp/gen_cpp.py
/home/jinwei/catkin_ws/devel/include/uarm/Angles.h: /home/jinwei/catkin_ws/src/UArmForROS-master/msg/Angles.msg
/home/jinwei/catkin_ws/devel/include/uarm/Angles.h: /opt/ros/kinetic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/jinwei/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Generating C++ code from uarm/Angles.msg"
	cd /home/jinwei/catkin_ws/src/UArmForROS-master && /home/jinwei/catkin_ws/build/catkin_generated/env_cached.sh /usr/bin/python2 /opt/ros/kinetic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/jinwei/catkin_ws/src/UArmForROS-master/msg/Angles.msg -Iuarm:/home/jinwei/catkin_ws/src/UArmForROS-master/msg -Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg -p uarm -o /home/jinwei/catkin_ws/devel/include/uarm -e /opt/ros/kinetic/share/gencpp/cmake/..

uarm_generate_messages_cpp: UArmForROS-master/CMakeFiles/uarm_generate_messages_cpp
uarm_generate_messages_cpp: /home/jinwei/catkin_ws/devel/include/uarm/Coords.h
uarm_generate_messages_cpp: /home/jinwei/catkin_ws/devel/include/uarm/CoordsWithTS4.h
uarm_generate_messages_cpp: /home/jinwei/catkin_ws/devel/include/uarm/CoordsWithTime.h
uarm_generate_messages_cpp: /home/jinwei/catkin_ws/devel/include/uarm/Angles.h
uarm_generate_messages_cpp: UArmForROS-master/CMakeFiles/uarm_generate_messages_cpp.dir/build.make

.PHONY : uarm_generate_messages_cpp

# Rule to build all files generated by this target.
UArmForROS-master/CMakeFiles/uarm_generate_messages_cpp.dir/build: uarm_generate_messages_cpp

.PHONY : UArmForROS-master/CMakeFiles/uarm_generate_messages_cpp.dir/build

UArmForROS-master/CMakeFiles/uarm_generate_messages_cpp.dir/clean:
	cd /home/jinwei/catkin_ws/build/UArmForROS-master && $(CMAKE_COMMAND) -P CMakeFiles/uarm_generate_messages_cpp.dir/cmake_clean.cmake
.PHONY : UArmForROS-master/CMakeFiles/uarm_generate_messages_cpp.dir/clean

UArmForROS-master/CMakeFiles/uarm_generate_messages_cpp.dir/depend:
	cd /home/jinwei/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jinwei/catkin_ws/src /home/jinwei/catkin_ws/src/UArmForROS-master /home/jinwei/catkin_ws/build /home/jinwei/catkin_ws/build/UArmForROS-master /home/jinwei/catkin_ws/build/UArmForROS-master/CMakeFiles/uarm_generate_messages_cpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : UArmForROS-master/CMakeFiles/uarm_generate_messages_cpp.dir/depend

