
#Currently python pseudo code. needs to be written in arduino for the controller.
#Depends, will Arduino (M4) function as a feeder for a program on A9 python?
#Perhaps I can get both working, compare speeds, optimise. Rational approach.

method runningcircuit
if (runningcircuit.type() == "asynchronous")
    n = 1 # length of step, dependent on computation time.
    while(int i = length(voltage[]); i > 0; i--):
        if i
        voltage[i] = voltage[i-n]
    voltage[0] = read.input()
    #shift array and implement after a single step (To be used immediately, may )
    runningcircuit.run()

else# synchronous
    for i in length(voltage[]) # length of a snapshot
        voltgae[i] = read.input()

    runningcircuit.run()



public double[ ] forward( double[ ] arrTime, int arrTimeLength ) {

    double[ ] arrHilb = new double[ arrTimeLength ];

    int h = arrHilb.length >> 1; // .. -> 8 -> 4 -> 2 .. shrinks in each step by half wavelength
    for( int i = 0; i < h; i++ ) {

      arrHilb[ i ] = arrHilb[ i + h ] = 0.; // set to zero before sum up

      for( int j = 0; j < _motherWavelength; j++ ) {

        int k = ( i << 1 ) + j; // k = ( i * 2 ) + j;
        while( k >= arrHilb.length )
          k -= arrHilb.length; // circulate over arrays if scaling and wavelet are are larger

        arrHilb[ i ] += arrTime[ k ] * _scalingDeCom[ j ]; // low pass filter for the energy (approximation)
        arrHilb[ i + h ] += arrTime[ k ] * _waveletDeCom[ j ]; // high pass filter for the details

      } // Sorting each step in patterns of: { scaling coefficients | wavelet coefficients }

    } // h = 2^(p-1) | p = { 1, 2, .., N } .. shrinks in each step by half wavelength

    return arrHilb;

  } // forward


public class Symlet9 extends Wavelet {

  /**
   * Already orthonormal coefficients taken from Filip Wasilewski's webpage
   * http://wavelets.pybytes.com/wavelet/sym9/ Thanks!
   *
   * @author Christian Scheiblich (cscheiblich@gmail.com)
   * @date 17.08.2014 14:31:46
   */
  public Symlet9( ) {

    _name = "Symlet 9"; // name of the wavelet

    _transformWavelength = 2; // minimal wavelength of input signal

    _motherWavelength = 18; // wavelength of mother wavelet

    _scalingDeCom = new double[ _motherWavelength ];
    _scalingDeCom[ 0 ] = 0.0014009155259146807;
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

    _buildOrthonormalSpace( );

  } // Symlet9

} // Symlet9


#Above is symlet 9


namespace TurboWavelets
{
	public class Biorthogonal53Wavelet1DStatic
	{
		/// <summary>
		/// A fast implementation of a 1 dimensional biorthogonal 5/3 wavelet transformation
		/// for arbitary lenghts (works for all sizes, not just power of 2)
		/// using the lifting scheme.
		/// </summary>
		/// <param name="src">The source values which should be transformed</param>
		/// <param name="dst">The resulting values after the transformation</param>
		/// <returns>None</returns>
		public static void wavelet53_1d (float[] src, float[] dst, int length)
		{
			if (length >= 3) {
				int half = length >> 1;
				//if the length is even then subtract 1 from "half"
				//as there is the same number of low and high frequency values
				//(Note that "num_lf_values" is equal to "half+1")
				//For a odd length there is one additional low frequency value (so do not subtract 1)
				//"half" is one less than "num_lf_values" as we cannot directly
				//calculate the last value in the for-loop (array bounds)
				if ((length & 1) == 0)
					half--;
				int offsrc = 0;
				// starting offset for high frequency values (= number of low frequency values)
				int offdst = half + 1;
				int num_lf_values = offdst;

				float last_hf = 0.0f;
				for (int i = 0; i < half; i++) {
					//calculate the high frequency value by
					//subtracting the mean of the immediate neighbors for every second value
					float hf = src [offsrc + 1] - (src [offsrc] + src [offsrc + 2]) * 0.5f;
					//smoothing the low frequency value, scale by factor 2
					//(instead of scaling low frequencies by factor sqrt(2) and
					//shrinking high frequencies by factor sqrt(2)
					//and reposition to have all low frequencies on the left side
					dst [i] = 2.0f * (src [offsrc] + (last_hf + hf) * 0.25f);
					dst [offdst++] = hf;
					last_hf = hf;
					offsrc += 2;
				}
				if ((length & 1) == 0) {
					//the secound last value in the array is our last low frequency value
					dst [num_lf_values - 1] = src [length - 2];
					//the last value is a high frequency value
					//however here we just subtract the previos value (so not really a
					//biorthogonal 5/3 transformation)
					//This is done because the 5/3 wavelet cannot be calculated at the boundary
					dst [length - 1] = src [length - 1] - src [length - 2];
				} else {
					dst [num_lf_values - 1] = src [length - 1];
				}
			} else {
				//We cannot perform the biorthogonal 5/3 wavelet transformation
				//for lengths smaller than 3. We could do a simpler transformation...
				//Here however, we just copy the values from the source to the destination array
				for (int i = 0; i < length; i++)
					dst [i] = src [i];
			}
		}

