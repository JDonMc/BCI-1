#ifndef BCIControl_h
#define BCIControl_h

#include "Arduino.h"

class BCIControl
{
    public:
        BCIControl();
        void setPin(int bciPin);
        void recordLTSync(int duration, int numPoints, int output_location);
        void transmitLT(int output_location);

    public:
        int _numPoints;
        int _LinearTime[];
        int _BCI_pin;

};

#endif