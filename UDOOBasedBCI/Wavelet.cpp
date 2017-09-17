#include "Arduino.h"
#include "SimpleDiscreteWaveletTransform.h"


Wavelet::Wavelet(int waveletArrayLength)
{
    _waveletArrayLength = waveletArrayLength;
    _maxLevel = (int)round( log( waveletArrayLength ) / log( 2. ) ); //test if works math.h //////////////////////

    _transformWavelength = 2; // minimal wavelength of input signal

    _motherWavelength = 18; // wavelength of mother wavelet

    _scalingDeCom = new float[ _motherWavelength ];
    _scalingDeCom[ 0 ] = 0.0014009155259146807; //is this decimal range allowed?
    _scalingDeCom[ 1 ] = 0.0006197808889855868;
    _scalingDeCom[ 2 ] = -0.013271967781817119;
    _scalingDeCom[ 3 ] = -0.01152821020767923;
    _scalingDeCom[ 4 ] = 0.03022487885827568;
    _scalingDeCom[ 5 ] = 0.0005834627461258068;
    _scalingDeCom[ 6 ] = -0.05456895843083407;
    _scalingDeCom[ 7 ] = 0.238760914607303;
    _scalingDeCom[ 8 ] = 0.717897082764412;
    _scalingDeCom[ 9 ] = 0.6173384491409358;
    _scalingDeCom[ 10 ] = 0.035272488035271894;
    _scalingDeCom[ 11 ] = -0.19155083129728512;
    _scalingDeCom[ 12 ] = -0.018233770779395985;
    _scalingDeCom[ 13 ] = 0.06207778930288603;
    _scalingDeCom[ 14 ] = 0.008859267493400484;
    _scalingDeCom[ 15 ] = -0.010264064027633142;
    _scalingDeCom[ 16 ] = -0.0004731544986800831;
    _scalingDeCom[ 17 ] = 0.0010694900329086053;
    buildOrthonormalSpace();
}

float Wavelet::slowForward(float timePoints[])
{
    float arrHilb[] = new float[ _waveletArrayLength ];
    int h = _waveletArrayLength >> 1;
    for( int i = 0; i < h; i++ )
    {
        arrHilb[ i ] =  0.;
        arrHilb[ i + h ] = 0.;

        for( int j = 0; j < _motherWavelength; j++ )
        {
            int k = ( i << 1 ) + j; // k = ( i * 2 ) + j;
            while( k >= _waveletArrayLength )
            {
                k -= _waveletArrayLength;
            }

            arrHilb[ i ] += timePoints[ k ] * _scalingDeCom[ j ]; // low pass filter for the energy (approximation)
            arrHilb[ i + h ] += timePoints[ k ] * _waveletDeCom[ j ]; // high pass filter for the details

            //return a value from here to show the equation in the middle of running for a .gif of a graph
            //depicting the creation of hilbert space from linear time space.
        }

    }

    return arrHilb[];
}

float Wavelet::slowReverse(float hilbPoints[])
{
    float arrTime[] = new float[ _waveletArrayLength ];
    arrTimeLength = sizeof(arrTime[]); // again, might just skip
    for( int i = 0; i < arrTimeLength; i++ )
    {
        arrTime[ i ] = 0.; // set to zero before sum up
    }

    int h = arrTimeLength >> 1; // .. -> 8 -> 4 -> 2 .. shrinks in each step by half wavelength
    for( int i = 0; i < h; i++ )
    {

          for( int j = 0; j < _motherWavelength; j++ )
          {

               int k = ( i << 1 ) + j; // k = ( i * 2 ) + j;
               while( k >= arrTimeLength )
               {
                    k -= arrTimeLength; // circulate over arrays if scaling and wavelet are larger
               }

               // adding up energy from low pass (approximation) and details from high pass filter
               arrTime[ k ] += ( hilbPoints[ i ] * _scalingReCon[ j ] )+ ( hilbPoints[ i + h ] * _waveletReCon[ j ] );
          } // Reconstruction from patterns of: { scaling coefficients | wavelet coefficients }

    } // h = 2^(p-1) | p = { 1, 2, .., N } .. shrink in each step by half wavelength

    return arrTime[];

  } // reverse
}

float Wavelet::fastForward(float timePoints[])
{

    //java
    float arrHilb[] = timePoints[];

    int l = 0;
    int h = sizeof(arrHilb);
    while( h >= _transformWavelength && l < _maxLevel )
    {
         float[ ] arrTempPart = slowForward( arrHilb, h );
         for(int i = 0; i < h ; i ++)
         {
              arrHilb[i] = arrTempPart[i];
         }
         h = h >> 1;
         l++;

    } // levels

    return arrHilb[];

}

