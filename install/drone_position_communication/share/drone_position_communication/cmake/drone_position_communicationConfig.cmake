# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_drone_position_communication_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED drone_position_communication_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(drone_position_communication_FOUND FALSE)
  elseif(NOT drone_position_communication_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(drone_position_communication_FOUND FALSE)
  endif()
  return()
endif()
set(_drone_position_communication_CONFIG_INCLUDED TRUE)

# output package information
if(NOT drone_position_communication_FIND_QUIETLY)
  message(STATUS "Found drone_position_communication: 0.0.0 (${drone_position_communication_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'drone_position_communication' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${drone_position_communication_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(drone_position_communication_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${drone_position_communication_DIR}/${_extra}")
endforeach()