		/// <summary>
		/// A fast implementation of a 1 dimensional biorthogonal 5/3 wavelet back-transformation
		/// for arbitary lenghts (works for all sizes, not just power of 2)
		/// using the lifting scheme.
		/// </summary>
		/// <param name="src">The source values which should be back-transformed</param>
		/// <param name="dst">The resulting values after the back-transformation</param>
		/// <returns>None</returns>
		public static void wavelet53_1d_inverse (float[] src, float[] dst, int length)
		{
			if (length >= 3) {
				int half = length >> 1;
				//if the length is even then subtract 1 from "half"
				//as there is the same number of low and high frequency values
				//(Note that "num_lf_values" is equal to "half+1")
				//For a odd length there is one additional low frequency value (so do not subtract 1)
				//"half" is one less than "num_lf_values" as we cannot directly
				//calculate the last value in the for-loop (array bounds)
				if ((length & 1) == 0)
					half--;
				// number of low frequency values
				int num_lf_values = half + 1;

				float last_lf = 0.5f * src [0] - src [num_lf_values] * 0.25f;
				float last_hf = src [num_lf_values];
				//Calculate the first two values outside the for loop (array bounds)
				dst [0] = last_lf;
				dst [1] = last_hf + last_lf * 0.5f;
				for (int i = 1; i < half; i++) {
					float hf = src [num_lf_values + i];
					float lf = 0.5f * src [i];
					//reconstruct the original value by removing the "smoothing"
					float lf_reconst = lf - (hf + last_hf) * 0.25f;
					dst [2 * i] = lf_reconst;
					//add reconstructed low frequency value (left side) and high frequency value
					dst [2 * i + 1] = lf_reconst * 0.5f + hf;
					//add other low frequency value (right side)
					//This must be done one iteration later, as the
					//reconstructed values is not known earlier
					dst [2 * i - 1] += lf_reconst * 0.5f;
					last_hf = hf;
					last_lf = lf_reconst;
				}

				if ((length & 1) == 0) {
					//restore the last 3 values outside the for loop
					//adding the missing low frequency value (right side)
					dst [length - 3] += src [num_lf_values - 1] * 0.5f;
					//copy the last low frequency value
					dst [length - 2] = src [num_lf_values - 1];
					//restore the last value by adding last low frequency value
					dst [length - 1] = src [length - 1] + src [num_lf_values - 1];
				} else {
					//restore the last 2 values outside the for loop
					//adding the missing low frequency value (right side)
					dst [length - 2] += src [num_lf_values - 1] * 0.5f;
					//copy the last low frequency value
					dst [length - 1] = src [num_lf_values - 1];
				}
			} else {
				//We cannot perform the biorthogonal 5/3 wavelet transformation
				//for lengths smaller than 3. We could do a simpler transformation...
				//Here however, we just copy the values from the source to the destination array
				for (int i = 0; i < length; i++)
					dst [i] = src [i];
			}
		}
	}
}


public


class FastWaveletTransform extends WaveletTransform {

/ **
* Constructor receiving a Wavelet object and setting identifier of transform.
*
* @ date 10.02.2010 08:10

:42
 * @ author
Christian
Scheiblich(cscheiblich @ gmail.com)
* @ param
wavelet
* object
of
type
Wavelet
* /
public
FastWaveletTransform(Wavelet
wavelet ) {

    super(wavelet);
_name = "Fast Wavelet Transform"; // set
identifier
of
transform;
keep
constant

} // FastWaveletTransform

