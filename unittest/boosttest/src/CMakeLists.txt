cmake_minimum_required (VERSION 2.6)
project (main)

set(Boost_DEBUG ON)
SET(BOOST_INCLUDEDIR "../../../boost_1_58_0/build/include")
SET(BOOST_LIBRARYDIR "../../../boost_1_58_0/build/lib")

FIND_PACKAGE( Boost 1.58.0 COMPONENTS program_options regex unit_test_framework REQUIRED )


set(TURTLE_HEADERS  "../../../turtle-1.2.7/include")


INCLUDE_DIRECTORIES( ${Boost_INCLUDE_DIR} ${TURTLE_HEADERS})

ADD_EXECUTABLE( main UTDriver.cpp testcase.cpp testfixture.cpp testmock.cpp)


TARGET_LINK_LIBRARIES( main ${Boost_LIBRARIES} )



if(Boost_FOUND)
  message(STATUS "Boost_INCLUDE_DIR  ${Boost_INCLUDE_DIR}")
  message(STATUS "Boost_LIBRARIES   ${Boost_LIBRARIES}")
endif()
