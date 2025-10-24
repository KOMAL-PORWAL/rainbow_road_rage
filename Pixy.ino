#include <Pixy2.h>

Pixy2 pixy;

void setup() {
  Serial.begin(115200);
  pixy.init();
  pixy.line.setMode(LINE_MODE_WHITE_LINE);
}

void loop() {
  // int8_t version = pixy.getVersion();
  int8_t result = pixy.line.getMainFeatures();
  // pixy.ccc.getBlocks();
  // Serial.println(pixy.ccc.blocks[0].m_signature);
  // Serial.println("test");
  Serial.println(result);
  //Serial.println(version);



  if (result > 0 && pixy.line.numVectors > 0) {
    Serial.println(result);
    int x0 = pixy.line.vectors[0].m_x0;
    int x1 = pixy.line.vectors[0].m_x1;

    int lineCenter = (x0 + x1) / 2;
    int imageCenter = pixy.frameWidth / 2;
    int error = lineCenter - imageCenter;

    if (error > 10) Serial.println("TURN RIGHT");
    else if (error < -10) Serial.println("TURN LEFT");
    else Serial.println("GO STRAIGHT");
  } else {
    Serial.println("NO LINE DETECTED");
  }

  delay(100);
}
