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

add_executable(voxel_grid_filter src/voxel_grid_filter.cpp)
target_link_libraries(voxel_grid_filter ${PCL_LIBRARIES})

add_executable(statistical_removal src/statistical_removal.cpp)
target_link_libraries(statistical_removal ${PCL_LIBRARIES})

add_executable(icp_test src/icp_test.cpp)
target_link_libraries(icp_test ${PCL_LIBRARIES})

#add_executable(incr_registration src/incr_registration.cpp)
#target_link_libraries(incr_registration ${PCL_LIBRARIES})

add_executable(interactive_icp src/interactive_icp.cpp)
target_link_libraries(interactive_icp ${PCL_LIBRARIES})