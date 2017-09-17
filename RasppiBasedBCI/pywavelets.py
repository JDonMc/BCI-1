import pywt, math
c = math.sqrt(2)/2
dec_lo, dec_hi, rec_lo, rec_hi = [c, c], [-c, c], [c, c], [c, -c]
filter_bank = [dec_lo, dec_hi, rec_lo, rec_hi]
myWavelet = pywt.Wavelet(name="myHaarWavelet", filter_bank=filter_bank)


class HaarFilterBank(object):
    @property
    def filter_bank(self):
        c = math.sqrt(2)/2
        dec_lo, dec_hi, rec_lo, rec_hi = [c, c], [-c, c], [c, c], [c, -c]
        return [dec_lo, dec_hi, rec_lo, rec_hi]
filter_bank = HaarFilterBank()
myOtherWavelet = pywt.Wavelet(name="myHaarWavelet", filter_bank=filter_bank)


# https://pywavelets.readthedocs.io/en/latest/ref/dwt-discrete-wavelet-transform.html
from pywt import wavedec
coeffs = wavedec([1,2,3,4,5,6,7,8], 'db1', level=2)
cA2, cD2, cD1 = coeffs
cD1
array([-0.70710678, -0.70710678, -0.70710678, -0.70710678])
cD2
array([-2., -2.])
cA2
array([  5.,  13.])

import pywt
import numpy as np
coeffs = pywt.wavedec2(np.ones((4,4)), 'db1')
# Levels:
len(coeffs)-1
pywt.waverec2(coeffs, 'db1')

#https://pywavelets.readthedocs.io/en/latest/ref/nd-dwt-and-idwt.html
pywt.dwtn(data, wavelet, mode, axes)
pywt.wavedecn(data, wavelet, mode, level, axes)
