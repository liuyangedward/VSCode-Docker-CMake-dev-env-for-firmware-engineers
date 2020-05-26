cmake_minimum_required(VERSION 3.16)

# Include the toolchain file
include(toolchain.cmake)

project(${PROJECT_NAME} C ASM)
set(TARGET ${PROJECT_NAME}.elf)

# Header file path
include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/Core/Inc
    ${CMAKE_CURRENT_SOURCE_DIR}/Drivers/STM32L4xx_HAL_Driver/Inc
    ${CMAKE_CURRENT_SOURCE_DIR}/Drivers/STM32L4xx_HAL_Driver/Inc/Legacy
    ${CMAKE_CURRENT_SOURCE_DIR}/Drivers/CMSIS/Device/ST/STM32L4xx/Include
    ${CMAKE_CURRENT_SOURCE_DIR}/Drivers/CMSIS/Include
)

# Source file path
file(GLOB_RECURSE 
    SOURCES
	${CMAKE_CURRENT_SOURCE_DIR}/Core/Startup/startup_stm32l475vgtx.s
    ${CMAKE_CURRENT_SOURCE_DIR}/Core/Src/*.c
    ${CMAKE_CURRENT_SOURCE_DIR}/Drivers/STM32L4xx_HAL_Driver/Src/*.c
)

# Build the elf file
add_executable(${PROJECT_NAME}.elf ${SOURCES})

# Build hex file and bin file
set(HEX_FILE ${PROJECT_BINARY_DIR}/build.hex)
set(BIN_FILE ${PROJECT_BINARY_DIR}/build.bin)
add_custom_command(TARGET ${TARGET} POST_BUILD
        COMMAND ${CMAKE_OBJCOPY} -Oihex $<TARGET_FILE:${TARGET}> ${PROJECT_NAME}.hex
        COMMAND ${CMAKE_OBJCOPY} -Obinary $<TARGET_FILE:${TARGET}> ${PROJECT_NAME}.bin
        COMMENT "Building ${HEX_FILE} and ${BIN_FILE}")
