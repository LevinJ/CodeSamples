cmake_minimum_required(VERSION 2.6 FATAL_ERROR)

set(CMAKE_BUILD_TYPE DEBUG)
project(MY_GRAND_PROJECT)
find_package(PCL 1.3 REQUIRED)
include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})
add_executable(pcd_write_test src/pcd_write.cpp)
target_link_libraries(pcd_write_test ${PCL_LIBRARIES})

message(STATUS "PCL_VERSION = ${PCL_VERSION}")