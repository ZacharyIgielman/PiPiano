# Software set-up
In order to get all those lovely button inputs, the PiPiano uses a chip which itself uses
the I2C protocol. Most of the time, you won't need to worry about I2C but you do need 
to set-up your Pi properly before you can use the PiPiano.

## Enable I2C
You need to enable I2C in order for the chip on the PiPiano to work. I2C is a 'protocol'
that the chip uses to provide more 'ports' to communicate with. Do the following on the
command line of your Pi:

* `sudo nano /etc/modules`
* Add the two following lines:
	* `i2c-bcm2708`
	* `i2c-dev`
* Press ctrl-X and then press Y and return to save.
* `sudo nano /etc/modprobe.d/raspi-blacklist.conf`
* Add a # character to the beginning of two lines so that they read:
	* `#blacklist spi-bcm2708`
	* `#blacklist i2c-bcm2708`
* to get i2c working on the latest Raspbian if it does not work:
	* `sudo nano /boot/config.txt`
	* Add this line:
		* `dtparam=i2c_arm=on`
	* Press ctrl-X and then press Y and return to save.
* Press ctrl-X and then press Y and return to save.
* `sudo adduser pi i2c`
* Do `sudo reboot`

Once booted back up, make sure you are connected to the internet. Then do the following from
the command line:

* `sudo apt-get update`
* (This takes between 1-2 minutes)
* `sudo apt-get install python-smbus i2c-tools`
* (This installs a 'toolset' to communicate with I2C from Python and will take about a minute)
* Do `sudo reboot` again

Once booted back up, login and do the following:

* If you're using a more recent (Rev 2) Pi, type: `sudo i2cdetect -y 1`
* If you're using a early (Rev 1) Pi, type: `sudo i2cdetect -y 0`
* This will print a grid of numbers. Hopefully, the 20/0 cell is showing '20'.

## If you're going to be programming in C...
If you want to use the C programming language to program the PiPiano, you
will need to install something called "WiringPi". Here's how to do it from the command line:

* `cd ~`
* `git clone git://git.drogon.net/wiringPi`
* `cd wiringPi`
* `git pull origin`
* `./build`
* This will take some time to build
* Type in `gpio -v` - this should tell you what version of wiringPi you've now correctly installed

C programs need to be "compiled" (i.e. turned from raw C code into something you can
actually run). Instructions for compiling each of the examples is included in the .c file.
Please note that they do not all compile the same way!
