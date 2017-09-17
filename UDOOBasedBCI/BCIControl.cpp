#include "Arduino.h"
#include "BCIControl.h"

BCIControl::BCIControl()
{
    //set up each neural network for a series of consecutive operations and their parallel lines
    //each network can be named based on position in the network 1, 11, 12, 2, 21, 22,
    //giving us 26+10 outputs per network
    //first network must always be 1, as it's the As Trigger.
    //each network must have an option of whether it's As or S.
    getNetworkConfig(); //requires serial to be active.
    generateNetworkOutputConfig();

}

//seems to be TESTable
void BCIControl::setPin(int bciPin)
{
    _BCI_pin = bciPin;
    pinMode(_BCI_pin, INPUT);
}

//seems to be TESTable //NOPE, each layer must be added independently
void BCIControl::initialiseNNTriple(int numConnections, int numNeurons)
{
    int NNTLength = 3 * sizeof(_NetworkOutputs);
    NeuralNetwork[NNTLength] _NeuralNetsTriple;
    for( int i = 0 ; i < _NeuralNetsTriple.length; i+=3)
    {
        _NeuralNetsTriple[i] = new NeuralNetwork();
        _NeuralNetsTriple[i+1] = new NeuralNetwork();
        _NeuralNetsTriple[i+2] = new NeuralNetwork();

        _NeuralNetsTriple[i].addLayer(numConnections, numNeurons);
        _NeuralNetsTriple[i+1].addLayer(numConnections, numNeurons);
        _NeuralNetsTriple[i+2].addLayer(numConnections, numNeurons);

    }
}


//seems to be TESTable
void BCIControl::addLayerNNTriple(int numConnections, int numNeurons)
{
    for (int i = 0; i < sizeof(_NeuralNetsTriple); i+=3)
    {
        _NeuralNetsTriple[i].addLayer(numConnections, numNeurons);
        _NeuralNetsTriple[i+1].addLayer(numConnections, numNeurons);
        _NeuralNetsTriple[i+2].addLayer(numConnections, numNeurons);
    }

}

//seems to be TESTable
float BCIControl::recordLTSync(int duration, int numPoints, int BCI_pin, string Output)
{
    _BCI_pin = BCI_pin;
    float[numPoints] LinearTime;
    pinMode(BCI_pin, INPUT);
    interval = duration / numPoints; // duration must be a multiple of numPoints in 'milliseconds'. AKA 500, 500
    Serial.println("Record?");
    if (Serial.read() == 'what')
        Serial.println(Output);
    input = "";
    while (input != "y")
    {
        input = Serial.read();
    }
    for (int i = 0; i < numPoints; i++)
    {
        LinearTime[i] = analogRead(BCI_pin);
        delay(interval); // can use millis() or micros() with a displacement.
    }
    return LinearTime;
}

// //requires python equivalent


//seems to be TESTable //requires python equivalent,
void BCIControl::transmitLT(float LinearTime[], string Output)
{
    //Header
    Serial.println("transmitLT");
    check = serial.read();
    if (check == 'length')
    {
        Serial.println(LinearTime.length);
        checknext = serial.read();
        if (checknext = 'output')
        {
            Serial.println(Output);
            //Body
            for (int i = 0; i < LinearTime.length; i++)
            {
                Ith = serial.read();
                if (Ith == i)
                Serial.println(LinearTime[i]);
            }
        }

    }
}


//seems to be TESTable //requires python equivalent, BUILT
void BCIControl::learn10timesTriple(string Output)
{

    Serial.println("learn10times");
    Serial.println(Output);
    outputLocation = getOutputLocation(Output);//need method
    for (int i = 0; i < 10; i++)
    {
        Serial.println("getIthLength");
        dataLength = Serial.read();
        float learnData[dataLength][];
        for (int j = 0; j < dataLength; j++)
        {
            Serial.println(j);
            learnData[i][j] = (float) Serial.read();
        }
        _NeuralNetsTriple[outputLocation].trainNetwork(learnData, getExpectedOutputData(Output));
        _NeuralNetsTriple[outputLocation+1].trainNetwork(learnData, getExpectedOutputData(Output));
        _NeuralNetsTriple[outputLocation+2].trainNetwork(learnData, getExpectedOutputData(Output));

    }
}

