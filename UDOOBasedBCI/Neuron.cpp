#include "Connection.h"
#include "Arduino.h"
#include "Neuron.h"

Neuron::Neuron( int numOfConnections )
{ // not sure if it needs to be private:
    _numOfConnections = numOfConnections;
    randomiseBias();
    for(int i = 0; i<numOfConnections; i++)
    {
        Connection conn = new Connection();
        addConnection(conn);
    }
}

void Neuron::addConnection(Connection conn)
{
    connections[] = ((Connection) append(connections[], conn));
}

//Function to return the number of connections associated with this neuron.
int Neuron::getConnectionCount()
{
    return sizeof(connections);
}

//Function to set the bias of this Neuron
void Neuron::setBias(float tempBias)
{
    bias = tempBias;
}

//Function to randomise the bias of this Neuron
void Neuron::randomiseBias()
{
    setBias(random(1));
}

//Function to convert the neuronInputValue to an neuronOutputValue
//Make sure that the number of connEntryValues matches the number of connections

float Neuron::getNeuronOutput(float connEntryValues[])
{   ///////////// connection count must be the size of input array /////////// therefore NN can Narrow each layer.
    if(sizeof(connEntryValues)!=getConnectionCount())
    {
        println("Neuron Error: getNeuronOutput(): Wrong number of connEntryValue");
        exit();
    }
    neuronInputValue=0;
    //First Sum all of the weighted connection values (connExit) attached to this neuron.
    for(int i=0; i<getConnectionCount(); i++)
    {    ////////// each neuron gets a sum of the outputs from each connection to each data point//////////////
        neuronInputValue += connections[i].calcConnExit(connEntryValues[i]);
    }
    //add the bias to the Neuron's inputValue
    neuronInputValue += bias;
    //Send the inputValue through the activation function to produce ethe Neuron's outputValue
    neuronOutputValue = Activation(neuronInputValue);

    return neuronOutputValue;
}

    //Sigmoid Activation function
float Neuron::Activation(float x)
{
    float activatedValue = 1 / (1 + exp(-1*x)); ////////// graph this range ///////// set as input data point range
    return activatedValue;                          /////// x can range -inf to +inf //// y can range 0 to 1
}                                               ///// y can be modded by connection weighting to -inf to +inf