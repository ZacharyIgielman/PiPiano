# PiPiano
## Welcome to the PiPiano documentation.
Here you will find instructions on how to assemble your PiPiano and then program it using both Python and C.

### Assembly guide
Please visit [this page](assembling.md) to see an assembly guide.
This guide teaches you not only how to solder but how to put together your PiPiano kit.

### Getting the example code
In order to use the examples, you will need to use 'git' on your Pi to download the code.
This is a simple procedure. First of all, open up a command line terminal and type in the following:

```
cd ~
git clone https://github.com/ZacharyIgielman/PiPiano
```

This will download all the code to your home directory.
To access the code, you will need to type

```
cd PiPiano
cd examples
```

### Exploring the example code
The following examples are provided in both Python and C. If you do not have much experience
programming, we recommend starting with Python as it is a slightly easier to understand
language. Each example file contains comments which explains what it does.

* [button.py](examples/button.py) / [button.c](examples/button.c) - a script that detects what buttons have been pressed on your PiPiano
* [buzzer.py](examples/buzzer.py) / [buzzer.c](examples/buzzer.c) - a script that plays sounds through your PiPiano's buzzer
* [buzzer.py](examples/piano.py) / [piano.c](examples/piano.c) - a script that detects button presses and plays the appropriate sound through the buzzer
* [trafficLight.py](examples/trafficLight.py) / [trafficLight.c](examples/trafficLight.c) - a script that displays a United Kingdom traffic light sequence using the LEDs on the PiPiano 

The following additional Python example is provided:

* [multitonePygameSampler.py](examples/multitonePygameSampler.py) - a script which detects button presses and uses Pygame to play the appropriate .wav file through the Pi's headphone socket

