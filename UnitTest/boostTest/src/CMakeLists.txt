cmake_minimum_required (VERSION 2.6)
project (main)
#FIND_PACKAGE( Boost 1.5 COMPONENTS program_options regex unit_test_framework REQUIRED )
libboost_unit_test_framework.a
set(BOOST_HEADERS  "../../../boost_1_58_0/build/include")
set(TURTLE_HEADERS  "../../../turtle-1.2.7/include")
set(BOOST_TESTLIBRARY  "/home/developer/projects/CodeSamples/boost_1_58_0/build/lib/libboost_unit_test_framework.a")

INCLUDE_DIRECTORIES( ${Boost_INCLUDE_DIR} ${TURTLE_HEADERS})

ADD_EXECUTABLE( main UTDriver.cpp testcase.cpp testfixture.cpp testmock.cpp)

TARGET_LINK_LIBRARIES( main ${BOOST_TESTLIBRARY} )

#message(STATUS "Boost_INCLUDE_DIR  ${Boost_INCLUDE_DIR}")
#message(STATUS "Boost_LIBRARIES   ${Boost_LIBRARIES}")


