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

# Include any dependencies generated for this target.
include coordinate_switch/CMakeFiles/switch.dir/depend.make

# Include the progress variables for this target.
include coordinate_switch/CMakeFiles/switch.dir/progress.make

# Include the compile flags for this target's objects.
include coordinate_switch/CMakeFiles/switch.dir/flags.make

coordinate_switch/CMakeFiles/switch.dir/src/switch.cpp.o: coordinate_switch/CMakeFiles/switch.dir/flags.make
coordinate_switch/CMakeFiles/switch.dir/src/switch.cpp.o: /home/jinwei/catkin_ws/src/coordinate_switch/src/switch.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jinwei/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object coordinate_switch/CMakeFiles/switch.dir/src/switch.cpp.o"
	cd /home/jinwei/catkin_ws/build/coordinate_switch && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/switch.dir/src/switch.cpp.o -c /home/jinwei/catkin_ws/src/coordinate_switch/src/switch.cpp

coordinate_switch/CMakeFiles/switch.dir/src/switch.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/switch.dir/src/switch.cpp.i"
	cd /home/jinwei/catkin_ws/build/coordinate_switch && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jinwei/catkin_ws/src/coordinate_switch/src/switch.cpp > CMakeFiles/switch.dir/src/switch.cpp.i

coordinate_switch/CMakeFiles/switch.dir/src/switch.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/switch.dir/src/switch.cpp.s"
	cd /home/jinwei/catkin_ws/build/coordinate_switch && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jinwei/catkin_ws/src/coordinate_switch/src/switch.cpp -o CMakeFiles/switch.dir/src/switch.cpp.s

coordinate_switch/CMakeFiles/switch.dir/src/switch.cpp.o.requires:

.PHONY : coordinate_switch/CMakeFiles/switch.dir/src/switch.cpp.o.requires

coordinate_switch/CMakeFiles/switch.dir/src/switch.cpp.o.provides: coordinate_switch/CMakeFiles/switch.dir/src/switch.cpp.o.requires
	$(MAKE) -f coordinate_switch/CMakeFiles/switch.dir/build.make coordinate_switch/CMakeFiles/switch.dir/src/switch.cpp.o.provides.build
.PHONY : coordinate_switch/CMakeFiles/switch.dir/src/switch.cpp.o.provides

coordinate_switch/CMakeFiles/switch.dir/src/switch.cpp.o.provides.build: coordinate_switch/CMakeFiles/switch.dir/src/switch.cpp.o


# Object files for target switch
switch_OBJECTS = \
"CMakeFiles/switch.dir/src/switch.cpp.o"

# External object files for target switch
switch_EXTERNAL_OBJECTS =

/home/jinwei/catkin_ws/devel/lib/coordinate_switch/switch: coordinate_switch/CMakeFiles/switch.dir/src/switch.cpp.o
/home/jinwei/catkin_ws/devel/lib/coordinate_switch/switch: coordinate_switch/CMakeFiles/switch.dir/build.make
/home/jinwei/catkin_ws/devel/lib/coordinate_switch/switch: coordinate_switch/CMakeFiles/switch.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/jinwei/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/jinwei/catkin_ws/devel/lib/coordinate_switch/switch"
	cd /home/jinwei/catkin_ws/build/coordinate_switch && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/switch.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
coordinate_switch/CMakeFiles/switch.dir/build: /home/jinwei/catkin_ws/devel/lib/coordinate_switch/switch

.PHONY : coordinate_switch/CMakeFiles/switch.dir/build

coordinate_switch/CMakeFiles/switch.dir/requires: coordinate_switch/CMakeFiles/switch.dir/src/switch.cpp.o.requires

.PHONY : coordinate_switch/CMakeFiles/switch.dir/requires

coordinate_switch/CMakeFiles/switch.dir/clean:
	cd /home/jinwei/catkin_ws/build/coordinate_switch && $(CMAKE_COMMAND) -P CMakeFiles/switch.dir/cmake_clean.cmake
.PHONY : coordinate_switch/CMakeFiles/switch.dir/clean

coordinate_switch/CMakeFiles/switch.dir/depend:
	cd /home/jinwei/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jinwei/catkin_ws/src /home/jinwei/catkin_ws/src/coordinate_switch /home/jinwei/catkin_ws/build /home/jinwei/catkin_ws/build/coordinate_switch /home/jinwei/catkin_ws/build/coordinate_switch/CMakeFiles/switch.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : coordinate_switch/CMakeFiles/switch.dir/depend

