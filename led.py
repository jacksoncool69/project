#!/usr/bin/python3

import os
import sys
sys.path.append(os.path.abspath('.'))

from piclap import *

import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep

red = LED(2)

class Config(Settings):
    '''Describes custom configurations and action methods to be executed based
    on the number of claps detected.
    '''

    def __init__(self):
        Settings.__init__(self)
        self.method.value = 2200

    def on2Claps(self):
        '''Custom action for 2 claps'''
        if red.is_lit:
            red.off()
            print("Light off")
        else:
            red.on()
            print("Light flashed")
    def on3Claps(self):
        '''Custom action for 3 claps'''
        print("light blinking")
        red.off()
        sleep(1)
        red.on()
        sleep(1)
        red.off()
        sleep(1)
        red.on()
        sleep(1)
        red.off()

    def on4Claps(self):
        '''Custom action for 4 claps'''
        print("4 claps.. ")


def main():
    config = Config()
    listener = Listener(config=config, calibrate=False)
    listener.start()


if __name__ == '__main__':
    main()
