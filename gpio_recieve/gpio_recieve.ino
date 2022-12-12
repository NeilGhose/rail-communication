byte character = 0;
void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(6, INPUT);
  pinMode(7, OUTPUT);
}

void loop() {
  digitalWrite(7, digitalRead(6));
  Serial.println(digitalRead(6));
  digitalWrite(LED_BUILTIN, LOW);
  if (Serial.available()) {
    digitalWrite(LED_BUILTIN, HIGH);
    character = Serial.read();
    Serial.println((char)character);
  }
}
