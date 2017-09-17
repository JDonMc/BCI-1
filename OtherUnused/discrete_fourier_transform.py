


read(file)

def discrete_fourier_transform(xn):
    N = length(xn)
    K = N
    fourier[0::K] = 0
    for k in K:
        cissum = 0
        for n in N:
            cissum += xn[n]*(cos(-2*pi()*k*n/N)+i*sin(2*pi()*k*n/N))
        fourier[k] = cissum
    return fourier



def inverse_discrete_fourier_transform(fourier):
    N = length(fourier)
    K = N
    original[0::K] = 0
    for k in K:
        cissum = 0
        for n in N:
            cissum += xn[n] * (cos(-2 * pi() * k * n / N) + i * sin(2 * pi() * k * n / N))
        original[k] = cissum
    return original

def discrete_wavelet_transform(original):



    return wavelet

def inverse_discrete_wavelet_transform(wavelet):



    return fourier

