cmake_minimum_required (VERSION 2.6)
project (main)
FIND_PACKAGE( Boost 1.5 COMPONENTS program_options regex unit_test_framework REQUIRED )
INCLUDE_DIRECTORIES( ${Boost_INCLUDE_DIR} )

ADD_EXECUTABLE( main testhello.cpp )

TARGET_LINK_LIBRARIES( main ${Boost_LIBRARIES} )

message(STATUS "Boost_INCLUDE_DIR  ${Boost_INCLUDE_DIR}")
message(STATUS "Boost_LIBRARIES   ${Boost_LIBRARIES}")


