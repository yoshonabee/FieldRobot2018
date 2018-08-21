#include <Wire.h>

void setup() {
  Wire.begin(0x08);
  Serial.begin(9600);
}

void loop() {
  int r = Wire.read();
  Serial.println(r);
}
