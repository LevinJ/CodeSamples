cmake_minimum_required (VERSION 3.5)

project (main)

SET(CMAKE_BUILD_TYPE Debug)
MESSAGE("Build type: " ${CMAKE_BUILD_TYPE})

find_package(log4cplus 2.0 REQUIRED)

file(GLOB SOURCES "src/*.cpp")
add_executable(main ${SOURCES} )

target_link_libraries(main log4cplus)
