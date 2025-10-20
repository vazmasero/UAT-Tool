#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "graphviz::cdt" for configuration "Release"
set_property(TARGET graphviz::cdt APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(graphviz::cdt PROPERTIES
  IMPORTED_IMPLIB_RELEASE "${_IMPORT_PREFIX}/lib/cdt.lib"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/cdt.dll"
  )

list(APPEND _cmake_import_check_targets graphviz::cdt )
list(APPEND _cmake_import_check_files_for_graphviz::cdt "${_IMPORT_PREFIX}/lib/cdt.lib" "${_IMPORT_PREFIX}/bin/cdt.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
