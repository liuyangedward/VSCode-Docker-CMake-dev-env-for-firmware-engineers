set(CPU_ARCH cortex-m4)
set(FPU_ARCH fpv4-sp-d16)
set(FLOAT_ABI hard)
set(ARM_ASM mthumb)
set(SPECS nano.specs)
set(LINKER_SCRIPT ${CMAKE_CURRENT_SOURCE_DIR}/STM32L475VGTX_FLASH.ld)

set(CMAKE_C_COMPILER arm-none-eabi-gcc)
set(CMAKE_ASM_COMPILER arm-none-eabi-gcc)

set(CMAKE_C_FLAGS "-mcpu=${CPU_ARCH} -std=gnu11 -DUSE_HAL_DRIVER -DSTM32L475xx --specs=${SPECS} -mfpu=${FPU_ARCH} -mfloat-abi=${FLOAT_ABI} -${ARM_ASM} -T${LINKER_SCRIPT} -Wl,--gc-sections -fmessage-length=0 -ffunction-sections -fdata-sections")
set(CMAKE_ASM_FLAGS	"-mcpu=${CPU_ARCH} -x assembler-with-cpp --specs=${SPECS} -mfpu=${FPU_ARCH} -mfloat-abi=${FLOAT_ABI} -${ARM_ASM}")

