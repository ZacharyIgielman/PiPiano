#!/usr/bin/python
# piano.py
# turn your PiPiano into a piano, each button is an apropriate piano note
# Author : Zachary Igielman

# to run:
# sudo python piano.py

import RPi.GPIO as GPIO
import time
from Adafruit_I2C import Adafruit_I2C
from Adafruit_MCP230xx import *
import thread

buzzer_pin=26

GPIO.setmode(GPIO.BOARD)

GPIO.setup(buzzer_pin, GPIO.OUT)
myPWM=GPIO.PWM(buzzer_pin, 10)
myPWM.start(0)

scale=[262,294,330,349,392,440,494,524,277,311,370,415,466]

myBus=""
if GPIO.RPI_REVISION == 1:
    myBus=0
else:
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

last=[0,0,0,0,0,0,0,0,0,0,0,0,0]

while True:
    i=0
    x=0
    while i<13:
        if not mcp.input(i):
            x=x+1
        if not (mcp.input(i)) and mcp.input(i)!=last[i]:
            myPWM.ChangeFrequency(scale[i])
            print i
        last[i]=mcp.input(i)
        i=i+1
    if x>0:
        myPWM.ChangeDutyCycle(50)
    else:
        myPWM.ChangeDutyCycle(0)
