cmake_minimum_required(VERSION 3.10)
project(main)

set(CMAKE_BUILD_TYPE Debug)
include_directories(./src)
add_executable(main  src/main.cpp)
target_link_libraries(main  lcm) 
