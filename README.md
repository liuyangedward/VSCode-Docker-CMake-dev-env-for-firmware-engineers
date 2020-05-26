# VSCode-Docker-CMake-dev-env-for-firmware-engineers

## What is this repo about?

This repo contains a blinky sample app which runs on B-L475E-IOT01A (https://www.st.com/en/evaluation-tools/b-l475e-iot01a.html). Rather than the sample app, it's the development environment that I want to share. This dev env can be easily tailored to work with most of the popular MCUs in the markets, especially STM32 families.

This dev env includes:

- VSCode: A very popular text editor in software development world. It's lightweighted, fast and comes with heaps of 3rd party plugins devloped by its users which allows the VSCode to be integrated with many other tools.

- Docker: It provides a 100% deterministic dev env. It solves the classic headache that goes like "It works on my machine, why doen't it work on yours?"

- CMake: An build system for C/C++ based projects. IMO it's better than Makefile when used in large projects as many dependencies/libraries come with native CMake support.

- OpenOCD: A free programming&debugging tool. A debugger is optional in software development but I find it still quite useful for firmware devlopment.

## Why do you share it?

Nowadays MCU vendors tend to provide their own toolchains and IDEs. Some developers use STM32CubeIDE, some use KEIL, some use IAR embedded workbench. Nothing is standardized in the firmware industry. I'm tired of learning all the IDEs and their updates :( whenever I work on a new MCU or move to a new company. I believe there are other firmware engineers like me facing the same issue, thats why I open-sourced it.

## How to use it?

Though you can use this dev env on any hostOS, I'd recommand using Ubuntu as the host OS. Flashing the firmware seems to have an issue on non-linux based OS as the docker can't easily access the serial(USB) port from the container. (AFAIK this is solvable) Another reason is that docker runs way faster on Ubuntu than MacOS and Window, due to its own implementation.

You need to install VSCode, docker and docker compose to your host machine. Open this repo in VSCode and run it in remote container. (https://code.visualstudio.com/docs/remote/containers)

## Known issues:

The openOCD integration doesn't look the cleanest to me, though it works.