#include <Wire.h>
#include <Servo.h>
#include <time.h>

#define MotorA 10
#define MotorB 11

#define CAT 6

#define S0 22
#define S1 23
#define S2 24
#define S3 25
#define sensorOut 26

char start = '0';
int mi = 1520;
int ra = 200;
int red = 0, green = 0, blue = 0, color;
int min_red = 2000, min_green = 2000, min_blue = 2000;

Servo cat;

void setup() {
  Wire.begin(0x0c);
  Serial.begin(115200);
  Wire.onReceive(receiveEvent);

  cat.attach(CAT);
  cat.writeMicroseconds(mi); 

  pinMode(MotorA, OUTPUT);
  pinMode(MotorB, OUTPUT);
  analogWrite(MotorA, 130);
  analogWrite(MotorB, 0);

  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(sensorOut, INPUT);

  digitalWrite(S0, LOW);
  digitalWrite(S1, HIGH);
}

void loop() {
    color = turn();
    if (color == 1){
      cat.writeMicroseconds(mi+ra);
      delay(1500);
      cat.writeMicroseconds(mi);
    } else if (color == 2){
      cat.writeMicroseconds(mi-ra);
      delay(1500);
      cat.writeMicroseconds(mi);
    }

    min_red = 2000;
    min_blue = 2000;
    min_green = 2000;
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

    min_red = min(red, min_red);
    min_green = min(green, min_green);
    min_blue = min(blue, min_blue);
}

int turn() {
  get_color();
  if (min_red < 1000 && min_green < 1000 && min_blue < 1000) {
    for (int i = 0; i < 3; i++) {
      get_color();
    }

      if (min_red < 400 && min_green < 450 && min_blue < 150) return 1;
      else return 2;
  }

  return 0;
}

void receiveEvent() {
  if (Wire.available())
    start = Wire.read();
}
