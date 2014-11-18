#!/usr/bin/python
# trafficLight.py
# loops through red, yellow, green like a traffic light
# Author : Zachary Igielman

# to run:
# sudo python trafficLight.py

# Import the libraries necessary for changing the state of the LEDs
import RPi.GPIO as GPIO
import time
from Adafruit_I2C import Adafruit_I2C
from Adafruit_MCP230xx import *

# Determine the version of Raspberry Pi so the chip on the PiPiano gets picked up 
myBus=""
if GPIO.RPI_REVISION == 1:
    myBus=0
else:
    myBus=1

# Initialise the chip on the PiPiano and specify how many pins it has
mcp = Adafruit_MCP230XX(busnum = myBus, address = 0x20, num_gpios = 16)

# Setup the LED pins as outputs
i=13
while i<16:
    mcp.config(i,0)
    i=i+1

# Create a function that turns the LEDs on/off depending on what values are sent to it when the function is called
def light(a,b,c):
    mcp.output(13,a)
    mcp.output(14,b)
    mcp.output(15,c)

# Turn the LEDs on/off in the 'traffic lights sequence' 
while True:
    light(1,0,0)
    time.sleep(3)
    light(1,1,0)
    time.sleep(1)
    light(0,0,1)
    time.sleep(5)
    light(0,1,0)
    time.sleep(1)
