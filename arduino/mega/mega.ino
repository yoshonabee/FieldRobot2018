#include <Wire.h>

void setup() {
  Wire.begin(0x08);
  Serial.begin(115200);
  Wire.onReceive(receiveEvent)
}

void loop() {
  delay(100);
}

void receiveEvent() {
  while (Wire.available()) {
    char r = Wire.read();
    Serial.println(r);
  }
}