//seems to be TESTable //requires python equivalent, BUILT
float BCIControl::test10timesTriple(int NetConfig, string Output)
{
    float[3][10] score[][];
    Serial.println("test10times");
    Serial.println(Output);
    outputLocation = getOutputLocation(Output);
    for (int i = 0; i < 10; i++)
    {
        Serial.println("getIthLength");
        dataLength = Serial.read();
        float learnData[dataLength][];
        for (int j = 0; j < dataLength; j++)
        {
            Serial.println(j);
            learnData[i][j] = (float) Serial.read();
        }
        _NeuralNetsTriple[outputLocation].processInputsToOutputs(learnData);
        _NeuralNetsTriple[outputLocation+1].processInputsToOutputs(learnData);
        _NeuralNetsTriple[outputLocation+2].processInputsToOutputs(learnData);

        score[1][i] = _NeuralNetsTriple[outputLocation].getOutputs();
        score[2][i] = _NeuralNetsTriple[outputLocation+1].getOutputs();
        score[3][i] = _NeuralNetsTriple[outputLocation+2].getOutputs();
    }
    return score[][];
}

//seems to be TESTable
float BCIControl::listenToBrain(int numberOfTimePoints, int timeOfTimePoints)
{
    float listen[];
    for(int i = 0; i < numberOfTimePoints; i++)
    {
        listen[numberOfTimePoints] = Analog.read(_BCI_pin);
        delay(timeOfTimePoints);
    }
    return listen[];
}

//seems to be TESTable
//float BCIControl::getExpectedOutputData(String Output)
//{   //gets the output data for a particular Output string.
    //might create a couple of options here. eOD ranges from 0 to 1.
    //thus Output being correct could range from 0.5 to 1. Try 1. Try 0.7.
    //need a way to specify max and min it could be, learn twice, interpolate...?
//    float eOD[]
//    for (int i = 0; i < ; i++)
//    {
//         if(_NetworkOutputs[i] == Output)
//         {
//              eOD[] = _NetworkOutputConfig[i];
//         }
//    }
//    return eOD[]
//}

//seems to be TESTable
void BCIControl::LearnFSFW(float linearFromBrain[], string Output)
{
    waveCompare = new DiscreteWaveletTransform(linearFromBrain[].length);

    sFWData = waveCompare.slowForward(linearFromBrain);
    fFWData = waveCompare.fastForward(linearFromBrain);
    FFData = waveCompare.fourierForward(linearFromBrain);

    outputLocationTriple = 3 * getOutputLocation(Output);

    _NeuralNetsTriple[outputLocationTriple].trainNetwork(sFWData, getExpectedOutputData(Output));
    _NeuralNetsTriple[outputLocationTriple+1].trainNetwork(fFWData, getExpectedOutputData(Output));
    _NeuralNetsTriple[outputLocationTriple+2].trainNetwork(FFWData, getExpectedOutputData(Output));
}

//seems to be TESTable
float BCIControl::TestFSFW(float linearFromBrain[], string Output)
{
    float outs[][];
    waveCompare = new DiscreteWaveletTransform(linearFromBrain.length);

    sFWData = waveCompare.slowForward(linearFromBrain);
    fFWData = waveCompare.fastForward(linearFromBrain);
    FFData = waveCompare.fourierForward(linearFromBrain);

    outputLocationTriple = 3 * getOutputLocation(Output);

    _NeuralNetsTriple[outputLocationTriple].processInputsToOutputs(sFWData);
    _NeuralNetsTriple[outputLocationTriple+1].processInputsToOutputs(fFWData);
    _NeuralNetsTriple[outputLocationTriple+2].processInputsToOutputs(FFWData);

    outs[0][] = _NeuralNetsTriple[outputLocationTriple].getOutputs();
    outs[1][] = _NeuralNetsTriple[outputLocationTriple+1].getOutputs();
    outs[2][] = _NeuralNetsTriple[outputLocationTriple+2].getOutputs();
    return outs[][];
}