     / **
*Performs
a
1 - D
forward
transform
from time domain

to
Hilbert
domain
using
* one
kind
of
a
Fast
Wavelet
Transform(FWT)
algorithm
for a given array of
* dimension (length) 2 ^ p | pEN; N = 2, 4, 8, 16, 32, 64, 128, .., and so on.
* However, the algorithms stops for a supported level that has be in the
* range 0, .., p of the dimension of the input array; 0 is the time series
* itself and p is the maximal number of possible levels.
*
* @ author Christian Scheiblich (cscheiblich @ gmail.com)
* @ date 22.03.2015 11:58:37
                          * @ throws
JWaveException
* if given
array is not of
length
2 ^ p | pEN or given
level
does
not
*match
the
supported
domain(array)
* @ see
jwave.transforms.BasicTransform  # forward(double[], int)
* /
@ Override
public
double[]
forward(double[]
arrTime, int
level )
throws
JWaveException
{

if ( !isBinary(arrTime.length) )
throw
new
JWaveFailure(
    "FastWaveletTransform#forward - "
    + "given array length is not 2^p | p E N ... = 1, 2, 4, 8, 16, 32, .. "
    + "please use the Ancient Egyptian Decomposition for any other array length!");

int
noOfLevels = calcExponent(arrTime.length);
if (level < 0 | | level > noOfLevels)
throw
new
JWaveFailure("FastWaveletTransform#forward - "
             + "given level is out of range for given array");

double[]
arrHilb = Arrays.copyOf(arrTime, arrTime.length);

int
l = 0;
int
h = arrHilb.length;
int
transformWavelength = _wavelet.getTransformWavelength(); // normally
2
while (h >= transformWavelength & & l < level) {

double[] arrTempPart = _wavelet.forward( arrHilb, h );
System.arraycopy( arrTempPart, 0, arrHilb, 0, h );
h = h >> 1;
l++;

} // levels

return arrHilb;

} // forward

     / **
*Performs
a
1 - D
reverse
transform
from Hilbert domain

to
time
domain
using
* one
kind
of
a
Fast
Wavelet
Transform(FWT)
algorithm
for a given array of
* dimension (length) 2 ^ p | pEN; N = 2, 4, 8, 16, 32, 64, 128, .., and so on.
* However, the algorithms starts for at a supported level that has be in the
* range 0, .., p of the dimension of the input array; 0 is the time series
* itself and p is the maximal number of possible levels.The coefficients of
* the input array have to match to the supported level.
*
* @ author Christian Scheiblich (cscheiblich @ gmail.com)
* @ date 22.03.2015 12:00:10
                          * @ throws
JWaveException
* if given
array is not of
length
2 ^ p | pEN or given
level
does
not
*match
the
supported
domain(array)
* @ see
jwave.transforms.BasicTransform  # reverse(double[], int)
* /
@ Override
public
double[]
reverse(double[]
arrHilb, int
level )
throws
JWaveException
{

if ( !isBinary( arrHilb.length ) )
throw
new
JWaveFailure(
    "FastWaveletTransform#reverse - "
    + "given array length is not 2^p | p E N ... = 1, 2, 4, 8, 16, 32, .. "
    + "please use the Ancient Egyptian Decomposition for any other array length!");

int
noOfLevels = calcExponent(arrHilb.length);
if (level < 0 | | level > noOfLevels)
    throw
    new
    JWaveFailure("FastWaveletTransform#reverse - "
                 + "given level is out of range for given array");

int
length = arrHilb.length; // length
of
first
Hilbert
space
double[]
arrTime = Arrays.copyOf(arrHilb, length);

int
transformWavelength = _wavelet.getTransformWavelength(); // normally
2
int
h = transformWavelength;

int
steps = calcExponent(length);
for (int l = level; l < steps; l++ )
h = h << 1; // begin
reverse
transform
at
certain - matching - level
of
Hilbert
space

while (h <= arrTime.length & & h >= transformWavelength) {

double[] arrTempPart = _wavelet.reverse( arrTime, h );
System.arraycopy( arrTempPart, 0, arrTime, 0, h );
h = h << 1;

} // levels

return arrTime;

} // reverse

} // FastWaveletTransfrom



