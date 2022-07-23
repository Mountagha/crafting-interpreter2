# Set the minimum version of CMake that can be used
# To find the cmake version run
# $ cmake --version
cmake_minimum_required(VERSION 3.5)

# set the c version
set(CMAKE_C_STANDARD 99)
# Set the project name
project (crafting-interpreters)

add_compile_options(-g)

# include_directories("include")
file(GLOB SOURCES "*.c")

# Add an executable
add_executable(interpreter ${SOURCES})