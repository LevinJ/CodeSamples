cmake_minimum_required(VERSION 3.0.0)
project(gsstream_test VERSION 0.1.0)

include(CTest)
enable_testing()
# Gstreamer doesn't provide CMake files
find_package(PkgConfig REQUIRED)
pkg_check_modules(GSTREAMER REQUIRED gstreamer-1.0 IMPORTED_TARGET)
pkg_check_modules(GST_APP REQUIRED gstreamer-app-1.0 IMPORTED_TARGET)



add_executable(gsstream_test main.cpp)

target_link_libraries(gsstream_test PkgConfig::GSTREAMER PkgConfig::GST_APP)
target_include_directories(gsstream_test PUBLIC
  "$<BUILD_INTERFACE:${GSTREAMER_INCLUDE_DIRS}>")

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
