#include "Arduino.h"
#include "Connection.h"

Connection::Connection()
{
    randomiseWeight();
}
Connection::Connection(float tempWeight)
{
    setWeight(tempWeight);
}
void Connection::setWeight(float tempWeight)
{
    weight = tempWeight;
}
void Connection::randomiseWeight()
{
    setWeight(random(2)-1);
}
float calcConnExit(float tempInput)
{
    connEntry = tempInput;
    connExit = connEntry * weight;
    return connExit;
}