#https://github.com/codeprof/TurboWavelets.Net/blob/master/TurboWavelets/Biorthogonal53Wavelet1DStatic.cs
namespace TurboWavelets
{
	public class Biorthogonal53Wavelet1DStatic
	{
		/// <summary>
		/// A fast implementation of a 1 dimensional biorthogonal 5/3 wavelet transformation
		/// for arbitary lenghts (works for all sizes, not just power of 2)
		/// using the lifting scheme.
		/// </summary>
		/// <param name="src">The source values which should be transformed</param>
		/// <param name="dst">The resulting values after the transformation</param>
		/// <returns>None</returns>
		public static void wavelet53_1d (float[] src, float[] dst, int length)
		{
			if (length >= 3) {
				int half = length >> 1;
				//if the length is even then subtract 1 from "half"
				//as there is the same number of low and high frequency values
				//(Note that "num_lf_values" is equal to "half+1")
				//For a odd length there is one additional low frequency value (so do not subtract 1)
				//"half" is one less than "num_lf_values" as we cannot directly
				//calculate the last value in the for-loop (array bounds)
				if ((length & 1) == 0)
					half--;
				int offsrc = 0;
				// starting offset for high frequency values (= number of low frequency values)
				int offdst = half + 1;
				int num_lf_values = offdst;

				float last_hf = 0.0f;
				for (int i = 0; i < half; i++) {
					//calculate the high frequency value by
					//subtracting the mean of the immediate neighbors for every second value
					float hf = src [offsrc + 1] - (src [offsrc] + src [offsrc + 2]) * 0.5f;
					//smoothing the low frequency value, scale by factor 2
					//(instead of scaling low frequencies by factor sqrt(2) and
					//shrinking high frequencies by factor sqrt(2)
					//and reposition to have all low frequencies on the left side
					dst [i] = 2.0f * (src [offsrc] + (last_hf + hf) * 0.25f);
					dst [offdst++] = hf;
					last_hf = hf;
					offsrc += 2;
				}
				if ((length & 1) == 0) {
					//the secound last value in the array is our last low frequency value
					dst [num_lf_values - 1] = src [length - 2];
					//the last value is a high frequency value
					//however here we just subtract the previos value (so not really a
					//biorthogonal 5/3 transformation)
					//This is done because the 5/3 wavelet cannot be calculated at the boundary
					dst [length - 1] = src [length - 1] - src [length - 2];
				} else {
					dst [num_lf_values - 1] = src [length - 1];
				}
			} else {
				//We cannot perform the biorthogonal 5/3 wavelet transformation
				//for lengths smaller than 3. We could do a simpler transformation...
				//Here however, we just copy the values from the source to the destination array
				for (int i = 0; i < length; i++)
					dst [i] = src [i];
			}
		}

		/// <summary>
		/// A fast implementation of a 1 dimensional biorthogonal 5/3 wavelet back-transformation
		/// for arbitary lenghts (works for all sizes, not just power of 2)
		/// using the lifting scheme.
		/// </summary>
		/// <param name="src">The source values which should be back-transformed</param>
		/// <param name="dst">The resulting values after the back-transformation</param>
		/// <returns>None</returns>
		public static void wavelet53_1d_inverse (float[] src, float[] dst, int length)
		{
			if (length >= 3) {
				int half = length >> 1;
				//if the length is even then subtract 1 from "half"
				//as there is the same number of low and high frequency values
				//(Note that "num_lf_values" is equal to "half+1")
				//For a odd length there is one additional low frequency value (so do not subtract 1)
				//"half" is one less than "num_lf_values" as we cannot directly
				//calculate the last value in the for-loop (array bounds)
				if ((length & 1) == 0)
					half--;
				// number of low frequency values
				int num_lf_values = half + 1;

				float last_lf = 0.5f * src [0] - src [num_lf_values] * 0.25f;
				float last_hf = src [num_lf_values];
				//Calculate the first two values outside the for loop (array bounds)
				dst [0] = last_lf;
				dst [1] = last_hf + last_lf * 0.5f;
				for (int i = 1; i < half; i++) {
					float hf = src [num_lf_values + i];
					float lf = 0.5f * src [i];
					//reconstruct the original value by removing the "smoothing"
					float lf_reconst = lf - (hf + last_hf) * 0.25f;
					dst [2 * i] = lf_reconst;
					//add reconstructed low frequency value (left side) and high frequency value
					dst [2 * i + 1] = lf_reconst * 0.5f + hf;
					//add other low frequency value (right side)
					//This must be done one iteration later, as the
					//reconstructed values is not known earlier
					dst [2 * i - 1] += lf_reconst * 0.5f;
					last_hf = hf;
					last_lf = lf_reconst;
				}

				if ((length & 1) == 0) {
					//restore the last 3 values outside the for loop
					//adding the missing low frequency value (right side)
					dst [length - 3] += src [num_lf_values - 1] * 0.5f;
					//copy the last low frequency value
					dst [length - 2] = src [num_lf_values - 1];
					//restore the last value by adding last low frequency value
					dst [length - 1] = src [length - 1] + src [num_lf_values - 1];
				} else {
					//restore the last 2 values outside the for loop
					//adding the missing low frequency value (right side)
					dst [length - 2] += src [num_lf_values - 1] * 0.5f;
					//copy the last low frequency value
					dst [length - 1] = src [num_lf_values - 1];
				}
			} else {
				//We cannot perform the biorthogonal 5/3 wavelet transformation
				//for lengths smaller than 3. We could do a simpler transformation...
				//Here however, we just copy the values from the source to the destination array
				for (int i = 0; i < length; i++)
					dst [i] = src [i];
			}
		}
	}
}






