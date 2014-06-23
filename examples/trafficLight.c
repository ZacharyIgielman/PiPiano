//trafficLight.c
//loops through red, yellow, green like a traffic light
//Author : Zachary Igielman

#include <stdio.h>
#include <wiringPi.h>
#include <mcp23017.h>

int main (void)
{
  int i;

  wiringPiSetup() ;
  mcp23017Setup(65, 0x20) ;

  printf ("Raspberry Pi - MCP23017 Test\n") ;

  for (i = 78 ; i < 81 ; i++)
    pinMode(i, OUTPUT) ;

  for (;;)
  {
    digitalWrite(80,1);
    digitalWrite(79,0);
    digitalWrite(78,0);
    delay(3000);
    digitalWrite(80,1);
    digitalWrite(79,1);
    digitalWrite(78,0);
    delay(1000);
    digitalWrite(80,0);
    digitalWrite(79,1);
    digitalWrite(78,1);
    delay(5000);
    digitalWrite(80,0);
    digitalWrite(79,1);
    digitalWrite(78,0);
    delay(1000);
  }
  return 0 ;
}
