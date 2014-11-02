#!/usr/bin/python
# genSonicPi.py
# This enables you to press the buttons on PiPiano like a piano
# and will generate a text file with code for Sonic Pi which will turn the 
# button presses into real sounds when you copy it into Sonic Pi
# Author : Zachary Igielman

# to run:
# sudo python genSonicPi.py

# Import all the libraries you need to read the button presses and to light the LEDs
import RPi.GPIO as GPIO
import time
from Adafruit_I2C import Adafruit_I2C
from Adafruit_MCP230xx import *
import thread

# Define the name of the file you will be creating. This file will contain commands
# that can be copied into Sonic Pi
file_name=time.strftime("%Y%m%d_%H%M.txt")
file=open(file_name,"w")

# Specify the numbering scheme you will be using for the GPIO
GPIO.setmode(GPIO.BOARD)

# Define the musical scale as Sonic Pi 'notes'
scale=[60,62,64,65,67,69,71,72,61,63,66,68,70]

# Work out which version of the Pi you are using so that the PiPiano chip gets picked up
myBus=""
if GPIO.RPI_REVISION == 1:
    myBus=0
else:
    myBus=1

# Access the chip on the PiPiano and set it up correctly
mcp = Adafruit_MCP230XX(busnum = myBus, address = 0x20, num_gpios = 16)

# Set-up the pins on the PiPiano's MCP chip. Define them as 'pull-ups' (i.e. default to 1)
# and then turn them all OFF to start with.
i=0
while i<13:
    mcp.pullup(i,1)
    i=i+1
i=13
while i<16:
    mcp.config(i,0)
    i=i+1

# Create a function that will allow you to light up the PiPiano's LEDs
def light(a,b,c):
    mcp.output(13,a)
    mcp.output(14,b)
    mcp.output(15,c)

# Create a loop which will light up the LEDs in strict time - essentially creating
# a metronome out of your LEDs.
def metronome():
    while True:
        light(1,0,0)
        time.sleep(0.5)
        light(0,1,0)
        time.sleep(0.5)
        light(0,0,1)
        time.sleep(0.5)

# Start up the metronome in a thread. This means that the metronome will continue to light
# up the LEDs even while you are reading the button presses.
thread.start_new_thread(metronome, ())

try:
	# Do the main loop (reading in button presses) forever
	# ZACH - this needs to change to catch the KeyboardInterrupt exception 
	# otherwise the file will never be closed when Ctrl-C is pressed
    while True:
        i=0

		# Loop over the 13 button inputs, detect button presses and add
		# the Sonic Pi command to the file
        while i<13:
            if not (mcp.input(i)):
                file.write("play "+str(scale[i])+"\n")
            i=i+1
        time.sleep(0.05)

        # Add a pause to the Sonic Pi command file in line with the actual pauses between
        # button presses 
        file.write("sleep 0.05\n")

finally:
	# Close the file when the program finishes
    file.close()
