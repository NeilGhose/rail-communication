void setup() {
  Serial.begin(115200);
}

char data[1400];

void loop() {
  if (Serial.available() > 0) {
    int n = Serial.readBytes(data, 1024);
    Serial.print(data);
  }
}