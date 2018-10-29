#include <Wire.h>
#include <Servo.h>

#define MotorA 10
#define MotorB 11

#define CAT 6

#define S0 22
#define S1 23
#define S2 24
#define S3 25
#define sensorOut 26

char start = '0';

int red = 0, green = 0, blue = 0, color;
int min_red = 255, min_green = 255, min_blue = 255;

Servo cat;

void setup() {
//  Wire.begin(0x0c);
  Serial.begin(115200);
//  Wire.onReceive(receiveEvent);

  cat.attach(CAT, 700, 2400);
  cat.write(95);
  
//  pinMode(MotorA, OUTPUT);
//  pinMode(MotorB, OUTPUT);
//
//  pinMode(S0, OUTPUT);
//  pinMode(S1, OUTPUT);
//  pinMode(S2, OUTPUT);
//  pinMode(S3, OUTPUT);
//  pinMode(sensorOut, INPUT);
//
//  digitalWrite(S0, HIGH);
//  digitalWrite(S1, LOW);
}

void loop() {
//  cat.write(95);
//  Serial.println(95);
//  delay(1000);
//  cat.write(85);
//  Serial.println(85);
//  delay(1000);
//  cat.write(95);
//  Serial.println(95);
//  delay(1000);
//  cat.write(103);
//  Serial.println(103);
//  delay(1000);
//  Serial.println("cool");
//  for (int i = 0; i < 10000000; i++) {
//    if (start == '0') {
//       analogWrite(MotorA, 120);
//       analogWrite(MotorB, 0);
//      
//      color = get_color();
//      
//      // if (color == 1) {
//      //   cat.write(120);
//      //   delay(2000);
//      // } else if (color == 2) {
//      //   cat.write(60);
//      //   delay(2000);
//      // }
//      
//      // cat.write(90);
//    }
////  }
//  min_red = 255;
//  min_blue = 255;
//  min_green = 255;
}

int get_color() {
  digitalWrite(S2,LOW);
  digitalWrite(S3,LOW);
  red = pulseIn(sensorOut, LOW);

  min_red = min(red, min_red);
 
  Serial.print("R= ");
  Serial.print(min_red);
  Serial.print("  ");
  delay(10);

  digitalWrite(S2,HIGH);
  digitalWrite(S3,HIGH);
  green = pulseIn(sensorOut, LOW);

  min_green = min(green, min_green);
  
  Serial.print("G= ");
  Serial.print(min_green);
  Serial.print("  ");
  delay(10);

  digitalWrite(S2,LOW);
  digitalWrite(S3,HIGH);
  blue = pulseIn(sensorOut, LOW);

  min_blue = min(blue, min_blue);
  
  Serial.print("B= ");
  Serial.print(min_blue);
  Serial.println("  ");
  delay(10);

  if (red < 45 && green < 45 && blue < 45) return 1;
  else if (red < 55 && green < 55 && blue < 55) return 2;
  else return 0;
}

void receiveEvent() {
  if (Wire.available())
    start = Wire.read();
}
