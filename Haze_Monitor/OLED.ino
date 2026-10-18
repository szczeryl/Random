//SDA to #21. SCL to #22

#include <Arduino.h>
#include <U8g2lib.h>
#include <Wire.h>

// I2C OLED, 128 x 64
U8G2_SH1106_128X64_NONAME_F_HW_I2C
  u8g2(U8G2_R0, U8X8_PIN_NONE);

void setup() {
  Wire.begin(21, 22);  // SDA = GPIO 21, SCL = GPIO 22

  u8g2.begin();
  u8g2.clearBuffer();

  u8g2.setFont(u8g2_font_ncenB08_tr);
  u8g2.drawStr(0, 20, "Hello ESP32!");
  u8g2.drawStr(0, 40, "OLED working");

  u8g2.sendBuffer();
}

void loop() {
}
