#!/usr/bin/python
# trafficLight.py
# loops through red, yellow, green like a traffic light
# Author : Zachary Igielman

# to run:
# sudo python trafficLight.py

import RPi.GPIO as GPIO
import time
from Adafruit_I2C import Adafruit_I2C
from Adafruit_MCP230xx import *

myBus=""
if GPIO.RPI_REVISION == 1:
    myBus=0
else:
    myBus=1

mcp = Adafruit_MCP230XX(busnum = myBus, address = 0x20, num_gpios = 16)

i=13
while i<16:
    mcp.config(i,0)
    i=i+1

def light(a,b,c):
    mcp.output(13,a)
    mcp.output(14,b)
    mcp.output(15,c)

while True:
    light(1,0,0)
    time.sleep(3)
    light(1,1,0)
    time.sleep(1)
    light(0,0,1)
    time.sleep(5)
    light(0,1,0)
    time.sleep(1)
