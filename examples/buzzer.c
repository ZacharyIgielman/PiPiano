//buzzer.c
//plays a scale on the buzzer
//Author : Zachary Igielman

#include <stdio.h>
#include <errno.h>
#include <string.h>

#include <wiringPi.h>
#include <softTone.h>

#define	PIN	14

int scale [13] = {262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494, 524} ;

int main ()
{
  int i ;

  wiringPiSetup () ;

  softToneCreate (PIN) ;

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
