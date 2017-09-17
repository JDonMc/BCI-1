#ifndef Layer_h
#define Layer_h

#include "Arduino.h"
#include "Connection.h"
#include "Neuron.h"

class Layer
{
    public:
        Neuron neurons[] = {};
        float layerINPUTs[]={};
        float layerOUTPUTs[]={};
        float expectedOUTPUTs[]={};
        float layerError;
        float learningRate;

        Layer(int numberConnections, int numberNeurons);
        void addNeuron(Neuron xNeuron);
        int getNeuronCount(); //returns
        void addActualOUTPUT();
        void setExpectedOUTPUTs(float tempExpectedOUTPUTs[]);
        void clearExpectedOUTPUT();
        void setLearningRate(float tempLearningRate);
        void setInputs(float tempInputs[]);
        void processInputsToOutputs();
        float getLayerError(); //returns
        void setLayerError(float tempLayerError);
        void increaseLayerErrorBy(float temporaryLayerError); // set to different variable
        void setDeltaError(float expectedOutputData[]);
        void trainLayer(float temporaryLearningRate); // set to different variable
    private:
        int _numberConnections;
        int _numberNeurons;
        Neuron _xNeuron;
        float _tempExpectedOUTPUTs[];
        float _tempLearningRate;
        float _tempInputs[];
        float _tempLayerError;
        float _temporaryLayerError; // set to different variable
        float _expectedOutputData[];
        float _temporaryLearningRate; // set to different variable

};

#endif
