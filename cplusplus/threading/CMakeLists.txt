project(THREADTEST)

find_package (Threads)
cmake_minimum_required (VERSION 3.5)

add_definitions("-std=c++11")

set(CXX_FLAGS "-Wall")
set(CMAKE_CXX_FLAGS, "${CXX_FLAGS}")

set(sources src/launch_thread.cpp)




add_executable(test1 ${sources})
target_link_libraries(test1 Threads::Threads)
