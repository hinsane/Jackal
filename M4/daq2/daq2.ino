#define MIC_PIN A0
#define SAMPLE_RATE_HZ 105000

void setup() {
  Serial.begin(115200);
  while (!Serial) { delay(10); }
  
  pinMode(MIC_PIN, INPUT);
}

void loop() {
  for (int i = 0; i < SAMPLE_RATE_HZ/1000; i++) {
    int16_t sample = analogRead(MIC_PIN);
    Serial.write((uint8_t *)&sample, sizeof(sample));
    delayMicroseconds(1000/SAMPLE_RATE_HZ);
  }
}
