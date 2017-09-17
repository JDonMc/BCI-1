import math

# instead use import pywt
class Wavelet:
    def __init__(self, wavelet_array_length):
        self.wavelet_array_length = wavelet_array_length
        self.max_level = round(math.log(wavelet_array_length) / math.log(2.))
        self.transform_wave_length = 2
        self.mother_wave_length = 18
        self.scaling_de_com = [None]*self.mother_wave_length
        self.scaling_de_com[0] = 0.0014009155259146807
        self.scaling_de_com[1] = 0.0006197808889855868
        self.scaling_de_com[2] = -0.013271967781817119
        self.scaling_de_com[3] = -0.01152821020767923
        self.scaling_de_com[4] = 0.03022487885827568
        self.scaling_de_com[5] = 0.0005834627461258068
        self.scaling_de_com[6] = -0.05456895843083407
        self.scaling_de_com[7] = 0.238760914607303
        self.scaling_de_com[8] = 0.717897082764412
        self.scaling_de_com[9] = 0.6173384491409358
        self.scaling_de_com[10] = 0.035272488035271894
        self.scaling_de_com[11] = -0.19155083129728512
        self.scaling_de_com[12] = -0.018233770779395985
        self.scaling_de_com[13] = 0.06207778930288603
        self.scaling_de_com[14] = 0.008859267493400484
        self.scaling_de_com[15] = -0.010264064027633142
        self.scaling_de_com[16] = -0.0004731544986800831
        self.scaling_de_com[17] = 0.0010694900329086053
        self.wavelet_de_com = [None]*18
        self.wavelet_re_con = [None]*18
        self.scaling_re_con = [None]*18
        self.build_orthonormal_space()

    def forward(self, time_points): # how do I include the level?
        arr_hilbert = [None]*len(time_points)
        h = self.wavelet_array_length >> 1
        for i in range(0, h, 1):
            arr_hilbert[i] = 0.  # why is this setting to zero again?
            arr_hilbert[i+h] = 0.
            for j in range(0, self.mother_wave_length, 1):
                k = i << 1
                while k >= self.wavelet_array_length:
                    k -= self.wavelet_array_length
                arr_hilbert[i] += time_points[k] * self.scaling_de_com[j]
                arr_hilbert[i+h] += time_points[k] * self.wavelet_de_com[j]
        return arr_hilbert

    def reverse(self, hilbert_points):
        arr_time = [None]*len(hilbert_points)
        for i in range(0, self.wavelet_array_length, 1):
            arr_time[i] = 0.
        h = self.wavelet_array_length >> 1
        for i in range(0, h, 1):
            for j in range(0, self.mother_wave_length, 1):
                k = (i << 1) + j
                while k >= self.wavelet_array_length:
                    k -= self.wavelet_array_length
                arr_time[k] += (hilbert_points[i] * self.scaling_re_con[j]) + \
                               (hilbert_points[i+h] * self.wavelet_re_con[j])
        return arr_time

    def get_scaling_length(self):
        return self.mother_wave_length

    def set_scaling_length(self, scale_length):
        self.mother_wave_length = scale_length
        self.scaling_de_com = [None]*self.mother_wave_length

    def save_scaling(self):
        return self.scaling_de_com

    def set_scaling(self, scaling):
        for s in range(0, self.mother_wave_length, 1):
            self.scaling_de_com[s] = scaling[s]
        self.build_orthonormal_space()

    def build_orthonormal_space(self):
        self.wavelet_de_com = [None]*self.mother_wave_length
        for i in range(0, self.mother_wave_length, 1):
            if i % 2 == 0:
                self.wavelet_de_com[i] = self.scaling_de_com[self.mother_wave_length-1-i]
            else:
                self.wavelet_de_com[i] = -self.scaling_de_com[self.mother_wave_length - 1 - i]
        self.scaling_re_con = [None]*self.mother_wave_length
        self.wavelet_re_con = [None]*self.mother_wave_length
        for i in range(0, self.mother_wave_length, 1):
            self.scaling_re_con[i] = self.scaling_de_com[i]
            self.wavelet_re_con[i] = self.wavelet_de_com[i]

