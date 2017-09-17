#include "Arduino.h"
#include "NeuralNetwork.h"
#include "Connection.h"
#include "Neuron.h"
#include "Layer.h"
//might have to use specific public variables (_XX rather than XX) for intra-class calling - unsure



NeuralNetwork::NeuralNetwork()
{
    /* the default learning rate of a nn is set to 0.1, which can by changed with setLearningRate(LR) function */
    learningRate = 0.1;
}

/* Function to add a Layer to the Neural Network */
void NeuralNetwork::addLayer(int numConnections, int numNeurons)
{
    _numConnections = numConnections;
    _numNeurons = numNeurons;
    layers[] = (Layer) append(layers, new Layer(numConnections, numNeurons));
}

/* Function to return the number of layers in the neural network */
int NeuralNetwork::getLayerCount()
{
    return sizeof(layers[]);
}

/* Function to set the learningRate of the Neural Network */
void NeuralNetwork::setLearningRate(float tempLearningRate)
{
    _tempLearningRate = tempLearningRate;
    learningRate = tempLearningRate;
}

/* Function to set the inputs of the neural network */
void NeuralNetwork::setInputs(float tempInputs[])
{
    _tempInputs = tempInputs;
    arrayOfInputs = tempInputs;
}

/* Function to set the inputs of a specified layer */
void NeuralNetwork::setLayerInputs(float temporaryInputs[], int layerIndex)
{
    _temporaryInputs = temporaryInputs;
    _layerIndex = layerIndex;
    if(layerIndex>getLayerCount() -1 )
    {
        println("NN Error: setLayerInputs: Layer index " + layerIndex + " exceeded limits");
    } else
    {
        layers[layerIndex].setInputs(tempInputs);
    }
}

/* Function to set the outputs of the neural network */
void NeuralNetwork::setOutputs(float tempOutputs[])
{
    _tempOutputs = tempOutputs;
    arrayOfOutputs = tempOutputs;
}

/* Function to return the outputs of the NN */
float NeuralNetwork::getOutputs()
{
    return arrayOfOutputs[];
}


/* Function to process the NN's IVs and convert to output pattern using ALL layers of NN*/
void NeuralNetwork::processInputsToOutputs(float temporInputs[])
{
    _temporInputs = temporInputs;
    setInputs(temporInputs);

    /* Check to make sure that the number of NN inputs matches the Neuron Connection Count in the first layer */
    if(getLayerCount()>0)
    {
        if(sizeof(arrayOfInputs)!=layers[0].neurons[0].getConnectionCount())
        {
            println("NN Error: processInputsToOutputs; The number of inputs do Not match the NN");
            exit();
        } else
        {
            /* the number of inputs are fine: continue */
            for(int i=0; i < getLayerCount(); i++)
            {
                /*Set the inputs for each layer: the first layer gets its input data from the nN whereas the nd and subsequent layers
                get their input dat from the previous layers actual output. */
                if(i==0)
                {
                    setLayerInputs(arrayOfInputs, i);
                } else
                {                   //previous outs, layer number////////// thus output range == input range////////
                    setLayerInputs(layers[i-1].actualOUTPUTs, i);
                }

                /* Now that the layer has had its IVs set. process, convert into output, plug into net layer */
                layers[i].processInputsToOutputs();
            }
            /* Once all the data has filtered through to the end of network, can grab the actual outputs of last layer
            these values become the NN output values (arrayOfOutputs)*/
            setOutputs(layers[getLayerCount()-1].actualOUTPUTs);
        }
    } else
    {
        println("Error: there are no layers in NN");
        exit();
    }
}

