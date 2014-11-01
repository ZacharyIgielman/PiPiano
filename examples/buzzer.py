#!/usr/bin/python
# buzzer.py
# Plays a scale on the buzzer
# Author : Zachary Igielman

# to run:
# sudo python buzzer.py

# Import the libraries you will be using
import RPi.GPIO as GPIO, time, sys

# Define the pin that the buzzer is on
buzzer_pin=26

# Specify which numbering scheme we're using on the board
GPIO.setmode(GPIO.BOARD)

# Set-up the buzzer as an output so we can produce sounds
GPIO.setup(buzzer_pin, GPIO.OUT)

# Set-up the buzzer as a PWM. This allows us to play different tones on one GPIO pin
myPWM=GPIO.PWM(buzzer_pin, 50)
myPWM.start(50)

# Define the PWM values required to play different tones on the buzzer
scale=[262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494, 524]

try:
    while True:
    	# Loop through each PWM value and play it on the buzzer
        a=0
        while a < 13:
            print a
            myPWM.ChangeFrequency(scale[a])
            time.sleep(0.5)
            a=a+1
finally:
	# Clean up the GPIO so that everything returns to normal
    GPIO.cleanup()
    
    # Exit the program
    sys.exit(0)
