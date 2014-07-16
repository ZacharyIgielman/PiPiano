#!/usr/bin/python
# button.py
# detects button presses and prints which button is pressed
# Author : Zachary Igielman

import RPi.GPIO as GPIO
import time
from Adafruit_I2C import Adafruit_I2C
from Adafruit_MCP230xx import *

myBus=""
if GPIO.RPI_REVISION == 1:
    myBus=0
elif GPIO.RPI_REVISION == 2:
    myBus=1

mcp = Adafruit_MCP230XX(busnum = myBus, address = 0x20, num_gpios = 16)

i=0
while i<13:
    mcp.pullup(i,1)
    i=i+1

while True:
    print("")
    print("Buttons pressed: "),
    i=0
    while i<13:
        if not (mcp.input(i)):
            print(str(i) + " "),
        i=i+1
