/* Sweep
  by BARRAGAN <http://barraganstudio.com>
  This example code is in the public domain.
  modified 8 Nov 2013
  by Scott Fitzgerald
  http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo penZer;
Servo penOne;
Servo penTwo;
Servo penThr;
Servo penFou;
Servo penFiv;
Servo penSix;
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
int maxPos = 115;
int minPos = 30;


void setup() {
  pinMode(0, INPUT);
  pinMode(13, INPUT);
  pinMode(12, INPUT);
  pinMode(11, INPUT);
  pinMode(10, INPUT);
  pinMode(9, INPUT);
  pinMode(8, INPUT);
  penZer.attach(1);
  penOne.attach(2);  // attaches the servo on pin 9 to the servo object
  penTwo.attach(3);
  penThr.attach(4);
  penFou.attach(5);
  penFiv.attach(6);
  penSix.attach(7);
}

void loop()
{

  if (digitalRead(13) == LOW) {
    penZer.write(maxPos);
  }
  else

    penZer.write(minPos);

  if (digitalRead(13) == LOW) {
    penOne.write(maxPos);
  }
  else

    penOne.write(minPos);

  if (digitalRead(12) == LOW) {
    penTwo.write(maxPos);
  }
  else

    penTwo.write(minPos);

  if (digitalRead(11) == LOW) {
    penThr.write(maxPos);
  }
  else

    penThr.write(minPos);

  if (digitalRead(10) == LOW) {
    penFou.write(maxPos);
  }
  else

    penFou.write(minPos);

  if (digitalRead(9) == LOW) {
    penFiv.write(maxPos);
  }
  else

    penFiv.write(minPos);

  if (digitalRead(8) == LOW) {
    penSix.write(maxPos);
  }
  else

    penSix.write(minPos);
}
