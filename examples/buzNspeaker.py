#!/usr/bin/python
# Author : Zachary Igielman

import RPi.GPIO as GPIO
import time
from Adafruit_I2C import Adafruit_I2C
from Adafruit_MCP230xx import *
import thread
import pygame
import itertools

samples=["C4.wav","D4.wav","E4.wav","F4.wav","G4.wav","A4.wav","B4.wav","C5.wav","Csharp4.wav","Dsharp4.wav","Fsharp4.wav","Gsharp4.wav","Asharp4.wav"]
pygame.mixer.init()
pygame.mixer.set_num_channels(13)

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
sounds=[]*13
while i<13:
    mcp.pullup(i,1)
    sounds.append(pygame.mixer.Sound(samples[i]))
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

def samplerThread():
    while True:
        l=0
        while l<13:
            if mcp.input(l)!=last[l]:
                if not mcp.input(l):
                    sounds[l].play(loops=-1)
                else:
                    sounds[l].stop()
            last[i]=mcp.input(l)
            l=l+1
thread.start_new_thread(samplerThread, ())

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
