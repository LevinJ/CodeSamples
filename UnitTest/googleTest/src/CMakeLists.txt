cmake_minimum_required (VERSION 2.6)
project (main)
find_package (Threads)

set(GMOCK_LIB  "/home/developer/projects/CodeSamples/gmock-1.7.0/build/libgmock_main.a")
set(GMOCK_HEADERS "../../../gmock-1.7.0/include")
set(GTEST_HEADERS "../../../gmock-1.7.0/gtest/include")

include_directories(${GMOCK_HEADERS}  ${GTEST_HEADERS})
add_executable( main testcase.cpp testmock.cpp testfixture.cpp)

TARGET_LINK_LIBRARIES( main ${CMAKE_THREAD_LIBS_INIT} ${GMOCK_LIB} )

message(STATUS "INCLUDE_DIRECTORIES:   ${INCLUDE_DIRECTORIES}")



