# cmake needs this line
cmake_minimum_required(VERSION 2.8)

# Define project name
project(opencv_example_project)

set(OpenCV_DIR "/home/levin/workspace/opencv/build_30rc1/install/share/OpenCV")
set(CMAKE_BUILD_TYPE Debug)


# Find OpenCV, you may need to set OpenCV_DIR variable
# to the absolute path to the directory containing OpenCVConfig.cmake file
# via the command line or GUI
find_package(OpenCV REQUIRED)

# If the package has been found, several variables will
# be set, you can find the full list with descriptions
# in the OpenCVConfig.cmake file.
# Print some message showing some of them
message(STATUS "OpenCV library status:")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")
message("Generated with config types: ${CMAKE_CONFIGURATION_TYPES}")

# Add OpenCV headers location to your include paths
include_directories(${OpenCV_INCLUDE_DIRS})

# Declare the executable target built from your sources
file(GLOB SOURCES ".//*.cpp")
message("SOURCES: ${SOURCES}")

add_executable(cvtest SOURCES)

# Link your application with OpenCV libraries
target_link_libraries(cvtest ${OpenCV_LIBS})
