#include "Arduino.h"
#include "Connection.h"
#include "Neuron.h"
#include "Layer.h"

Layer::Layer(int numberConnections, int numberNeurons)
{
    _numberConnections = numberConnections;
    _numberNeurons = numberNeurons;
    /* Add all the neurons and actualOutputs to the layer */
    for(int i=0; i<numberNeurons; i++)
    {
        Neuron tempNeuron = new Neuron(numberConnections);
        addNeuron(tempNeuron);
        addActualOUTPUT();
    }
}

/* Function to add an input or output Neuron to this Layer */
void Layer::addNeuron(Neuron xNeuron)
{
    _xNeuron = xNeuron;
    neurons[] = (Neuron) append(neurons, xNeuron);
}

/* Function to get the number of neurons in this layer */
int Layer::getNeuronCount()
{
    return sizeof(neurons);
}

/*Function to increment the size of the actualOUTPUTs array by one. */
void Layer::addActualOUTPUT()
{
    actualOUTPUTs = float[sizeof(actualOUTPUTs)+1]; ///changed a few times
}

/* Function to set the ENTIRE expectedOUTPUTs array in one go. */
void Layer::setExpectedOUTPUTs(float tempExpectedOUTPUTs[])
{
    _tempExpectedOUTPUTs = tempExpectedOUTPUTs;
    expectedOUTPUTs = tempExpectedOUTPUTs;
}

/* Function to clear ALL values from the expectedOUTPUTs array */
void Layer::clearExpectedOUTPUT()
{
    expectedOUTPUTs = float[sizeof(expectedOUTPUTs)]; ///changed from .expand()
}

/* Function to set the learning rate of the layer */
void Layer::setLearningRate(float tempLearningRate)
{
    _tempLearningRate = tempLearningRate;
    learningRate = tempLearningRate;
}

/* Function to set the inputs of this layer */
void Layer::setInputs(float tempInputs[])
{
    _tempInputs = tempInputs;
    layerINPUTs=tempInputs;
}

/* Function to convert ALL the Neuron input values into Neuron output values in this layer, through a special activation function. */
void Layer::processInputsToOutputs()
{
    /* neuronCount is used a couple of times in this function. */
    int neuronCount = getNeuronCount();

    /* Check to make sure that there ar neurons in this layer to process the inputs */
    if(neuronCount>0)
    {
        /* Check to make sure the number of inputs matches the number of Neuron Connections. */
        if(sizeof(layerINPUTs)!=neurons[0].getConnectionCount())
        {
            println("Error in Layer: processInputsToOutputs: The number of inputs do Not match the number of Neuron connections in this layer");
            exit();
        }else
        {
            /*the number of inputs are fine: continue Calculate the actualOUTPUT of each neuron in this layer based on their layerInputs */
            for(int i=0; i<neuronCount;i++)
            {           ////// the number of new connections is equal to the previous number of neurons ////////////
                actualOUTPUTs[i] = neurons[i].getNeuronOutput(layerINPUTs);
            }
         }
    } else
    {
        println("Error in Layer: processInputsToOutputs: There are no Neurons in this layer");
        exit();
    }
}

/* Function to get the error of this layer */
float Layer::getLayerError()
{
    return layerError;
}

/* Function to set the error of this layer */
void Layer::setLayerError(float tempLayerError)
{
    _tempLayerError = tempLayerError;
    layerError=tempLayerError;
}

/* Function to increase the layerError by a certain amount */
void Layer::increaseLayerErrorBy(float temporaryLayerError)
{
    _temporaryLayerError = temporaryLayerError;
    layerError+=tempLayerError;
}

/* Function to calculate and set the deltaError of each neuron in the layer */
void Layer::setDeltaError(float expectedOutputData[])
{
    _expectedOutputData = expectedOutputData;
    setExpectedOUTPUTs(expectedOutputData);
    int neuronCount = getNeuronCount();
    /* reset the layer error to 0 before cycling through each neuron */
    setLayerError(0);
    for(int i=0; i<neuronCount;i++)
    {
        neurons[i].deltaError = actualOUTPUTs[i]*(1-actualOUTPUTs[i])*(expectedOUTPUTs[i]-actualOUTPUTS[i]);
        /* Increase the layer Error by absolute difference between the calculated value and expected */
        increaseLayerErrorBy(abs(expectedOUTPUTs[i]-actualOUTPUTs[i]));
    }
}

/* Function to train the layer */
void Layer::trainLayer(float temporaryLearningRate)
{
    _temporaryLearningRate = temporaryLearningRate;
    setLearningRate(tempLearningRate);
    int neuronCount = getNeuronCount();

    for(int i=0; i<neuronCount; i++)
    {
        /* update the bias for neuron[i] */
        neurons[i].bias += (learningRate * 1 * neurons[i].deltaError);

        /* update the weight of each connection for this neuron[i] */
        for(int j=0; j<neurons[i].getConnectionCount(); j++)
        {
            neurons[i].connections[j].weight += (learningRate * neurons[i].connections[j].connEntry * neurons[i].deltaError);
        }
    }
}