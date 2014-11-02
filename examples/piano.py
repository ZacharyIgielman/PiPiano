#!/usr/bin/python
# piano.py
# turn your PiPiano into a piano, each button is an apropriate piano note
# Author : Zachary Igielman

# to run:
# sudo python piano.py

# Import all the libraries you need to read in button inputs and output to the buzzer
import RPi.GPIO as GPIO
import time
from Adafruit_I2C import Adafruit_I2C
from Adafruit_MCP230xx import *
import thread

# Define the GPIO pin that is used for the buzzer
buzzer_pin=26

# Specify the numbering scheme for the GPIO
GPIO.setmode(GPIO.BOARD)

# Set-up the buzzer pin as an output and also as a PWM so that we can play different tones
GPIO.setup(buzzer_pin, GPIO.OUT)
myPWM=GPIO.PWM(buzzer_pin, 10)
myPWM.start(0)

# Specify an array of PWM values so that we can play the correct tones depending on the button press
scale=[262,294,330,349,392,440,494,524,277,311,370,415,466]

# Determine which version of the Raspberry Pi we are using to make sure that the 
# PiPiano's chip is picked up
myBus=""
if GPIO.RPI_REVISION == 1:
    myBus=0
else:
    myBus=1

# Start-up the chip on the PiPiano and specify the number of pins it has on it
mcp = Adafruit_MCP230XX(busnum = myBus, address = 0x20, num_gpios = 16)

# Set-up all the buttons as 'pull-ups' and then turn them all off.
i=0
while i<13:
    mcp.pullup(i,1)
    i=i+1
i=13
while i<16:
    mcp.config(i,0)
    i=i+1

# Create a function to control the LEDs
def light(a,b,c):
    mcp.output(13,a)
    mcp.output(14,b)
    mcp.output(15,c)

# Create a function to help you keep time by lighting up the LEDs in a pattern with
# a steady gap between the changes
def metronome():
    while True:
        light(1,0,0)
        time.sleep(0.5)
        light(0,1,0)
        time.sleep(0.5)
        light(0,0,1)
        time.sleep(0.5)

# Start the metronome up in a 'thread' which means it will continue to run while
# you are reading in button presses
thread.start_new_thread(metronome, ())

# Initialise an array which holds the values of all the buttons
last=[0,0,0,0,0,0,0,0,0,0,0,0,0]

while True:
    i=0
    x=0
    # Read in button inputs and keep track of what the last set of button presses was
    # Change the frequency of the buzzer to whatever buttons are being pressed
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