float Wavelet::fastReverse( float hilbPoints[])
{
    float arrTime[] = hilbPoints[];
    int h = _transformWavelength;
    for( int l = _waveletArrayLength; l < _maxLevel; l++ )
    {
        h = h << 1; // begin reverse transform at certain - matching - level of Hilbert space
    }
    while( h <= _waveletArrayLength && h >= _transformWavelength )
    {
         float[ ] arrTempPart = slowReverse(arrTime);
         for(int i = 0; i < h ; i ++)
         {
            arrTime[i] = arrTempPart[i];
         }
         h = h << 1;

    }

    return arrTime[];
}

float Wavelet::fourierForward( float timePoints[] )
{
    int m = _waveletArrayLength;
    float arrFreq[] = new float[ m ]; // result

    int n = m >> 1; // half of m

    for( int i = 0; i < n; i++ ) {

      int iR = i * 2;
      int iC = i * 2 + 1;

      arrFreq[ iR ] = 0.;
      arrFreq[ iC ] = 0.;

      float arg = -2. * 3.1415926535 * (float i) / (float n);

      for( int k = 0; k < n; k++ ) {

        int kR = k * 2;
        int kC = k * 2 + 1;

        float cos = cos( k * arg );
        float sin = sin( k * arg );

        arrFreq[ iR ] += timePoints[ kR ] * cos - timePoints[ kC ] * sin;
        arrFreq[ iC ] += timePoints[ kR ] * sin + timePoints[ kC ] * cos;

      }

      arrFreq[ iR ] /= (float)n;
      arrFreq[ iC ] /= (float)n;

    }

    return arrFreq[];

}

  /**
   * The 1-D reverse version of the Discrete Fourier Transform (DFT); The input
   * array arrFreq is organized by real and imaginary parts of a complex number
   * using even and odd places for the index. For example: arrTime[ 0 ] = real1,
   * arrTime[ 1 ] = imag1, arrTime[ 2 ] = real2, arrTime[ 3 ] = imag2, ... The
   * output arrTime is organized by the same scheme.
   *
   * @date 25.03.2010 19:56:29
   * @author Christian Scheiblich (cscheiblich@gmail.com)
   * @throws JWaveException
   * @see jwave.transforms.BasicTransform#reverse(float[])
   */
float Wavelet::fourierReverse( float freqPoints[] )
{
    int m = _waveletArrayLength;
    float arrTime[] = new float[ m ]; // result

    int n = m >> 1; // half of m

    for( int i = 0; i < n; i++ )
    {
      int iR = i * 2;
      int iC = i * 2 + 1;

      arrTime[ iR ] = 0.;
      arrTime[ iC ] = 0.;

      float arg = 2. * 3.1415926535 * (float)i / (float)n;

      for( int k = 0; k < n; k++ )
      {
        int kR = k * 2;
        int kC = k * 2 + 1;

        float cos = cos( k * arg );
        float sin = sin( k * arg );

        arrTime[ iR ] += freqPoints[ kR ] * cos - freqPoints[ kC ] * sin;
        arrTime[ iC ] += freqPoints[ kR ] * sin + freqPoints[ kC ] * cos;

      }

    }

    return arrTime[];

}

int Wavelet::getScalingLength()
{
    return _motherWavelength;
}

void Wavelet::setScalingLength(int scaleLength)
{
    _motherWavelength = scaleLength;

    _scalingDeCom[] = new float[ _motherWavelength ];
}

float Wavelet::saveScaling()
{
    return _scalingDeCom[];
}
void Wavelet::setScaling(float scalingDeCom[])
{
    for( int s = 0; s < _motherWavelength; s++)
    {
        _scalingDeCom[s] = scalingDeCom[s];
    }
    buildOrthonormalSpace();
}


void Wavelet::buildOrthonormalSpace()
{
    _waveletDeCom[] = new float[ _motherWavelength ];
    for( int i = 0; i < _motherWavelength; i++ )
    {
        if( i % 2 == 0 )
        {
            _waveletDeCom[ i ] = _scalingDeCom[ ( _motherWavelength - 1 ) - i ];
        }else{
            _waveletDeCom[ i ] = -_scalingDeCom[ ( _motherWavelength - 1 ) - i ];
        }

    }
    // Copy to reconstruction filters due to orthogonality (orthonormality)!
    _scalingReCon[] = new float[ _motherWavelength ];
    _waveletReCon[] = new float[ _motherWavelength ];
    for( int i = 0; i < _motherWavelength; i++ )
    {
        _scalingReCon[ i ] = _scalingDeCom[ i ];
        _waveletReCon[ i ] = _waveletDeCom[ i ];
    }
}