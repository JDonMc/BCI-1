#include "Arduino.h"
#include "BCIControl.h"

BCIControl::BCIControl()
{
}

void BCIControl::setPin(int bciPin)
{
    _BCI_pin = bciPin;
    pinMode(_BCI_pin, INPUT);
}

void BCIControl::recordLTSync(int duration, int numPoints, int output_location)
{
    _numPoints = numPoints;
    int interval = 1000 * duration / numPoints;
    Serial.println(9998); //ready to record!
    int check = 0;
    Serial.read();
    check = Serial.parseInt(); //ready to record?
    if (check == 9998)
    {
        Serial.println(output_location);
        check = 0;
    }
    Serial.read();
    check = Serial.parseInt();
    if (check == 9998)
    {
        for (int i = 0; i < numPoints; i++)
        {
            _LinearTime[i] = analogRead(_BCI_pin);
            delayMicroseconds(interval);
        }
    }
}

void BCIControl::transmitLT(int output_location)
{
    Serial.println(9999);
    int check = 0;
    Serial.read();  //asks for confirmation, ready to transmit
    check = Serial.parseInt(); // should be 9999
    if (check == 9999)
    {
        Serial.println(_numPoints);
        check = 0;
    }
    Serial.read();  //asks for confirmation, what is the output
    check = Serial.parseInt();
    if (check == 9999)
    {
        Serial.print(output_location);
    }
    for (int i = 0; i < _numPoints; i++)
    {
        Serial.println(_LinearTime[i]);
    }

}

