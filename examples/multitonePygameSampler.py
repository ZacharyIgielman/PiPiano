#!/usr/bin/python
# multitonePygameSampler.py
# this enables you to press the buttoins on PiPiano like a piano, and will play the sounds out of the Pi's audio output like a proper keyboard
# Author : Zachary Igielman

# to run:
# sudo python multitonePygameSampler.py

# to change volume:
# amizer cset numid=1 -- 80%

# to change audio outout for Pi (audio jack/HDMI)
# amizer cset numid=3 0 (for auto-detect)
# amizer cset numid=3 1 (for analog)
# amizer cset numid=3 2 (for HDMI)