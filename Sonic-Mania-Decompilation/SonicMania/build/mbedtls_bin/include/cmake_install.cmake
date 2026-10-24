# Install script for directory: C:/src/APCpp/build/mbedtls-3.6.4/include

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Program Files (x86)/APCpp")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
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
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mbedtls" TYPE FILE PERMISSIONS OWNER_READ OWNER_WRITE GROUP_READ WORLD_READ FILES
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/aes.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/aria.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/asn1.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/asn1write.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/base64.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/bignum.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/block_cipher.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/build_info.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/camellia.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/ccm.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/chacha20.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/chachapoly.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/check_config.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/cipher.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/cmac.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/compat-2.x.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/config_adjust_legacy_crypto.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/config_adjust_legacy_from_psa.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/config_adjust_psa_from_legacy.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/config_adjust_psa_superset_legacy.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/config_adjust_ssl.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/config_adjust_x509.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/config_psa.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/constant_time.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/ctr_drbg.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/debug.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/des.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/dhm.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/ecdh.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/ecdsa.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/ecjpake.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/ecp.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/entropy.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/error.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/gcm.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/hkdf.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/hmac_drbg.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/lms.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/mbedtls_config.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/md.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/md5.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/memory_buffer_alloc.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/net_sockets.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/nist_kw.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/oid.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/pem.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/pk.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/pkcs12.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/pkcs5.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/pkcs7.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/platform.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/platform_time.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/platform_util.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/poly1305.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/private_access.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/psa_util.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/ripemd160.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/rsa.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/sha1.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/sha256.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/sha3.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/sha512.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/ssl.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/ssl_cache.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/ssl_ciphersuites.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/ssl_cookie.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/ssl_ticket.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/threading.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/timing.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/version.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/x509.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/x509_crl.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/x509_crt.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/mbedtls/x509_csr.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/psa" TYPE FILE PERMISSIONS OWNER_READ OWNER_WRITE GROUP_READ WORLD_READ FILES
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/build_info.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_adjust_auto_enabled.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_adjust_config_dependencies.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_adjust_config_key_pair_types.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_adjust_config_synonyms.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_builtin_composites.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_builtin_key_derivation.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_builtin_primitives.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_compat.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_config.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_driver_common.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_driver_contexts_composites.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_driver_contexts_key_derivation.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_driver_contexts_primitives.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_extra.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_legacy.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_platform.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_se_driver.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_sizes.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_struct.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_types.h"
    "C:/src/APCpp/build/mbedtls-3.6.4/include/psa/crypto_values.h"
    )
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
if(CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "C:/src/APCpp/build/mbedtls_bin/include/install_local_manifest.txt"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
