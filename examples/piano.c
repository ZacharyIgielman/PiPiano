//piano.c
//turn your PiPiano into a piano, each button plays the corresponding piano note frequency on the piezo buzzer of PiPiano
//Author : Zachary Igielman

//to run:
//gcc -Wall -o piano piano.c -lwiringPi -lpthread
//sudo ./piano

//Import all the libraries you need to read in button inputs and output to the buzzer
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <pthread.h>
#include <wiringPi.h>
#include <softTone.h>
#include <mcp23017.h>

//Create a function to control the LEDs
void light(int a, int b, int c)
{
    digitalWrite(113,a);
    digitalWrite(114,b);
    digitalWrite(115,c);
}

// Create a function to help you keep time by lighting up the LEDs in a pattern with
// a steady gap between the changes
void *metronome()
{
    for (;;) {
        light(1,0,0);
        delay(500);
        light(0,1,0);
        delay(500);
        light(0,0,1);
        delay(500);
    }
    return NULL;
}

//Define the GPIO pin that is used for the buzzer
#define	PIN	11

//Specify an array of PWM values so that we can play the correct tones depending on the button press
int scale [13] = {262,294,330,349,392,440,494,524,277,311,370,415,466} ;

//Initialise an array which holds the values of all the buttons
int last[13]={0,0,0,0,0,0,0,0,0,0,0,0,0};

int main ()
{
    int i;
    //Setup the library we use to control GPIO
    wiringPiSetup();
    mcp23017Setup(100, 0x20);
    //Set-up the buzzer pin as a soft tone so we can play frequencies on it
    softToneCreate (PIN) ;
    //Set-up all the buttons as 'pull-ups' and inputs
    for (i = 0 ; i < 13 ; ++i) {
        pinMode (100+i, INPUT);
        pullUpDnControl (100+i, PUD_UP);
    }
    //Setup the LEDs as outputs
    for (i = 113 ; i < 116 ; i++)
        pinMode(i, OUTPUT) ;
    //Start the metronome up in a 'thread' which means it will continue to run while
    //you are reading in button presses
    pthread_t metronome_thread;
    pthread_create(&metronome_thread,NULL,metronome,NULL);
    //Read in button inputs and keep track of what the last set of button presses was
    //Change the frequency of the buzzer to whatever buttons are being pressed
    for (;;) {
        int x=0;
        for (i = 0 ; i < 13 ; ++i) {
            if ((!digitalRead(100+i)) && (last[i]!=digitalRead(100+i))) {
                softToneWrite (PIN, scale [i]) ;
                printf("%d\n",i);
            }
            if (!digitalRead(100+i)) {
                x=x+1;
            }
            last[i]=digitalRead(100+i);
        }
        if (x==0) {
            softToneWrite(PIN,0);
        }
    }
    return 0;
}
