#ifndef SimpleDiscreteWaveletTransform_h
#define SimpleDiscreteWaveletTransform_h

#include "Arduino.h"


class DiscreteWaveletTransform
{
    public:
         Wavelet(int waveletArrayLength); //length must be power of 2 and has something to do with scaleLength
         float slowForward(float timePoints[]);
         float slowReverse(float hilbPoints[]);
         float fastForward(float timePoints[]);
         float fastReverse(float hilbPoints[]);
         float fourierForward(float timePoints[]);
         float fourierReverse(float freqPoints[]);
         int getScalingLength(int scaleLength);
         void setScalingLength(); //if the length is changed the scaling must be set
         float saveScaling();
         void setScaling(float scalingDeCom[]); //orthonormalspace is auto built after set
         void buildOrthonormalSpace();

    private:
         int _waveletArrayLength;
         int _maxLevel;
         int _motherWavelength;
         int _transformWavelength;
         float _scalingDeCom[];
         float _waveletDeCom[];
         float _scalingReCon[];
         float _waveletReCon[];

};



#endif


