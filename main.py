#!/usr/bin/env python
"""
Info about our project comes here.
"""

from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
import time


__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"


remote_factory = PiGPIOFactory(host='192.168.0.252')
button1 = Button(pin=17, pin_factory=remote_factory)
button2 = Button(pin=27, pin_factory=remote_factory)
button3 = Button(pin=22, pin_factory=remote_factory)


def main():
    counter = 0
    while True:
         if button1.is_pressed:
             time.sleep(1)
             counter = counter+1
             print(counter)

         if button2.is_pressed:
            time.sleep(1)
            counter = counter-1
            print(counter)

         if button3.is_pressed:
             time.sleep(1)
            counter = 0
            print(counter)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
