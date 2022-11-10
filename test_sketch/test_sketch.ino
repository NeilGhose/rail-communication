void setup() {
  Serial.begin(115200);
}
void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\t');
    Serial.print("You sent me: \n");
    Serial.println(data);
  }
}