#include "Adafruit_PM25AQI.h"

// Initialise PMSA003 sensor
HardwareSerial pmSerial(1);
Adafruit_PM25AQI aqi = Adafruit_PM25AQI();

unsigned long lastPMReading = 0;
const unsigned long pmInterval = 10000;

void setup() {
    Serial.begin(115200);
    delay(1000);

    // GPIO 19
    pmSerial.begin(9600, SERIAL_8N1, 19, -1);

    if (!aqi.begin_UART(&pmSerial)) {
        Serial.println("Could not find PM2.5 sensor!");
        while (1) {
            delay(10);
        }
    }

    Serial.println("PMSA003 initialised successfully!");
}

void loop() {
    unsigned long currentMillis = millis();

    if (currentMillis - lastPMReading >= pmInterval) {
        PM25_AQI_Data data;

        if (aqi.read(&data)) {
            /*Serial.print("PM2.5: ");
            Serial.print(data.pm25_standard);
            Serial.println(" ug/m3");

            Serial.print("PM10: ");
            Serial.print(data.pm100_standard);
            Serial.println(" ug/m3");*/

            Serial.print("PM2.5 (env): ");
            Serial.print(data.pm25_env);
            Serial.println(" ug/m3");

            Serial.print("PM10 (env): ");
            Serial.print(data.pm100_env);
            Serial.println(" ug/m3");
        } else {
            Serial.println("PM2.5 reading failed");
        }

        lastPMReading = currentMillis;
    }

    delay(10);
}
