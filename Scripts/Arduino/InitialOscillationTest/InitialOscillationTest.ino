/*-----------------
 Magic Marker Mixer
 Github: https://github.com/m3bolt/MarkerMixer
 Designers: https://github.com/kackle1998 , https://github.com/m3bolt/
 WIP
 Initial Arduino proof of concept for 1in-1out multicolor 3D Printing
-------------------*/
#include <Servo.h>

Servo servo1; Servo servo2;  Servo servo3;

int pos1 = 9; int minServo1 = 9; int maxServo1 = 41; //Current Pos, min Pos, max Pos
int pos2 = 9; int minServo2 = 9; int maxServo2 = 41;
int pos3 = 9; int minServo3 = 9; int maxServo3 = 41;

int servo1Pin=1; int servo2Pin=2; int servo3Pin=3; //Change these to whatever pin numbers you're using

int stepTime = 10;            // milliseconds
int minutesBetween = 4; // minutes

void setup() {
  servo1.attach(servo1Pin);
  servo2.attach(servo2Pin);
  servo3.attach(servo3Pin);
  servo1.write(minServo1); servo2.write(minServo2); servo3.write(minServo3);
}

void loop() {
  engageAll();
  delay(minutesBetween*60*1000); 
  disengageAll();
  engageServo1();
  delay(minutesBetween*60*1000);
  engageServo2();
  delay(minutesBetween*60*1000);
  engageServo3();
  delay(minutesBetween*60*1000);
}


void engageServo1(){
   for (pos1 = minServo1; pos1 <= maxServo1; pos1 += 1) {
    servo1.write(pos1);           
    delay(stepTime);                   
  }
}

void disengageServo1(){
   for (pos1 = maxServo1; pos1 >= minServo1; pos1 -= 1) { 
    servo1.write(pos1);             
    delay(stepTime);                     
  }
}

void engageServo2(){
   for (pos2 = minServo2; pos2 <= maxServo2; pos2 += 1) {
    servo2.write(pos2);           
    delay(stepTime);                   
  }
}

void disengageServo2(){
   for (pos2 = maxServo2; pos2 >= minServo2; pos1 -= 1) { 
    servo2.write(pos2);             
    delay(stepTime);                     
  }
}

void engageServo3(){
   for (pos3 = minServo3; pos3 <= maxServo3; pos3 += 1) {
    servo3.write(pos3);           
    delay(stepTime);                   
  }
}

void disengageServo3(){
   for (pos3 = maxServo3; pos3 >= minServo3; pos3 -= 1) { 
    servo3.write(pos3);             
    delay(stepTime);                     
  }
}

void engageAll(){
  engageServo1();
  engageServo2();
  engageServo3();
}

void disengageAll(){
  disengageServo1();
  disengageServo2();
  disengageServo3();
}
