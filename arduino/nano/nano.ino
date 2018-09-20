#include <Wire.h>

#define MotorA 10
#define MotorB 11
#define EncoderA 3
#define EncoderB 8

#define Kp 0.4
#define Kd 1

#define LOOPTIME 50

volatile int speed_req = 0;

int speed_act = 0;
int PWM_val = 80;
volatile long count = 0;
long countAnt = 0;
unsigned long lastMilli = 0;

char direct;
char last_direct;
String spd_str;

void setup() {
  Wire.begin(0x08);
  Serial.begin(115200);
  Wire.onReceive(receiveEvent);

  pinMode(MotorA, OUTPUT);
  pinMode(MotorB, OUTPUT);
  pinMode(EncoderA, INPUT_PULLUP);
  pinMode(EncoderB, INPUT_PULLUP);
  attachInterrupt(1, rencoder, FALLING);
}

void loop() {
  if (direct != last_direct) {
    count = 0;
    countAnt = 0;
    lastMilli = millis();
    last_direct = direct;
  }
  
  if((millis()-lastMilli) >= LOOPTIME) {
      lastMilli = millis();
      getMotorData();
      PWM_val = updatePid();

      if (speed_req == 0) {
        digitalWrite(MotorA, LOW);
        digitalWrite(MotorB, LOW);
      } else if (direct == 'F') {
        analogWrite(MotorA, PWM_val);
        digitalWrite(MotorB, LOW);
      } else if (direct == 'B') {
        digitalWrite(MotorA, LOW);
        analogWrite(MotorB, PWM_val);
      }

//      Serial.print("   PWM_val:");
//      Serial.println(PWM_val);
  }
}

void receiveEvent(int ptr) {
  if (Wire.available()) {
    direct = Wire.read();
//    Serial.print("direct:");
//    Serial.println(direct);
  }

  spd_str = "";
  while (Wire.available()) {
    spd_str += (char)Wire.read();
  }

  speed_req = spd_str.toInt();
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

//  Serial.print("speed_req:");
//  Serial.print(speed_req);
//  Serial.print("   speed_act:");
//  Serial.print(speed_act);
//  Serial.print("   error:");
//  Serial.print(error);
//  Serial.print("   pidTerm:");
//  Serial.print(pidTerm);

  return constrain(PWM_val + int(pidTerm), 0, 255);
}

void rencoder() {
  if (digitalRead(EncoderB) == HIGH) count++;
  else count--;
}