/* Function to train the entire network using an array */
void NeuralNetwork::trainNetwork(float inputData[], float expectedOutputData[])
{
    _inputData = inputData;
    _expectedOutputData = expectedOutputData;
    /*populate the entire network by processing input data */
    processInputsToOutputs(inputData);

    /* train each layer from back to front (Back Propagation) */
    for(int i=getLayerCount()-1; i>-1; i--)
    {
        if(i==getLayerCount()-1)
        {
            layers[i].setDeltaError(expectedOutputData);
            layers[i].trainLayer(learningRate);
            networkError = layers[i].getLayerError();
        } else
        {
            /* Calculate the expected value for each neuron in this layer (eg. Hidden layer) */
            for(int j=0; j < layers[i].getNeuronCount(); j++)
            {
                /* Reset the delta error of this neuron to zero */
                layers[i].neurons[j].deltaError=0;
                /* the delta error of a hidden layer is equal to the SUM of the product of the connection weight and error of the neurons in the next layer
                connection 1 of each neuron in the output layer connect with Neuron1 in the hidden layer */
                for(int k=0; k<layers[i+1].getNeuronCount(); k++)
                {
                    layers[i]neurons[j].deltaError += (layers[i+1].neurons[k].connections[j].weight * layers[i+1].neurons[k].deltaError);
                }
                /* Now that we have the sum of errors * weights attached to this neuron we must multiply it by the derivative of the activation function */
                layers[i].neurons[j].deltaError *= (layers[i].neurons[j].neuronOutputValue * (1-layers[i].neurons[j].neuronOutputValue));
            }
            /* Now that you have all the necessary fields populated, you can now Train this hidden layer then clear the Expected outputs, ready for the next round*/
            layers[i].trainLayer(learningRate);
            layers[i].clearExpectedOUTPUT();
        }
    }
}

/* Function to train the entire network, using an array of input and expected data within an ArrayList */
void NeuralNetwork::trainingCycle(ArrayList trainingInputData, ArrayList trainingExpectedData, Boolean trainRandomly) //unsure about ArrayList
{
    _trainingInputData = trainingInputData;
    _trainingExpectedData = trainingExpectedData;
    _trainRandomly = trainRandomly;
    int dataIndex;

    /* re initialise the training error with every cycle*/
    trainingError=0;

    /* cycle through the training data ether randomly or sequentially */
    for(int i=0; i<trainingInputData.size(); i++)
    {
        if(trainRandomly)
        {
            dataIndex=(int) (random(trainingInputData.size()));
        } else
        {
            dataIndex= i;
        }

        trainNetwork((float) trainingInputData[].get(dataIndex),(float) trainingExpectedData[].get(dataIndex)); //unsure about .get(dataIndex)

        /* use the network error variable which is calculated at the end of each individual training session to calculate the entire trainingError. */
        trainingError += abs(networkError);
    }
}

    /* Function to train the network until the Error is below a specific threshold */
void NeuralNetwork::autoTrainNetwork(ArrayList trainInputData, ArrayList trainingExpectedData, float trainingErrorTarget, int cycleLimit)
{
    _trainInputData = trainInputData;
    _trainingExpectedData = trainingExpectedData;
    _trainingErrorTarget = trainingErrorTarget;
    _cycleLimit = cycleLimit;
    trainingError = 9999;
    int trainingCounter = 0;

    /* Cycle through the training data until the trainingError gets below trainingErrorTarget or */
    while(trainingError > trainingErrorTarget && trainingCounter < cycleLimit)
    {
        /* re initialise the training error with every cycle */
        trainingError = 0;

        /* Cycle through the training data randomly */
        trainingCycle(trainingInputData, trainingExpectedData, true);

        /* increment the training counter to prevent endless loop*/
        trainingCounter++;
    }

    /* Due to the random nature in which this NN is trained there may be occasions when the error may drop below threshold, to check if so we will go through
    one more cycle but sequentially */
    if(trainingCounter < cycleLimit)
    {
        trainingCycle(trainingInputData, trainingExpectedData, false);
        trainingCounter++;
        if(trainingError > trainingErrorTarget)
        {
            if(retrainChances < 10)
            {
                retrainChances++;
                autoTrainNetwork(trainingInputData, trainingExpectedData, trainingErrorTarget, cycleLimit);
            }
        }
    } else
    {
        println("Cycle limit has been reached. has been retrained " + retrainChances + "times. Error: " + trainingError);
    }
}
