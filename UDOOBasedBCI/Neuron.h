#ifndef Neuron_h
#define Neuron_h

#include "Arduino.h"
#include "Connection.h"

class Neuron
{
    public:
        Connection[] connections={};
        float bias; //returns
        float neuronInputValue; //returns
        float neuronOutputValue; //returns
        float deltaError; //returns

    //check Neuron(i++)`


        Neuron(int numOfConnections; i ++);
        void addConnection(Connection conn);
        int getConnectionCount(); //returns
        void setBias(float tempBias);
        void randomiseBias();
        float getNeuronOutput(float[] connEntryValues); //returns
        float Activation(float x); //returns
    private:
        int _numOfConnections;
        Connection _conn;
        float _tempBias;
        float[] _connEntryValues;
        float _x;
};

#endif