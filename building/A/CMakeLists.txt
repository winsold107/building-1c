cmake_minimum_required(VERSION 3.7)
project(A)

find_package(Python COMPONENTS Interpreter Development)
add_custom_command(
  OUTPUT index.h
  COMMAND python3 ${PROJECT_SOURCE_DIR}/preparing.py ${PROJECT_SOURCE_DIR}/index.h
  DEPENDS preparing.py
)
add_library(A SHARED index.h)
set_target_properties(A PROPERTIES LINKER_LANGUAGE CXX)