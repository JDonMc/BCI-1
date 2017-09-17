#ifndef BCIControl_h
#define BCIControl_h

#include "Arduino.h"
#include "Wavelet.h"
#include "NeuralNetwork.h"

//1
//start with Saving to TextFile, Arduino > Serial > Py > File.
//then learning / testing from Text File > Py > Serial > Arduino > NN.
//then create an Asynchronous / Synchronous division.

//tips
//need to set it up so that 1 NN for each type of (Fourier, Wavelet, FastWavelet) transform.
//20 examples recorded from Analog Read and transmitted serially ready to save in python textfile. //save in py
//learn from python textfile 10 times for each of the 3 NNs for each learning answer
//test from python textfile 10 times for each of the 3 NNs for each learning answer

//include the ability to create various NNs with varied Layers, Neurons, Number of Connections. for each of 3.
//include the ability to redefine the Wavelet / FastWavelet transform constants.


//plan
//permutations:1, 10, ..., 100  1, 10, ..., 100   1, 10, ..., 100 //////// each neuron and connection must be related
//Transform (3) * Layers (10) * Neurons (10) * NumConnections (10)///// C(L1) = input.length > N(L1) > N(L2)
//>>> find the best N combinations for each DataSet/AnswerType  ///// ... > N(LFinal) = OutputOptions
// if(Wavelet/FastWavelet) include Constants,
//^'Selects for Transform' // for the best NN in each AnswerType:
//permutations:  x-5, x-4, ..., x+5, for each
//Transform (1) * Constants (11) * Layers (11) * Neurons (11) * Num Connections (11)
//^'Selects for NN config' // for the best NN in each AnswerType:
//permutations: x-0.5, x-0.4, ..., x+0.5, for constants
//therefore take in an 'A' value scaling the focus around
//^'Selects for Constants'

//^^^total optimisation procedure for Accuracy.
//Needs to be completed after an interval of time from the Total X learnings for each Answer.
//Like 'backing up' an iPhone, but reconfiguring learnings for optimisation.
//ENCRYPT AND STORE 'TOTAL X LEARNINGS FOR EACH ANSWER' LOCALLY, SEPARATE FROM INTERNET.
//Possibly replace with a save feature for just the constants of each NN (bias and weighting).
//only access and configure in user selected standby mode.


// need to balance the counts of each layer through trial and error to maximise accuracy at minimum computation time
// graph this data in terms of C, total num of connections, L number of layers, N number of neurons
// C vs time, L vs time, N vs time, C(l, n, c) etc. so control other variables.
// find the set of consistently accurate and then compare from that in terms of variables.

//total
//possibly include the ability to learn in every permutation of order
//possibly include the ability to compare the accuracy (n in 0 to 10) of each permutation order
//possibly include the ability to test from the learnt 10 times, to see if it remains consistent
//possibly include the ability to define which paths exist and where they flow.


//for the combining of each method
//// neural net input -inf to +inf per i (layer n neuron count is layer n+1 connection count), output 0 to 1 per i
////                                      layer 1 connection count is input data length
////                                final layer neuron count is number of outputs (aka concepts to choose from)
class BCIControl
{
    public:
        void BCIControl();
        void setPin(int bciPin);
        void initialiseNNTriple(int numConnections, int numNeurons);
        //initialiseNNQuad(int numConnections, int numNeurons) - takes lin+wav,lin+four,wav+four,lin+wav+four.
        void addLayerNNTriple(int numConnections, int numNeurons);
        //string[] setUpControlPathsNN(); - not sure
        float recordLTSync(int duration, int numPoints, int BCI_pin, string Output);
        //void runAsync(int duration, int numPoints, int BCI_pin, int multiples);
        void transmitLT(float LinearTime[], string Output);
        void learn10timesTriple(string LearningAnswer, string neuralNetworkID); // measure the time on this operation
        void test10timesTriple(float expectedOutputData[]); // not sure on Output configuration
        float listenToBrain(int numberOfTimePoints, int timeOfTimePoints);
        float getExpectedOutputData(String Output);
        void LearnFSFW(float linearFromBrain[], string neuralNetworkIDs[]); // measure the time on this operation
        float TestFSFW(float linearFromBrain[], string neuralNetworkIDs[]);
        int getNetworkConfig(); //Serial from python
        int sumNetworkSizeTotalToI(int i);
        void generateNetworkOutputConfig(float correctOutput); //run on creation
        float reOutput(int NCI, int NSI);
        int getOutputLocation(String Output);

    private:
        int _DiscreteWaveletTransform[];
        string _SaveFileName;
        string _LearningAnswer;
        string _DesiredOutput;
        string _HistoricalListLength;
        int _NetworkConfig[];
        int _NetworkSize[];
        string _NetworkOutputs[];
        float _NetworkOutputConfig[][];
        int _BCI_pin;
        NeuralNet _NeuralNetsTriple[];
};

#endif