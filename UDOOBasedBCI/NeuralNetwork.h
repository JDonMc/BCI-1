#ifndef NeuralNetwork_h
#define NeuralNetwork_h

#include "Arduino.h"
#include "Connection.h"
#include "Neuron.h"
#include "Layer.h"

class NeuralNetwork
{
    public:
        Layer[] layers = {};
        float[] arrayOfInputs = {};
        float[] arrayOfOutputs = {};
        float learningRate;
        float networkError;
        float trainingError;
        int retrainChances = 0;

        NeuralNetwork();
        void addLayer(int numConnections, int numNeurons); //each neuron has all connections
        int getLayerCount(); //returns
        void setLearningRate(float tempLearningRate);
        void setInputs(float[] tempInputs);
        void setLayerInputs(float[] temporaryInputs, int layerIndex); //changed name of #1.
        void setOutputs(float[] tempOutputs);
        float[] getOutputs(); //returns
        void processInputsToOutputs(float[] temporInputs); //changed name.
        void trainNetwork(float[] inputData, float[] expectedOutputData);
        void trainingCycle(ArrayList trainingInputData, ArrayList trainingExpectedData, Boolean trainRandomly);//should be a type of learning that is supersymmetric (same all ways);
        void autoTrainNetwork(ArrayList trainInputData, ArrayList trainingExpectedData, float trainingErrorTarget, int cycleLimit);//#1
    private:
        int _numConnections;
        int _numNeurons;
        float _tempLearningRate;
        float[] _tempInputs;
        float[] _temporaryInputs; //changed name
        int _layerIndex;
        float[] _tempOutputs;
        float[] _temporInputs; //changed name
        float[] _inputData;
        float[] _expectedOutputData;
        ArrayList _trainingInputData;
        ArrayList _trainingExpectedData;
        Boolean _trainRandomly;
        ArrayList _trainInputData; //changed name
        ArrayList _trainingExpectedData;
        float _trainingErrorTarget;
        int _cycleLimit;
};

#endif

// test various numConnections, numNeurons, numLayers