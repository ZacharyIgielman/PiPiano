# PiPiano
## Welcome to the PiPiano documentation.
Here you will find instructions on how to assemble your PiPiano and then program it using both Python and C.

### Assembly guide
Please visit [this page](assembling.md) to see an assembly guide.
This guide teaches you not only how to solder but how to put together your PiPiano kit.

### Software set-up
You will need to set-up your Pi correctly to be able to use the PiPiano. Follow
[these instructions](softwareSetup.md) first.

### Getting the example code
In order to use the examples, you will need to use 'git' on your Pi to download the code.
This is a simple procedure. First of all, open up a command line terminal and type in the following:

```
cd ~
git clone https://github.com/ZacharyIgielman/PiPiano
```

This will take around 5 minutes, and will download all the code to your home directory.
To access the code, you will need to type

```
cd PiPiano
cd examples
```

### Exploring the example code
The following examples are provided in both Python and C. If you do not have much experience
programming, we recommend starting with Python as it is slightly easier to understand.

* [button.py](examples/button.py) / [button.c](examples/button.c) - a script that detects what buttons have been pressed on your PiPiano
* [buzzer.py](examples/buzzer.py) / [buzzer.c](examples/buzzer.c) - a script that plays sounds through your PiPiano's buzzer
* [trafficLight.py](examples/trafficLight.py) / [trafficLight.c](examples/trafficLight.c) - a script that displays a United Kingdom traffic light sequence using the LEDs on the PiPiano 
* [piano.py](examples/piano.py) / [piano.c](examples/piano.c) - a script that detects button presses and plays the appropriate sound through the buzzer

The following additional Python examples are provided:

* [multitonePygameSampler.py](examples/multitonePygameSampler.py) - a script which detects button presses and uses Pygame to play the appropriate sound file through the Pi's headphone socket
* [genSonicPi.py](examples/genSonicPi.py) - a script which detects button presses and creates a text file containing instructions for [Sonic Pi](http://sonic-pi.net/).

You can explore all of the code files using your favourite editor. First of all, change
into the examples folder by typing:

```
cd examples
```

You can then open the code files in your editor. I recommend using nano which is used by
typing:

```
nano nameoffile
```

For example:

```
nano piano.py
```

Each example file contains comments which explains what it does. Comments in any of the
Python files start with a '#' symbol. In C files, the comments start with '//'.


### Running the example code
#### Python
In order to run the code in Python, you need to use 'sudo' (which allows access to the
GPIO pins). So, for example you would type:

```
sudo python piano.py
```

#### C
In order to run C code, you first of all need to compile it. Each code file contains
instructions on how to do this.
