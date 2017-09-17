
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.fftpack import fft, ifft
import pywt
import math

ones = np.ones(1024)

# Set up to reflect 0-17 points of Action Pulse


class APFilterBank(object):

    @ property
    def filter_bank(self):
        dec_lo = [None]*18
        dec_lo[0] = 0
        dec_lo[1] = 0.0006197808889855868
        dec_lo[2] = -0.013271967781817119
        dec_lo[3] = -0.01152821020767923
        dec_lo[4] = 0.03022487885827568
        dec_lo[5] = 0.0005834627461258068
        dec_lo[6] = -0.05456895843083407
        dec_lo[7] = 0.238760914607303
        dec_lo[8] = 0.717897082764412
        dec_lo[9] = 0.6173384491409358
        dec_lo[10] = 0.035272488035271894
        dec_lo[11] = -0.19155083129728512
        dec_lo[12] = -0.018233770779395985
        dec_lo[13] = 0.06207778930288603
        dec_lo[14] = 0.008859267493400484
        dec_lo[15] = -0.010264064027633142
        dec_lo[16] = -0.0004731544986800831
        dec_lo[17] = 0.0010694900329086053
        dec_hi, rec_lo, rec_hi = [None]*18

        for i in range(0, 18):
            if i % 2 == 0:
                dec_hi[i] = dec_lo[18 - 1 - i]
            else:
                dec_hi[i] = -dec_lo[18 - 1 - i]
        for i in range(0, 18):
            rec_lo[i] = dec_lo[17-i]
            rec_hi[i] = dec_hi[17-i]
        return [dec_lo, dec_hi, rec_lo, rec_hi]

filter_bank = APFilterBank()
myAPWavelet = pywt.Wavelet(name="myAPWavelet", filter_bank=filter_bank)
