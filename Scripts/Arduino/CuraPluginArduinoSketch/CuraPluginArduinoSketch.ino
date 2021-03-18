/*-----------------
 Magic Marker Mixer
 Github: https://github.com/m3bolt/MarkerMixer
 Designers:
 Code: https://github.com/kackle1998 
 Mech Design: https://github.com/m3bolt/ , https://github.com/kackle1998 
 WIP
 Initial Arduino+Cura proof of concept for 1in-1out multicolor 3D Printing
--------------------*/

#include <Servo.h>

Servo servo1; Servo servo2;  Servo servo3;
int pos1 = 30; int minServo1 = 30; int maxServo1 = 115; //Current Pos, min Pos, max Pos
int pos2 = 30; int minServo2 = 30; int maxServo2 = 115;
int pos3 = 30; int minServo3 = 30; int maxServo3 = 115;

int servo1Pin=1; int servo2Pin=2; int servo3Pin=3; //Change these to whatever pin numbers you're using
int inputServo1 = 4; int inputServo2 = 5; int inputServo3 = 6; //Same here

void setup() {
 servo1.attach(servo1Pin); pinMode(inputServo1, INPUT);
 servo2.attach(servo2Pin); pinMode(inputServo2, INPUT);
 servo3.attach(servo3Pin); pinMode(inputServo3, INPUT);
 servo1.write(minServo1); servo2.write(minServo2); servo3.write(minServo3);
}

void loop()
{
readServo1();
readServo2();
readServo3();
}

void readServo1(){
  if (digitalRead(inputServo1)==LOW)
    servo1.write(maxServo1);
  else
    servo1.write(minServo1);
}

void readServo2(){
  if (digitalRead(inputServo2)==LOW)
    servo2.write(maxServo2);
  else
    servo2.write(minServo2);
}

void readServo3(){
  if (digitalRead(inputServo3)==LOW)
    servo3.write(maxServo3);
  else
    servo3.write(minServo3);
}
