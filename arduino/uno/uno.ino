#include <Wire.h>

void setup() {
  Wire.begin(0x04);
  Serial.begin(9600);
}

void loop() {
  int r = Wire.read();
  Serial.println(r);
}
