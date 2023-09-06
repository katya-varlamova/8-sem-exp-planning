cmake_minimum_required(VERSION 3.5)

project(lab04 LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_compile_options(

	-Wall
	-Wextra
	-Wpedantic

	-Wcast-align
	-Wcast-qual
	-Wconversion
	-Wctor-dtor-privacy
	-Wenum-compare
	-Wfloat-equal
	-Wnon-virtual-dtor
	-Wold-style-cast
	-Woverloaded-virtual
	-Wredundant-decls
	-Wsign-conversion
	-Wsign-promo
)

set(
	HEADERS
	combinatorics.hpp
	experiment.hpp
	mainwindow.hpp
	random.hpp
	simulate.hpp
	statistics.hpp
)

set(
	SOURCES
	combinatorics.cpp
	experiment.cpp
	mainwindow.cpp
	random.cpp
	simulate.cpp
	statistics.cpp
)

set(
	FORMS
	mainwindow.ui
)

set(CMAKE_PREFIX_PATH "/Users/kate/Qt/6.0.2/clang_64/lib/cmake")
set(QT_VERSION 6)
set(REQUIRED_LIBS Core Gui Widgets)
set(REQUIRED_LIBS_QUALIFIED Qt6::Core Qt6::Gui Qt6::Widgets)

find_package(Qt${QT_VERSION} COMPONENTS ${REQUIRED_LIBS} REQUIRED)

add_executable(${PROJECT_NAME} ${HEADERS} ${SOURCES} ${FORMS} main.cpp)

target_link_libraries(${PROJECT_NAME} ${REQUIRED_LIBS_QUALIFIED})

