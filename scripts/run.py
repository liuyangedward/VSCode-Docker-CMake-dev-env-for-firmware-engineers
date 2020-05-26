#!/usr/bin/python

import sys
import os
import shutil
import serial

WORKSPACE_ROOT = os.path.dirname(os.path.realpath(__file__)) + "/../.."

class STM32L475VG:
    STM32L475VG_DEFAULT_BAUD = 115200
    buildDir = "build"

    def build(self, projectName):
        print('--------------Building--------------')
        os.chdir('..')
        if not os.path.exists(self.buildDir):
            os.mkdir(self.buildDir)
        os.chdir(self.buildDir)
        os.system("cmake .. -DPROJECT_NAME={}".format(projectName))
        os.system("cmake --build .")
        os.chdir('..')

    def flash(self, source):
        print('\n--------------Flashing--------------')
        os.chdir(self.buildDir)
        filename = "{}.bin".format(source)
        if not os.path.exists(filename):
            raise Exception("File {} not built!\n".format(filename))
        os.system("st-flash write {} 0x8000000".format(filename))
        os.chdir("..")

    def monitor(self, port):
        print('\n--------------Monitoring--------------')
        serial_instance = serial.serial_for_url(
            port, self.STM32L475VG_DEFAULT_BAUD)
        os.system("st-flash reset")
        try:
            while True:
                sys.stdout.write(serial_instance.read(1))
                sys.stdout.flush()
        except KeyboardInterrupt:
            serial_instance.close()

    def run(self, port):
        self.clean()
        projectName = "My-Dev-Env"
        self.build(projectName)
        self.flash(projectName)
        self.monitor(port)

    def clean(self):
        if os.path.exists(self.buildDir):
            shutil.rmtree(self.buildDir)


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

if __name__ == "__main__":
    os.chdir(BASE_DIR)
    stm32l475vg = STM32L475VG()
    fun = sys.argv[1]
    if(fun == "run"):
        stm32l475vg.run(sys.argv[2])
    elif(fun == "monitor"):
        stm32l475vg.monitor(sys.argv[2])
    elif(fun == "build"):
        stm32l475vg.build("My-Dev-Env")