#https://github.com/sumito3478/wavelet-audio-compression-example/blob/master/src/main/scala/info/sumito3478/dwt97.scala
package object dwt97 {
  import scalaxy.loops._
  import scala.language.postfixOps
  import scala.collection._

  def fwt97(xs: mutable.IndexedSeq[Double]) = {
    val a1 = -1.586134342
    val a2 = -0.05298011854
    val a3 = 0.8829110762
    val a4 = 0.4435068522
    val k1 = 0.81289306611596146
    val k2 = 0.61508705245700002
    val n = xs.length
    // Predict 1
    for (i <- 1 until n - 2 by 2 optimized)
      xs(i) += a1 * (xs(i - 1) + xs(i + 1))
    xs(n - 1) += 2 * a1 * xs(n - 2)
    // Update 1
    for (i <- 2 until n by 2 optimized)
      xs(i) += a2 * (xs(i - 1) + xs(i + 1))
    xs(0) += 2 * a2 * xs(1)
    // Predict 2
    for (i <- 1 until n - 2 by 2 optimized)
      xs(i) += a3 * (xs(i - 1) + xs(i + 1))
    xs(n - 1) += 2 * a3 * xs(n - 2)
    // Update 2
    for (i <- 2 until n by 2 optimized)
      xs(i) += a4 * (xs(i - 1) + xs(i + 1))
    xs(0) += 2 * a4 * xs(1)
    // Scale and pack
    val tmp = new Array[Double](n)
    for (i <- 0 until n / 2 optimized) {
      tmp(i) = k1 * xs(i * 2)
      tmp(n / 2 + i) = k2 * xs(i * 2 + 1)
    }
    for (i <- 0 until n optimized) {
      xs(i) = tmp(i)
    }
  }

  def iwt97(xs: mutable.IndexedSeq[Double]) = {
    val a1 = 1.586134342
    val a2 = 0.05298011854
    val a3 = -0.8829110762
    val a4 = -0.4435068522
    val k1 = 1.230174104914
    val k2 = 1.6257861322319229
    val n = xs.length
    // Unpack and Undo Scale
    val tmp = new Array[Double](n)
    for (i <- 0 until n / 2 optimized) {
      tmp(i * 2) = k1 * xs(i)
      tmp(i * 2 + 1) = k2 * xs(n / 2 + i)
    }
    for (i <- 0 until n optimized) {
      xs(i) = tmp(i)
    }
    // Undo update 2
    for (i <- 2 until n by 2 optimized) {
      xs(i) += a4 * (xs(i - 1) + xs(i + 1))
    }
    xs(0) += 2 * a4 * xs(1)
    // Undo predict 2
    for (i <- 1 until n - 2 by 2 optimized) {
      xs(i) += a3 * (xs(i - 1) + xs(i + 1))
    }
    xs(n - 1) += 2 * a3 * xs(n - 2)
    // Undo update 1
    for (i <- 2 until n by 2 optimized) {
      xs(i) += a2 * (xs(i - 1) + xs(i + 1))
    }
    xs(0) += 2 * a2 * xs(1)
    // Undo predict 1
    for (i <- 1 until n - 2 by 2 optimized) {
      xs(i) += a1 * (xs(i - 1) + xs(i + 1))
    }
    xs(n - 1) += 2 * a1 * xs(n - 2)
  }
}



#https://github.com/VadimKirilchuk/jawelet/wiki/CDF-9-7-Discrete-Wavelet-Transform
/ **
*dwt97.c - Fast
discrete
biorthogonal
CDF
9 / 7
wavelet
forward and inverse
transform(lifting
implementation)
*
* This
code is provided
"as is" and is given
for educational purposes.
        * 2006 - Gregoire Pau - gregoire.pau @ ebi.ac.uk
