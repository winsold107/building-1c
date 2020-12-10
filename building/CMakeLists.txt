cmake_minimum_required(VERSION 3.7)
project(building)

find_package(Python COMPONENTS Interpreter Development)
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_SOURCE_DIR}/bin)
set(LIBRARY_OUTPUT_PATH ${CMAKE_SOURCE_DIR}/lib)

include_directories("${PROJECT_SOURCE_DIR}")
add_subdirectory("A")
add_subdirectory("B")
set(SOURCE_FILES B/lib.cpp C/main.cpp)
add_executable(build ${SOURCE_FILES})
