#include <Wire.h>
int state = 0;

void setup() {
  pinMode(13, OUTPUT);
  Wire.begin(0x08);
  Serial.begin(115200);
  Wire.onReceive(receiveEvent);
}

void loop() {
  delay(100);
}

void receiveEvent(int how) {
  while (Wire.available()) {
    state += 1;
    int r = Wire.read();
    digitalWrite(13, state % 2);
  }
}
