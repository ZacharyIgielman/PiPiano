# PiPiano
## Welcome to the PiPiano documentation.
Here you will find instructions on how to assemble your PiPiano and then program it using both Python and C.

### Assembly guide
Please visit [this page](assembling.md) to see an assembly guide.
This guide teaches you not only how to solder but how to put together your PiPiano kit.

### Example code
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

The following examples are provided in both Python and C. If you do not have much experience
programming, we recommend starting with Python as it is a slightly easier to understand
language. Tutorials for each file are also available and are covered in the next section.

* [button.py](examples/button.py) / button.c - a script that detects what buttons have been pressed on your PiPiano
* buzzer.py / buzzer.c - a script that plays sounds through your PiPiano's buzzer
* piano.py / piano.c - a script that detects button presses and plays the appropriate sound through the buzzer
* trafficLight.py / trafficLight.c - a script that displays a United Kingdom traffic light sequence using the LEDs on the PiPiano 

The following additional example is provided:

* multitonePygameSampler.py - a script which detects button presses and plays the appropriate .wav file through the Pi's headphone socket

### Tutorials

