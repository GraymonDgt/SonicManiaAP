# Install script for directory: C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/src/vcpkg/packages/sdl2_x64-windows-static/debug")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "OFF")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "C:/src/vcpkg/buildtrees/sdl2/x64-windows-static-dbg/SDL2maind.lib")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE OPTIONAL FILES "C:/src/vcpkg/buildtrees/sdl2/x64-windows-static-dbg/CMakeFiles/SDL2main.dir/SDL2main.pdb")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "C:/src/vcpkg/buildtrees/sdl2/x64-windows-static-dbg/SDL2-staticd.lib")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE OPTIONAL FILES "C:/src/vcpkg/buildtrees/sdl2/x64-windows-static-dbg/CMakeFiles/SDL2-static.dir/SDL2-static.pdb")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/cmake/SDL2mainTargets.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/cmake/SDL2mainTargets.cmake"
         "C:/src/vcpkg/buildtrees/sdl2/x64-windows-static-dbg/CMakeFiles/Export/272ceadb8458515b2ae4b5630a6029cc/SDL2mainTargets.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/cmake/SDL2mainTargets-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/cmake/SDL2mainTargets.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE FILE FILES "C:/src/vcpkg/buildtrees/sdl2/x64-windows-static-dbg/CMakeFiles/Export/272ceadb8458515b2ae4b5630a6029cc/SDL2mainTargets.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE FILE FILES "C:/src/vcpkg/buildtrees/sdl2/x64-windows-static-dbg/CMakeFiles/Export/272ceadb8458515b2ae4b5630a6029cc/SDL2mainTargets-debug.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/cmake/SDL2staticTargets.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/cmake/SDL2staticTargets.cmake"
         "C:/src/vcpkg/buildtrees/sdl2/x64-windows-static-dbg/CMakeFiles/Export/272ceadb8458515b2ae4b5630a6029cc/SDL2staticTargets.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/cmake/SDL2staticTargets-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/cmake/SDL2staticTargets.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE FILE FILES "C:/src/vcpkg/buildtrees/sdl2/x64-windows-static-dbg/CMakeFiles/Export/272ceadb8458515b2ae4b5630a6029cc/SDL2staticTargets.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE FILE FILES "C:/src/vcpkg/buildtrees/sdl2/x64-windows-static-dbg/CMakeFiles/Export/272ceadb8458515b2ae4b5630a6029cc/SDL2staticTargets-debug.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Devel" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE FILE FILES
    "C:/src/vcpkg/buildtrees/sdl2/x64-windows-static-dbg/SDL2Config.cmake"
    "C:/src/vcpkg/buildtrees/sdl2/x64-windows-static-dbg/SDL2ConfigVersion.cmake"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/cmake/sdlfind.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/SDL2" TYPE FILE FILES
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_assert.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_atomic.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_audio.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_bits.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_blendmode.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_clipboard.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_copying.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_cpuinfo.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_egl.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_endian.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_error.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_events.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_filesystem.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_gamecontroller.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_gesture.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_guid.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_haptic.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_hidapi.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_hints.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_joystick.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_keyboard.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_keycode.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_loadso.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_locale.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_log.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_main.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_messagebox.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_metal.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_misc.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_mouse.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_mutex.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_name.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_opengl.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_opengl_glext.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_opengles.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_opengles2.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_opengles2_gl2.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_opengles2_gl2ext.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_opengles2_gl2platform.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_opengles2_khrplatform.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_pixels.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_platform.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_power.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_quit.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_rect.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_render.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_rwops.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_scancode.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_sensor.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_shape.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_stdinc.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_surface.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_system.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_syswm.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_test.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_test_assert.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_test_common.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_test_compare.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_test_crc32.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_test_font.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_test_fuzzer.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_test_harness.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_test_images.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_test_log.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_test_md5.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_test_memory.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_test_random.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_thread.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_timer.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_touch.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_types.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_version.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_video.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/SDL_vulkan.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/begin_code.h"
    "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/include/close_code.h"
    "C:/src/vcpkg/buildtrees/sdl2/x64-windows-static-dbg/include/SDL2/SDL_revision.h"
    "C:/src/vcpkg/buildtrees/sdl2/x64-windows-static-dbg/include-config-debug/SDL2/SDL_config.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/licenses/SDL2" TYPE FILE FILES "C:/src/vcpkg/buildtrees/sdl2/src/se-2.32.10-89f6bbf859.clean/LICENSE.txt")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "C:/src/vcpkg/buildtrees/sdl2/x64-windows-static-dbg/sdl2.pc")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
if(CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "C:/src/vcpkg/buildtrees/sdl2/x64-windows-static-dbg/install_local_manifest.txt"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
if(CMAKE_INSTALL_COMPONENT)
  if(CMAKE_INSTALL_COMPONENT MATCHES "^[a-zA-Z0-9_.+-]+$")
    set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
  else()
    string(MD5 CMAKE_INST_COMP_HASH "${CMAKE_INSTALL_COMPONENT}")
    set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INST_COMP_HASH}.txt")
    unset(CMAKE_INST_COMP_HASH)
  endif()
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "C:/src/vcpkg/buildtrees/sdl2/x64-windows-static-dbg/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
