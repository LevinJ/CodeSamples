cmake_minimum_required (VERSION 2.6)
project (Tutorial)
# The version number.
#set (Tutorial_VERSION_MAJOR 1)
SET(Tutorial_VERSION_MAJOR 2 CACHE STRING Tutorial_VERSION_MAJOR)
set (Tutorial_VERSION_MINOR 0 CACHE STRING Tutorial_VERSION_MAJOR)
 
# configure a header file to pass some of the CMake settings
# to the source code
configure_file (
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  )
 
 MESSAGE(STATUS "PROJECT_BINARY_DIR:         " ${PROJECT_BINARY_DIR})
# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
include_directories("${PROJECT_BINARY_DIR}")
 
# add the executable
add_executable(Tutorial tutorial.cxx)
