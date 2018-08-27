#include <Wire.h>
int mode;
String spd_str;
float spd;
int count = 0;

void setup() {
  pinMode(13, OUTPUT);
  Wire.begin(0x08);
  Serial.begin(115200);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
}

void loop() {
  delay(10);
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
  
  spd = spd_str.toFloat();
  Serial.print("speed:");
  Serial.println(spd);
}

void requestEvent() {
  count++;
  if (count % 10 == 0)
    Wire.write('E');
  else
    Wire.write('N');
}

