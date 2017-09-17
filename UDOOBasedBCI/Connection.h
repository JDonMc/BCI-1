#ifndef Connection_h
#define Connection_h

#include "Arduino.h"

class Connection
{
    public:
        Connection();
        Connection(float tempWeight);
        void setWeight(float tempWeight);
        void randomiseWeight();
        float calcConnExit(float tempInput); //returns connExit
        float connEntry;
        float weight;
        float connExit;
};

#endif