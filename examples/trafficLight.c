//trafficLight.c
//loops through red, yellow, green like a traffic light
//Author : Zachary Igielman

//to run:
//gcc -Wall -o trafficLight trafficLight.c -lwiringPi
//sudo ./trafficLight

#include <stdio.h>
#include <wiringPi.h>
#include <mcp23017.h>

void light(int a, int b, int c)
{
    digitalWrite(113,a);
    digitalWrite(114,b);
    digitalWrite(115,c);
}

int main (void)
{
    int i;

    wiringPiSetup() ;
    mcp23017Setup(100, 0x20) ;

    printf ("Raspberry Pi - MCP23017 Test\n") ;

    for (i = 113 ; i < 116 ; i++)
        pinMode(i, OUTPUT) ;

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
