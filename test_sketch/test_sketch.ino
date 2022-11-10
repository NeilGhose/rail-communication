void setup() {
  Serial.begin(115200);
}

char data[1400];

void loop() {
  if (Serial.available() > 0) {
    int n = Serial.readBytes(data, 1024);
    Serial.print("You sent me ");
    Serial.print(n);
    Serial.println(" bytes\n");
    Serial.println(data);
  }
}