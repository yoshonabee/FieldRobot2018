#include <Wire.h>
#include <Servo.h>

#define MotorA 10
#define MotorB 11
#define EncoderA 3
#define EncoderB 8

#define CAT 12

#define S0 22
#define S1 23
#define S2 24
#define S3 25
#define sensorOut 26

#define Kp 0.4
#define Kd 1

#define LOOPTIME 20

char start = '0';

int speed_req = 15;

int speed_act = 0;
int PWM_val = 50;
volatile long count = 0;
long countAnt = 0;
unsigned long lastMilli = 0;

int red = 0, green = 0, blue = 0, color;

Servo cat;

void setup() {
  Wire.begin(0x04);
  Serial.begin(115200);
  Wire.onReceive(receiveEvent);

  cat.attach(CAT, 700, 2500);
  cat.attach(90);
  
  pinMode(MotorA, OUTPUT);
  pinMode(MotorB, OUTPUT);
  pinMode(EncoderA, INPUT_PULLUP);
  pinMode(EncoderB, INPUT_PULLUP);
  attachInterrupt(1, rencoder, FALLING);

  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(sensorOut, INPUT);

  digitalWrite(S0, HIGH);
  digitalWrite(S1, LOW);
}

void loop() {
  if (start == '1') {
    analogWrite(MotorA, 100);
    analogWrite(MotorB, 0);
    if((millis()-lastMilli) >= LOOPTIME) {
        // lastMilli = millis();
        // getMotorData();
        // PWM_val = updatePid();
    
        // analogWrite(MotorA, PWM_val);
        // digitalWrite(MotorB, LOW);
  
        // color = get_color();
        // if (color == 1) {
        //   cat.write(120);
        //   delay(2000);
        // } else if (color == 2) {
        //   cat.write(60);
        //   delay(2000);
        // }
        
        // cat.write(90);
    }
  }
}

int get_color() {
  digitalWrite(S2,LOW);
  digitalWrite(S3,LOW);
  red = pulseIn(sensorOut, LOW);
  Serial.print("R= ");
  Serial.print(red);
  Serial.print("  ");
  delay(10);

  digitalWrite(S2,HIGH);
  digitalWrite(S3,HIGH);
  green = pulseIn(sensorOut, LOW);
  Serial.print("G= ");
  Serial.print(green);
  Serial.print("  ");
  delay(10);

  digitalWrite(S2,LOW);
  digitalWrite(S3,HIGH);
  blue = pulseIn(sensorOut, LOW);
  Serial.print("B= ");
  Serial.print(blue);
  Serial.println("  ");
  delay(10);

  if (red < 45 && green < 45 && blue < 45) return 1;
  else if (red < 55 && green < 55 && blue < 55) return 2;
  else return 0;
}

void getMotorData() {
  speed_act = ((count - countAnt) * (60 * (1000 / LOOPTIME))) / (14 * 27);
  countAnt = count;
}

int updatePid() {
  float pidTerm = 0;
  int error = 0;
  static int last_error = 0;
  error = abs(speed_req) - abs(speed_act);
  pidTerm = (Kp * error) + (Kd * (error - last_error));
  last_error = error;

  return constrain(PWM_val + int(pidTerm), 0, 255);
}

void rencoder() {
  if (digitalRead(EncoderB) == HIGH) count++;
  else count--;
}

void receiveEvent() {
  if (Wire.available())
    start = Wire.read();
}