* /

# include <stdio.h>
# include <stdlib.h>

double * tempbank=0;

/ **
* fwt97 - Forward biorthogonal 9 / 7 wavelet transform (lifting implementation)
*
* x is an input signal, which will be replaced by its output transform.
* n is the length of the signal, and must be a power of 2.
*
* The first half part of the output signal contains the approximation coefficients.
* The second half part contains the detail coefficients (aka.the wavelets coefficients).
*
* See also iwt97.
* /
void fwt97(double * x, int n) {
double
a;
int
i;

// Predict
1
a = -1.586134342;
for (i=1;i < n-2;i += 2) {
x[i] += a * (x[i-1]+x[i+1]);
}
x[n - 1] += 2 * a * x[n - 2];

// Update
1
a = -0.05298011854;
for (i=2;i < n;i += 2) {
x[i] += a * (x[i-1]+x[i+1]);
}
x[0] += 2 * a * x[1];

// Predict
2
a = 0.8829110762;
for (i=1;i < n-2;i += 2) {
x[i] += a * (x[i-1]+x[i+1]);
}
x[n - 1] += 2 * a * x[n - 2];

// Update
2
a = 0.4435068522;
for (i=2;i < n;i += 2) {
x[i] += a * (x[i-1]+x[i+1]);
}
x[0] += 2 * a * x[1];

// Scale
a = 1 / 1.149604398;
for (i=0;i < n;i++) {
if (i % 2) x[i] *= a;
else x[i] /= a;
}

// Pack
if (tempbank == 0) tempbank=(double * )malloc(n * sizeof(double));
for (i=0;i < n;i++) {
if (i % 2 == 0) tempbank[i / 2]=x[i];
else tempbank[n / 2+i / 2]=x[i];
}
for (i=0;i < n;i++) x[i]=tempbank[i];
}

/ **
*iwt97 - Inverse
biorthogonal
9 / 7
wavelet
transform
*
* This is the
inverse
of
fwt97
so
that
iwt97(fwt97(x, n), n) = x
for every signal x of length n.
*
* See also fwt97.
* /
void iwt97(double * x, int n) {
double
a;
int
i;

// Unpack
if (tempbank == 0) tempbank=(double * )malloc(n * sizeof(double));
for (i=0;i < n / 2;i++) {
tempbank[i * 2]=x[i];
tempbank[i * 2+1]=x[i+n / 2];
}
for (i=0;i < n;i++) x[i]=tempbank[i];

// Undo
scale
a = 1.149604398;
for (i=0;i < n;i++) {
if (i % 2) x[i] *= a;
else x[i] /= a;
}

// Undo
update
2
a = -0.4435068522;
for (i=2;i < n;i += 2) {
x[i] += a * (x[i-1]+x[i+1]);
}
x[0] += 2 * a * x[1];

// Undo
predict
2
a = -0.8829110762;
for (i=1;i < n-2;i += 2) {
x[i] += a * (x[i-1]+x[i+1]);
}
x[n - 1] += 2 * a * x[n - 2];

// Undo
update
1
a = 0.05298011854;
for (i=2;i < n;i += 2) {
x[i] += a * (x[i-1]+x[i+1]);
}
x[0] += 2 * a * x[1];

// Undo
predict
1
a = 1.586134342;
for (i=1;i < n-2;i += 2) {
x[i] += a * (x[i-1]+x[i+1]);
}
x[n - 1] += 2 * a * x[n - 2];
}

int
main()
{
double
x[32];
int
i;

// Makes
a
fancy
cubic
signal
for (i=0;i < 32;i++) x[i]=5+i+0.4 * i * i-0.02 * i * i * i;

// Prints
original
sigal
x
printf("Original signal:\n");
for (i=0;i < 32;i++) printf("x[%d]=%f\n", i, x[i]);
printf("\n");

// Do
the
forward
9 / 7
transform
fwt97(x, 32);

// Prints
the
wavelet
coefficients
printf("Wavelets coefficients:\n");
for (i=0;i < 32;i++) printf("wc[%d]=%f\n", i, x[i]);
printf("\n");

// Do
the
inverse
9 / 7
transform
iwt97(x, 32);

// Prints
the
reconstructed
signal
printf("Reconstructed signal:\n");
for (i=0;i < 32;i++) printf("xx[%d]=%f\n", i, x[i]);
}
