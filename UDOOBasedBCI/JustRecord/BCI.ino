#include "BCIControl.h"

int pin = A0;
int duration = 512;
const int numPoints = 1024;
float recording1[numPoints];
BCIControl BCI;
int check_if_ready;

void setup() {
    Serial.begin(115200);
    BCI.setPin(pin);
}

void loop() {
    while(Serial.available() > 0)
    {
        Serial.read();
        check_if_ready = Serial.parseInt();
        if(check_if_ready == 1)
        {
            for (int i = 0; i< 16; i++)
            {
                for (int j = 0; j < 40 ; j++)
                {
                    BCI.recordLTSync(duration, numPoints, i);
                    BCI.transmitLT(i);
                }
            }
        }
    }
}


