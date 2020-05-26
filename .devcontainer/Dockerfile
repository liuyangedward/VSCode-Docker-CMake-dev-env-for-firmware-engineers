FROM ubuntu:19.10 as DEV_STM32

# Install required packages
RUN apt-get update && \
        apt-get install -y \
        git \
        curl \
        wget \
        # Build tools
        gcc-arm-none-eabi \ 
        # Program and debug tools (libtinfo5 and libncurses5 are deps of arm-none-eabi-gdb)
        stlink-tools \
        openocd \
        libtinfo5 \
        libncurses5 \
        # Python
        python \
        python-pip \
        python-serial \
        # Clang
        clang \
        clang-format \
        clang-tidy

# Get Python components
RUN pip install watchdog autopep8

# Get CMake
RUN mkdir cmake && \
        cd cmake && \
        wget https://github.com/Kitware/CMake/releases/download/v3.16.0-rc2/cmake-3.16.0-rc2-Linux-x86_64.sh && \
        chmod +x cmake-3.16.0-rc2-Linux-x86_64.sh && \
        ./cmake-3.16.0-rc2-Linux-x86_64.sh --skip-license && \
        mv ./bin/* /usr/local/bin && \
        mv ./man/* /usr/local/man && \
        mv ./share/* /usr/local/share && \
        cd .. && \
        rm -rf cmake 
