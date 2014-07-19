#!/usr/bin/python
# multitonePygameSampler.py
# this enables you to press the buttoins on PiPiano like a piano, and will play the sounds out of the Pi's audio output like a proper keyboard
# Author : Zachary Igielman

# to run:
# sudo python multitonePygameSampler.py

# to change volume:
# amizer cset numid=1 -- 80%

# to change audio outout for Pi (audio jack/HDMI)
# amixer cset numid=3 0 (for auto-detect)
# amixer cset numid=3 1 (for analog)
# amixer cset numid=3 2 (for HDMI)

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

myBus=""
if GPIO.RPI_REVISION == 1:
    myBus=0
elif GPIO.RPI_REVISION == 2:
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

while True:
    i=0
    while i<13:
        if mcp.input(i)!=last[i]:
            if not mcp.input(i):
                sounds[i].play(loops=-1)
            else:
                sounds[i].stop()
        last[i]=mcp.input(i)
        i=i+1
