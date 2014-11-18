//button.c
//detects button presses and prints which button is pressed
//Author : Zachary Igielman

//to run:
//gcc -Wall -o button button.c -lwiringPi
//sudo ./button

//Import the libraries we need to use to access GPIO and connect to the port expander chip
#include <stdio.h>
#include <wiringPi.h>
#include <mcp23017.h>

int main (void)
{
    int i;
    //Setup the library we use to control GPIO
    wiringPiSetup();
    //Setup communication to our port expander chip
    mcp23017Setup(100, 0x20);
    printf ("PiPiano-buttons!\n") ;
    //This bit of code loops through all the buttons, sets 'pull ups' on them and makes them inputs
    for (i = 0 ; i < 13 ; ++i) {
        pinMode (100+i, INPUT);
        pullUpDnControl (100+i, PUD_UP);
    }
    for (;;) {
        //Print a new line followed by 'Buttons pressed: '
        printf("\nButtons pressed: ");
        //Read each of the 13 buttons on the PiPiano and if any are pressed print out the number of the button 
        for (i = 0 ; i < 13 ; ++i) {
            if (!digitalRead(100+i)) {
                printf("%d ",i);
            }
        }
    }
    return 0;
}
