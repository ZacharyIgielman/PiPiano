//piano.c
//turn your PiPiano into a piano, each button plays the corresponding piano note frequency on the piezo buzzer of PiPiano
//Author : Zachary Igielman

//to run:
//gcc -Wall -o piano piano.c -lwiringPi -lpthread
//sudo ./piano

#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <pthread.h>

#include <wiringPi.h>
#include <softTone.h>
#include <mcp23017.h>

void light(int a, int b, int c)
{
    digitalWrite(113,a);
    digitalWrite(114,b);
    digitalWrite(115,c);
}

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

#define	PIN	14

int scale [13] = {262,294,330,349,392,440,494,524,277,311,370,415,466} ;
int last[13]={0,0,0,0,0,0,0,0,0,0,0,0,0};

int main ()
{
    int i;
    wiringPiSetup();
    mcp23017Setup(100, 0x20);
    softToneCreate (PIN) ;
    for (i = 0 ; i < 13 ; ++i) {
        pinMode (100+i, INPUT);
        pullUpDnControl (100+i, PUD_UP);
    }
    for (i = 113 ; i < 116 ; i++)
        pinMode(i, OUTPUT) ;
    pthread_t metronome_thread;
    pthread_create(&metronome_thread,NULL,metronome,NULL);
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
