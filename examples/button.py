#!/usr/bin/python
# button.py
# Detects button presses and prints which button is pressed
# Author : Zachary Igielman

# To run this script, type the following command:
# sudo python button.py

# First of all, import the library to access the Pi's GPIO pins
import RPi.GPIO as GPIO

# Now import a library that lets us build delays into our code
import time

# Then, import two libraries which enable us to communicate with the chip on the PiPiano
from Adafruit_I2C import Adafruit_I2C
from Adafruit_MCP230xx import *

# This bit of code works out whether we are using a newer or older Raspberry Pi
myBus=""
if GPIO.RPI_REVISION == 1:
    myBus=0
else:
    myBus=1

# This communicates with the PiPiano chip and sets it up
mcp = Adafruit_MCP230XX(busnum = myBus, address = 0x20, num_gpios = 16)

# This bit of code loops through all the buttons, sets 'pull ups' on them and makes them inputs
i=0
while i<13:
    mcp.pullup(i,1)
    i=i+1

# Loop forever
while True:
    # Print a blank line to help us read the screen easier
    print("")
    # Print "Buttons pressed:". The comma tells Python not to print a carriage return character
    print("Buttons pressed: "),

    # Read each of the 13 buttons on the PiPiano and if any are pressed print out the number of the button 
    i=0
    while i<13:
        if not (mcp.input(i)):
            print(str(i) + " "),
        i=i+1
