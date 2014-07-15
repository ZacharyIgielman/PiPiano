//button.c
//detects button presses and prints which button is pressed
//Author : Zachary Igielman

#include <stdio.h>
#include <wiringPi.h>
#include <mcp23017.h>

int main (void)
{
    int i;
    
    wiringPiSetup();
    mcp23017Setup(100, 0x20);
    
    printf ("PiPiano-buttons!\n") ;
    
    for (i = 0 ; i < 13 ; ++i)
        pinMode (100+i, INPUT);
        pullUpDnControl (100+i, PUD_UP);
    }
    for (;;)
    {
        printf("\nButtons pressed: ")
        for (i = 0 ; i < 13 ; ++i)
            if (digitalRead(100+i)) {
                printf("%d ",i);
            }
        }
    }
    return 0;
}