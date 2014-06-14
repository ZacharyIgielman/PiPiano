#!/usr/bin/python
# buzzer.py
# plays a scale on the buzzer
# Author : Zachary Igielman

import RPi.GPIO as GPIO, time

buzzer_pin=23

GPIO.setmode(GPIO.BOARD)

GPIO.setup(buzzer_pin, GPIO.OUT)
myPWM=GPIO.PWM(buzzer_pin, 0)
myPWM.start(50)

scale=[262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494, 524]

while True:
  a=0
  while a < 13:
    myPWM.changeFrequency(scale[a])
    time.sleep(0.5)
    a=a+1
