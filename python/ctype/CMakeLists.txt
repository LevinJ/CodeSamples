cmake_minimum_required(VERSION 3.5)
project(foo)
set(CMAKE_BUILD_TYPE Release)


#However, the file(GLOB...) allows for wildcard additions:
file(GLOB SOURCES "*.cpp")

#Generate the shared library from the sources
add_library(foo SHARED ${SOURCES})

#Set the location for library installation -- i.e., /usr/local/lib in this case
# not really necessary in this example. Use "sudo make install" to apply
install(TARGETS foo DESTINATION /usr/local/lib)