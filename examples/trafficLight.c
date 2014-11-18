//trafficLight.c
//loops through red, yellow, green like a traffic light
//Author : Zachary Igielman

//to run:
//gcc -Wall -o trafficLight trafficLight.c -lwiringPi
//sudo ./trafficLight

//Import the libraries necessary for changing the state of the LEDs
#include <stdio.h>
#include <wiringPi.h>
#include <mcp23017.h>

//Create a function that turns the LEDs on/off depending on what values are sent to it when the function is called
void light(int a, int b, int c)
{
    digitalWrite(113,a);
    digitalWrite(114,b);
    digitalWrite(115,c);
}

int main (void)
{
    int i;
    //Setup the library for controlling GPIOs
    wiringPiSetup() ;
    //Setup communication to the PiPiano chip
    mcp23017Setup(100, 0x20) ;
    //Setup the LED pins as outputs
    for (i = 113 ; i < 116 ; i++)
        pinMode(i, OUTPUT) ;
    //Turn the LEDs on/off in the 'traffic lights sequence' 
    for (;;)
    {
        light(1,0,0);
        delay(3000);
        light(1,1,0);
        delay(1000);
        light(0,0,1);
        delay(5000);
        light(0,1,0);
        delay(1000);
    }
    return 0 ;
}
