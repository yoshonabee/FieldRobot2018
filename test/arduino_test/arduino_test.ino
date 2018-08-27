#include <Wire.h>
int mode;
String spd_str;
float spd;

void setup() {
  pinMode(13, OUTPUT);
  Wire.begin(0x08);
  Serial.begin(115200);
  Wire.onReceive(receiveEvent);
}

void loop() {
//  delay(10);
}

void receiveEvent(int ptr) {
  if (Wire.available()) {
    mode = Wire.read();
    Serial.print("mode:");
    Serial.println(mode);
  }
  
  spd_str = "";
  while (Wire.available()) {
    spd_str += (char)Wire.read();
  }
  Serial.println(spd_str);
}
