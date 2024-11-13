#include <DHT.h>
#include <ArduinoJson.h>


#define DHTPIN 13
#define DHTTYPE DHT22
#define LDR_PIN 15
#define BUTTON1_PIN 32
#define BUTTON2_PIN 34
#define RELAY_PIN 5

DHT dht(DHTPIN, DHTTYPE);


void setup() {
  Serial.begin(9600);
  pinMode(BUTTON1_PIN, INPUT_PULLUP);
  pinMode(BUTTON2_PIN, INPUT_PULLUP);
  pinMode(RELAY_PIN, OUTPUT);

  digitalWrite(RELAY_PIN, LOW);

}
void loop() {

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    delay(2000);
    return; 
  }
 
  bool button1State = digitalRead(BUTTON1_PIN) == LOW;
  bool button2State = digitalRead(BUTTON2_PIN) == LOW;

  int ldrValue = analogRead(LDR_PIN);

  bool relay = button1State && button2State && ldrValue > 500 && (humidity <= 40  || temperature > 30);
  
  if (relay) {
    digitalWrite(RELAY_PIN, HIGH);
  } else {
    digitalWrite(RELAY_PIN, LOW);
  } 

  StaticJsonDocument<200> jsonDoc;
  jsonDoc["k"] = button1State;
  jsonDoc["p"] = button2State;
  jsonDoc["ldr"] = ldrValue;
  jsonDoc["humidity"] = humidity;
  jsonDoc["temperature"] = temperature;
  jsonDoc["relay"] = relay;

  serializeJson(jsonDoc, Serial);
  Serial.println();
  Serial.print(",");

  delay(1000);
}
