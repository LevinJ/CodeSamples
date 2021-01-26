cmake_minimum_required(VERSION 3.10)
project(main)

set(CMAKE_BUILD_TYPE Debug)
find_package(Eigen3 3.3.3 EXACT REQUIRED)
find_package(Ceres 1.14.0 EXACT REQUIRED)

message(STATUS "EIGEN3_INCLUDE_DIR=${EIGEN3_INCLUDE_DIR}")
message(STATUS "CERES_INCLUDE_DIRS=${CERES_INCLUDE_DIRS}")


include_directories(
  ${EIGEN3_INCLUDE_DIR}
  ${CERES_INCLUDE_DIRS}
)
include_directories(./src)
add_executable(test_ceres  src/main.cpp)
target_link_libraries(test_ceres  ceres) 

add_executable(curve_fitting  src/curve_fitting.cpp)
target_link_libraries(curve_fitting  ceres) 
