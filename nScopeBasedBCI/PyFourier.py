import math

# instead use the following: from scipy.fftpack import fft, ifft
def forward(time_points):
    m = len(time_points)
    arr_freq = [None]*len(time_points)
    n = m >> 1
    for i in range(0, n, 1):
        ir = i * 2
        ic = i * 2 + 1
        arr_freq[ir] = 0.
        arr_freq[ic] = 0.
        arg = -2. * 3.1415926535 * float(i) / float(n)
        for k in range(0, n, 1):
            kr = k * 2
            kc = k * 2 + 1
            cos = math.cos(k*arg)
            sin = math.sin(k*arg)
            arr_freq[ir] += time_points[kr] * cos - time_points[kc] * sin
            arr_freq[ic] += time_points[kr] * sin + time_points[kc] * cos
        arr_freq[ir] /= float(n)
        arr_freq[ic] /= float(n)
    return arr_freq


def reverse(freq_points):
    m = len(freq_points)
    arr_time = [None]*len(freq_points)
    n = m >> 1
    for i in range(0, n, 1):
        ir = i * 2
        ic = i * 2 + 1
        arr_time[ir] = 0.
        arr_time[ic] = 0.
        arg = 2. * 3.1415926535 * float(i) / float(n)
        for k in range(0, n, 1):
            kr = k * 2
            kc = k * 2 + 1
            cos = math.cos(k*arg)
            sin = math.sin(k*arg)
            arr_time[ir] += freq_points[kr] * cos - freq_points[kc] * sin
            arr_time[ic] += freq_points[kr] * sin + freq_points[kc] * cos
    return arr_time

