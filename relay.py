#!/usr/bin/python3

import os
import sys
sys.path.append(os.path.abspath('.'))

from piclap import *

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
class Config(Settings):
    '''Describes custom configurations and action methods to be executed based
    on the number of claps detected.
    '''

    def __init__(self):
        Settings.__init__(self)
        self.method.value = 2200

    def on2Claps(self):
        '''Custom action for 2 claps'''
        GPIO.output(3, False)
    def on3Claps(self):
        '''Custom action for 3 claps'''
        GPIO.output(3, True)

    def on4Claps(self):
        '''Custom action for 4 claps'''
        print("4 claps.. ")


def main():
    config = Config()
    listener = Listener(config=config, calibrate=False)
    listener.start()


if __name__ == '__main__':
    main()
