#!/usr/bin/python
# genSonicPi.py
# this enables you to press the buttoins on PiPiano like a piano, and will generate a text file with code for sonic pi which will turn the button presses into real sounds when you copy it into sonic pi
# Author : Zachary Igielman

# to run:
# sudo python genSonicPi.py

import RPi.GPIO as GPIO
import time
from Adafruit_I2C import Adafruit_I2C
from Adafruit_MCP230xx import *
import thread

file_name=time.strftime("%Y%m%d_%H%M.txt")
file=open(file_name,"w")

GPIO.setmode(GPIO.BOARD)

scale=[60,62,64,65,67,69,71,72,61,63,66,68,70]

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
i=13
while i<16:
    mcp.config(i,0)
    i=i+1

def light(a,b,c):
    mcp.output(13,a)
    mcp.output(14,b)
    mcp.output(15,c)

def metronome():
    while True:
        light(1,0,0)
        time.sleep(0.5)
        light(0,1,0)
        time.sleep(0.5)
        light(0,0,1)
        time.sleep(0.5)

thread.start_new_thread(metronome, ())

try:
    while True:
        i=0
        while i<13:
            if not (mcp.input(i)):
                file.write("play "+str(scale[i])+"\n")
            i=i+1
        time.sleep(0.05)
        file.write("sleep 0.05\n")
finally:
    file.close()
