#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "graphviz::gvc" for configuration "Release"
set_property(TARGET graphviz::gvc APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(graphviz::gvc PROPERTIES
  IMPORTED_IMPLIB_RELEASE "${_IMPORT_PREFIX}/lib/gvc.lib"
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELEASE "graphviz::cdt;graphviz::cgraph"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/gvc.dll"
  )

list(APPEND _cmake_import_check_targets graphviz::gvc )
list(APPEND _cmake_import_check_files_for_graphviz::gvc "${_IMPORT_PREFIX}/lib/gvc.lib" "${_IMPORT_PREFIX}/bin/gvc.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
