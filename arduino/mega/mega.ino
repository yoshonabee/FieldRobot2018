#include <Wire.h>
char mode;
String spd_str;
float spd;

void setup() {
  pinMode(13, OUTPUT);
  Wire.begin(0x08);
  Serial.begin(115200);
  Wire.onReceive(receiveEvent);
}

void loop() {
  delay(10);
}

void receiveEvent(int ptr) {
  mode = Wire.read();
  Serial.print("mode:");
  Serial.println(mode);

  spd_str = "";
  while (Wire.available()) {
    char r = Wire.read();
    spd_str += r;
  }

  spd = spd_str.toFloat()
  Serial.print("speed:");
  Serial.println(spd);
}