//seems to be TESTable //requires python equivalent
void BCIControl::getNetworkConfig()
{
    Serial.println("getNetwork");
    while((string) Serial.read() != "ready")
    {
        delay(1);
    }
    Serial.println("getNetworkConfig");
    NCsize = (int) Serial.read(); //not sure on this, check read data type and convert
    for(int i = 0; i < NCsize; i++)
    {   //anything that does something in response to Voltage is a network
        //array of the numerical form of each network 0, 1, 11, 12, 2, 21, 22 ... AAAAA
        //max: 0:x:y:z:0 for the outputs of x:y:z:a
        Serial.println(i);
        _NetworkConfig[i] = (int) Serial.read();// (int) ?
    }

    Serial.println("getNetworkSize");
    NSsize = (int) Serial.read();// (int) ?
    for(int i = 0; i < NSsize; i++)
    {
        Serial.println(i);
        //array of the number of outputs per NN
        _NetworkSize[i] = (int) Serial.read();
    }

    Serial.println("getNetworkOutput");
    NOsize = (int) Serial.read(); //not sure on this, check read data type and convert
    for(int i = 0; i < NOsize; i++)
    {   //                                                      6               x ... (misses "Please", not correct)
        //array of the outputs in string form in the order of _NetworkSize[0] + _NS[1] + ... _NS[i]
        Serial.println(i);
        _NetworkOutputs[i] = (string) Serial.read(); // might need to convert to string??
    }

}

string BCIControl::getNetworkName(int i)
{
    return _NetworkOutputs[i];
}

//seems to be TESTable
int BCIControl::sumNetworkSizeTotalToI(int i)
{
    NST = 0;
    for (int j = 0; j<i; j++)
    {
        NST += _NetworkSize[j];
    }
    return NST;
}

//seems to be TESTable
void BCIControl::generateNetworkOutputConfig(float correctOutput)
{
    //Network output config holds all of the eOD for each output
    //AKA "Please",     0,    6, [cO,0,0,0,0,0],[0,cO,0,0,0,0]...
    //    NO[i],      NC[i], NS[i], NOC[i] ->
    //0 >> 1,2,3... 1 digit number
    //1 digit number >> 11, 12, 13 same number and another 1 digit number
    //go through network size and network outputs.

    //ith network goes to size, finds l
    for (int i = 0; i < sizeof(_NetworkConfig); i++)
    {
        if(i == 0)
        {
            _NetworkOutputConfig[i] = [correctOutput];
        }else{
            for (int j = 0; j < _NetworkSize[i]; j++)
            {

                for (int k = 0; k < _NetworkSize[i]; k++)
                {
                    _NetworkOutputConfig[sumNetworkSizeTotalToI[i]+j][k] = [0.];
                    if(j==k)
                    {
                        _NetworkOutputConfig[sumNetworkSizeTotalToI[i]+j][k] = [correctOutput];
                    }
                }
            }
        }

    }
}

//seems to be TESTable
float BCIControl::reOutput(int NCI, int NSI)
{
    return _NetworkOutputConfig[sumNetworkSizeTotalToI[NCI]+NSI];
}

//seems to be TESTable
int BCIControl::getOutputLocation(String Output)
{
    oLocation = 0;
    for (int i = 0; i < _NetworkOutputs.length; i++)
    {
        if (_NetworkOutputs[i] == Output)
        {
            oLocation = i;
            break;
        }
    }
    return oLocation
}
