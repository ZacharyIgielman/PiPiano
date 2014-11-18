//buzzer.c
//plays a scale on the buzzer
//Author : Zachary Igielman

//to run:
//gcc -Wall -o buzzer buzzer.c -lwiringPi
//sudo ./buzzer

//Import the libraries you will be using
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <wiringPi.h>
#include <softTone.h>

//Define the pin that the buzzer is on
#define	PIN	11

//Define the PWM values required to play different tones on the buzzer
int scale [13] = {262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494, 524} ;

int main ()
{
    int i ;
    //Setup the library we are using to control GPIOs
    wiringPiSetup () ;
    //Set-up the buzzer as a PWM. This allows us to play different tones on one GPIO pin
    softToneCreate (PIN) ;
    //Loop through each PWM value and play it on the buzzer
    for (;;)
    {
        for (i = 0 ; i < 13 ; ++i)
        {
            printf ("%3d\n", i) ;
            softToneWrite (PIN, scale [i]) ;
            delay (500) ;
        }
    }
}
