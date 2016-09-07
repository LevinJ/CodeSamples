# this one is important
SET(CMAKE_SYSTEM_NAME Linux)


# specify the cross compiler
SET(CMAKE_C_COMPILER   "C:/Program Files (x86)/CodeSourcery/Sourcery_CodeBench_Lite_for_ARM_GNU_Linux/bin/arm-none-linux-gnueabi-gcc.exe")
SET(CMAKE_CXX_COMPILER "C:/Program Files (x86)/CodeSourcery/Sourcery_CodeBench_Lite_for_ARM_GNU_Linux/bin/arm-none-linux-gnueabi-g++.exe")

# where is the target environment 
#SET(CMAKE_FIND_ROOT_PATH  ./)

# search for programs in the build host directories
SET(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
# for libraries and headers in the target directories
SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)