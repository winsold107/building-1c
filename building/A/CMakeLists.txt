cmake_minimum_required(VERSION 3.7)
project(A)
add_custom_command(
  OUTPUT index.h
  COMMAND python preparing.py index.h
  DEPENDS preparing.py
)
add_library(A SHARED index.h)
set_target_properties(A PROPERTIES LINKER_LANGUAGE CXX)