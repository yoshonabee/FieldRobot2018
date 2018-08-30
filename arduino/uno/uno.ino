#include <Wire.h>
#include <Servo.h>

#define trig 6
#define echo 7
#define flap 3
#define cat 5
#define S0 8
#define S1 9
#define S2 10
#define S3 11
#define sensorOut 12

int have_egg = 0;
int red = 0, green = 0, blue = 0, color = 0;

Servo servo_flap;
Servo servo_cat;

void setup() {
//  Wire.begin(0x04);
  Serial.begin(115200);
//  Wire.onRequest(requestEvent);

  servo_flap.attach(flap, 700, 2500);
  servo_cat.attach(cat, 700, 2500);
  servo_flap.write(0);
  servo_cat.write(90);

  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(sensorOut, INPUT);

  digitalWrite(S0,HIGH);
  digitalWrite(S1,LOW);
}



int get_egg_state() {
  float duration, distance;
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  duration = pulseIn (echo, HIGH);
  distance = (duration/2)/29;
  if (distance < 5)
    return 1;
  return 0;
}

void get_color() {
  digitalWrite(S2,LOW);
  digitalWrite(S3,LOW);
  red = pulseIn(sensorOut, LOW);
  Serial.print("R= ");
  Serial.print(red);
  Serial.print("  ");
  delay(100);

  digitalWrite(S2,HIGH);
  digitalWrite(S3,HIGH);
  green = pulseIn(sensorOut, LOW);
  Serial.print("G= ");
  Serial.print(green);
  Serial.print("  ");
  delay(100);

  digitalWrite(S2,LOW);
  digitalWrite(S3,HIGH);
  blue = pulseIn(sensorOut, LOW);
  Serial.print("B= ");
  Serial.print(blue);
  Serial.println("  ");
  delay(100);
}

void whatColor() {
  if (red < 40 && green < 40 && blue < 40)
    color = 1;
  else if (red < 50 && green < 50 && blue < 50)
    color = 2;
  else
    color = 0;
}

void eat_egg() {
  servo_flap.write(180);
  color = 0;
  
  do {
    get_color();
  } while (!color);
  servo_flap.write(0);

  if (color == 1)
    servo_cat.write(120);
  else if (color == 2)
    servo_cat.write(60);
  delay(2000);
  servo_cat.write(90);
}

void requestEvent() {
  if (have_egg) {
    Wire.write('E');
    eat_egg();
  } else {
    Wire.write('N');
    have_egg = get_egg_state();
  }
}
void loop() {
  get_color();
  delay(100);
}
