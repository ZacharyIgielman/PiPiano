**In this tutorial, you will learn how to solder and assemble PiPiano**

# What is soldering?
Soldering is the process whereby two pieces of metal are joined together using another material
(the solder) to fill in the gaps between them. Soldering is *not* the same as welding - soldering
is used to form an electrical, rather than a physical, connection. 

## How to solder
The best way to show you how to solder is to get you to watch a video. Carrie Anne Philbin
has done an excellent video in her Geek Gurl Diaries series.

![Learn to Solder with Carrie Anne](https://lh4.googleusercontent.com/proxy/p2tTllwxErbkxCLyGOQbmaLiNrWtC7TQm5s5vKxWBBOHZoiu1P5yb50LC4sUWUH9Tnxg9aqWf6boo669VpfcnMIf4LA=w506-h285-n)

[Watch Carrie Anne's Learn to Solder video](http://www.youtube.com/watch?v=P5L4Gl6Q4Xo)

For a further look at soldering, check out [David Stillman's video](https://www.youtube.com/watch?v=f95i88OSWB4) which gives additional tips on making a good solder joint.

If you make any mistakes, you should [watch this slightly longer video](https://www.youtube.com/watch?v=QL86gO9mfT8) which shows how to correct them.

If you'd prefer to read how to do soldering rather than watch these videos, [check out this comic book called "Soldering is Easy"](http://mightyohm.com/blog/2011/04/soldering-is-easy-comic-book/).

*Thanks to Matt Hawkins at [Raspberry Pi Spy](http://www.raspberrypi-spy.co.uk/) for spotting these last few links.*

# Parts list
![Contents](https://lh5.googleusercontent.com/-_ZR2-0ZpTEU/VCCJg1BuDlI/AAAAAAAAQHk/-BBBe-tqOdI/w1280-h720-no/20140813_185400.jpg)

* Main circuit board
* Piezo buzzer
* GPIO header
* Chip socket
* MCP23017 port expander chip
* 13 x tactile buttons
* 1 red LED, 1 yellow LED, 1 green LED
* 1 capacitor
* 1 resistor network

![Main board](https://lh3.googleusercontent.com/-bAdWL0yfNns/VCCJg5jJIgI/AAAAAAAAQHk/lMhdz_zQQss/w1153-h865-no/20140813_185623.jpg)
*Main circuit board*

# Soldering the PiPiano
1. Start with the GPIO header. As it says, you place the black part under the board, push the pins through
and solder them from the top. Be very careful to avoid "shorting" the pins by soldering them together.
Use BluTack to hold the header in place and use either more BluTack to hold the whole thing in place
or a pair of "helping hands". Solder one corner and make sure the header is flat to the board. You
can always reposition it by heating the single pin up and pushing it from the other side.
![Underside with BluTack](https://lh4.googleusercontent.com/-koYtepWpF7k/VCCJgwUcirI/AAAAAAAAQHk/VuzyLg37YCw/w1153-h865-no/20140813_191449.jpg)
![Soldering - keep it neat](https://lh4.googleusercontent.com/-lDvi2aqn_gg/VCCJg8nZUrI/AAAAAAAAQHk/svcEvR8IGaU/w649-h865-no/20140813_202504.jpg)

1. Now do the buttons. Be careful when pushing them into place that the legs go through the holes. Do
the top row first. Again, use BluTack to keep the board still while you solder.
![Buttons - top side](https://lh6.googleusercontent.com/-EN9t35aTH9Q/VCCJg5jbKtI/AAAAAAAAQHk/2ujy-fGMJNg/w649-h865-no/20140813_202736.jpg)
![Buttons - bottom side](https://lh4.googleusercontent.com/-3wi4u59KuSE/VCCJgyojXXI/AAAAAAAAQHk/phWzZz8Mv5k/w649-h865-no/20140813_202747.jpg)

1. Now do the second row of buttons. Be extra careful when soldering that you don't "bridge" the connections
by dragging solder from one pin to another.
![Buttons - second row on bottom](https://lh5.googleusercontent.com/-r5CaWdp3-mw/VCCJgxVMssI/AAAAAAAAQHk/MuJbhtk4xcg/w649-h865-no/20140813_210302.jpg)

1. Next solder the chip socket on. Ensure the slot on the socket matches the slot on the silk screen.
Again, solder one corner first, then all the corners, ensuring it lies flat against the board. Be very
careful your soldering iron does not touch the main header and melt it!

1. Insert the LEDs into the board. #1 is red, #2 is yellow and #3 is green. The long (positive)
leg should be on the left side towards the chip socket. Bend the legs away from one another to
hold the LEDs in place. Again, be careful not to touch the header with the iron. Snip
the LED legs with a sidecutter or scissors.
![Bend the LED legs](https://lh6.googleusercontent.com/-dtLJv2iHG80/VCCJg6gH0EI/AAAAAAAAQHk/C98GnjWGUK4/w649-h865-no/20140813_211312.jpg)

1. Push the yellow resistor network into place and hold with BluTack. The writing on the resistor
network should face towards the LEDs. Make sure it stands up straight - the BluTack should help.
![Starting to take shape](https://lh5.googleusercontent.com/-g15WEuhdwGA/VCCJg4VW1GI/AAAAAAAAQHk/pDMlttDCBNE/w649-h865-no/20140813_211950.jpg)

1. Now solder the capacitor in place using, you guessed it, more BluTack. The stripe on the side is the
negative terminal and should match the hole on the board with the - symbol on it - it's the
bottom hole. Again, bend the legs away to hold it in place. Snip the legs once soldered.
1. Now carefully push the chip into the holder. Make sure the notch on the chip matches the notch on the holder
(to the right). Be gentle, but firm. If you need to bend the pins, do so by pressing them against your table,
making sure you apply equal pressure to all the pins. Do it a bit at a time - it's very difficult
to unbend them! The chip will be _upside down_.

![Push the chip in upside down](https://lh4.googleusercontent.com/-hTVWVmeFcqc/VCCJg2DZuFI/AAAAAAAAQHk/gJ6sa3FKBbU/w649-h865-no/20140813_213044.jpg)

1. Carefully solder the buzzer wires on. The red wire goes at the top. BluTack will help again. Snip the ends off.
![Soldering the buzzer wires](https://lh5.googleusercontent.com/-qqZi19K8Vz0/VCCJg9w2W9I/AAAAAAAAQHk/fjS_8sf8Kw0/w649-h865-no/20140813_213057.jpg)

![The PiPiano in place](https://lh5.googleusercontent.com/-v2NyAO6Ko6s/VCCJgzHh-hI/AAAAAAAAQHk/pvfpfymjbJY/w1153-h865-no/20140813_213503.jpg)

Next step: setting up software (softwareSetup.md)
