#include <Wire.h>
int state = 0;

void setup() {
  pinMode(13, OUTPUT);
  Wire.begin(0x04);
  Serial.begin(115200);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
}

void loop() {
  delay(100);
}

int get_ball_state() {
  
}

void receiveEvent(int tmp) {
  while (Wire.available()) {
    state += 1;
    int r = Wire.read();
    digitalWrite(13, state % 2);
    Wire.write("1");
  }
}

void requestEvent(int tmp) {
  int have_ball = get_ball_state();
  Wire.write(have_ball);

  if (have_ball)
    eat_ball();
}

