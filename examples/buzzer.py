#!/usr/bin/python
# buzzer.py
# plays a scale on the buzzer
# Author : Zachary Igielman

import RPi.GPIO as GPIO, time

buzzer_pin=23

GPIO.setmode(GPIO.BOARD)

GPIO.setup(buzzer_pin, GPIO.OUT)
myPWM=GPIO.PWM(buzzer_pin, 
