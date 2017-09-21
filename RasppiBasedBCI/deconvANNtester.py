# https://pywavelets.readthedocs.io/en/latest/#documentation
# https://pywavelets.readthedocs.io/en/latest/ref/wavelets.html#custom-wavelets
# https://pywavelets.readthedocs.io/en/latest/ref/dwt-discrete-wavelet-transform.html
# https://pywavelets.readthedocs.io/en/latest/ref/2d-dwt-and-idwt.html
# https://pywavelets.readthedocs.io/en/latest/ref/nd-dwt-and-idwt.html
# import wavelet transformations
import pywt
# import fourier transformation
import numpy.fft as ft
# import artificial neural network
# https://www.tensorflow.org/
# https://github.com/tensorflow/tensorflow/tree/r1.2
#
import tensorflow as tf
import pickle
import matplotlib.pyplot as plt
# https://matplotlib.org/users/pyplot_tutorial.html
import json
import os
import pandas as pd
# Employing an exorbitant test to find optimal determination algorithms for fingerprinting a human from brain signals.
# __name__ == 'Brian Las Sing'
# Brain Signals


def derivative_aa(x):
    daa = [0] * (len(x)-1)
    for t in range(0, len(x)-1):
        daa[t] = x[t+1]-x[t]
    return daa


def derivative_ab(x):
    dab = [0] * (len(x) - 2)
    for t in range(1, len(x)-1):
        dab[t-1] = x[t+1]-x[t-1]
    return dab


def derivative_ac(x):
    dac = [0] * (len(x) - 1)
    for t in range(1, len(x)):
        dac[t-1] = x[t]-x[t-1]
    return dac
# transform data to max


def daubechies(x):
    waax = pywt.dwt(x, 'db1')
    return waax  # 'wavelet'


def custom_tailless(x, a, b):
    dec_lo = [a, a/2]
    dec_hi = [-b, a]
    rec_lo = [a, a/2]
    rec_hi = [a, -b]
    custom = pywt.Wavelet(name="tail", filter_bank=[dec_lo, dec_hi, rec_lo, rec_hi])
    wbax = pywt.dwt(x, custom)
    wiax = custom.wavefun()
    return wbax


def symlet(x):
    wcax = pywt.dwt(x, 'sym9')
    return wcax


def custom_tail(x, a, b):
    dec_lo = [a, a/2]
    dec_hi = [-b, a]
    rec_lo = [a/2, a]
    rec_hi = [a, -b]
    custom = pywt.Wavelet(name="tail", filter_bank=[dec_lo, dec_hi, rec_lo, rec_hi])
    wdax = pywt.dwt(x, custom)
    wiax = custom.wavefun()
    return wdax


def fourier(x):
    fax = ft.fft(x)
    return fax


def do_something_special(text, n, j):
    # convert the file into data points,
    # perform all operations of functions on data,
    # re-save the data in a new format

    i = -1
    stats = [[0]*256 for _ in range(0, 64)]
    for tex in text:
        if tex.find('#') > -1:
            if tex.find('FP1') > -1:
                i += 1
                m = -1
            elif tex.find('FP2') > -1:
                i += 1
                m = -1
            elif tex.find('F7') > -1:
                i += 1
                m = -1
            elif tex.find('F8') > -1:
                i += 1
                m = -1
            elif tex.find('AF1') > -1:
                i += 1
                m = -1
            elif tex.find('AF2') > -1:
                i += 1
                m = -1
            elif tex.find('FZ') > -1:
                i += 1
                m = -1
            elif tex.find('F4') > -1:
                i += 1
                m = -1
            elif tex.find('F3') > -1:
                i += 1
                m = -1
            elif tex.find('FC6') > -1:
                i += 1
                m = -1
            elif tex.find('FC5') > -1:
                i += 1
                m = -1
            elif tex.find('FC2') > -1:
                i += 1
                m = -1
            elif tex.find('FC1') > -1:
                i += 1
                m = -1
            elif tex.find('T8') > -1:
                i += 1
                m = -1
            elif tex.find('T7') > -1:
                i += 1
                m = -1
            elif tex.find('CZ') > -1:
                i += 1
                m = -1
            elif tex.find('C3') > -1:
                i += 1
                m = -1
            elif tex.find('C4') > -1:
                i += 1
                m = -1
            elif tex.find('CP5') > -1:
                i += 1
                m = -1
            elif tex.find('CP6') > -1:
                i += 1
                m = -1
            elif tex.find('CP1') > -1:
                i += 1
                m = -1
            elif tex.find('CP2') > -1:
                i += 1
                m = -1
            elif tex.find('P3') > -1:
                i += 1
                m = -1
            elif tex.find('P4') > -1:
                i += 1
                m = -1
            elif tex.find('PZ') > -1:
                i += 1
                m = -1
            elif tex.find('P8') > -1:
                i += 1
                m = -1
            elif tex.find('P7') > -1:
                i += 1
                m = -1
            elif tex.find('PO2') > -1:
                i += 1
                m = -1
            elif tex.find('PO1') > -1:
                i += 1
                m = -1
            elif tex.find('O2') > -1:
                i += 1
                m = -1
            elif tex.find('O1') > -1:
                i += 1
                m = -1
            elif tex.find('X') > -1:
                i += 1
                m = -1
            elif tex.find('AF7') > -1:
                i += 1
                m = -1
            elif tex.find('AF8') > -1:
                i += 1
                m = -1
            elif tex.find('F5') > -1:
                i += 1
                m = -1
            elif tex.find('F6') > -1:
                i += 1
                m = -1
            elif tex.find('FT7') > -1:
                i += 1
                m = -1
            elif tex.find('FT8') > -1:
                i += 1
                m = -1
            elif tex.find('FPZ') > -1:
                i += 1
                m = -1
            elif tex.find('FC4') > -1:
                i += 1
                m = -1
            elif tex.find('FC3') > -1:
                i += 1
                m = -1
            elif tex.find('C6') > -1:
                i += 1
                m = -1
            elif tex.find('C5') > -1:
                i += 1
                m = -1
            elif tex.find('F2') > -1:
                i += 1
                m = -1
            elif tex.find('F1') > -1:
                i += 1
                m = -1
            elif tex.find('TP8') > -1:
                i += 1
                m = -1
            elif tex.find('TP7') > -1:
                i += 1
                m = -1
            elif tex.find('AFZ') > -1:
                i += 1
                m = -1
            elif tex.find('CP3') > -1:
                i += 1
                m = -1
            elif tex.find('CP4') > -1:
                i += 1
                m = -1
            elif tex.find('P5') > -1:
                i += 1
                m = -1
            elif tex.find('P6') > -1:
                i += 1
                m = -1
            elif tex.find('C1') > -1:
                i += 1
                m = -1
            elif tex.find('C2') > -1:
                i += 1
                m = -1
            elif tex.find('PO7') > -1:
                i += 1
                m = -1
            elif tex.find('PO8') > -1:
                i += 1
                m = -1
            elif tex.find('FCZ') > -1:
                i += 1
                m = -1
            elif tex.find('POZ') > -1:
                i += 1
                m = -1
            elif tex.find('OZ') > -1:
                i += 1
                m = -1
            elif tex.find('P2') > -1:
                i += 1
                m = -1
            elif tex.find('P1') > -1:
                i += 1
                m = -1
            elif tex.find('CPZ') > -1:
                i += 1
                m = -1
            elif tex.find('nd') > -1:
                i += 1
                m = -1
            elif tex.find('Y') > -1:
                i += 1
                m = -1
        else:
            m += 1
            te = tex.split()
            stats[i][m] = float(te[3])
    for k in range(0, 64):
        for l in range(10):
            if l == 0:
                statist = custom_tail(stats[k], 0.9, 0.9)
                statistics = statist[0].tolist() + statist[1].tolist()
            if l == 1:
                statistics = stats[k]
            if l == 2:
                statist = custom_tail(stats[k], 0.8, 0.8)
                statistics = statist[0].tolist() + statist[1].tolist()
            if l == 3:
                statist = custom_tail(stats[k], 0.7, 0.7)
                statistics = statist[0].tolist() + statist[1].tolist()
            if l == 4:
                statistics = derivative_ac(stats[k])
            if l == 5:
                statistics = derivative_ab(stats[k])
            if l == 6:
                statistics = derivative_aa(stats[k])
            if l == 7:
                statist = daubechies(stats[k])
                statistics = statist[0].tolist() + statist[1].tolist()
            if l == 8:
                statist = custom_tailless(stats[k], 0.9, 0.9)
                statistics = statist[0].tolist() + statist[1].tolist()
            if l == 9:
                statist = symlet(stats[k])
                statistics = statist[0].tolist() + statist[1].tolist()
            if l == 10:
                statistics = custom_tail(derivative_ac(stats[k]), 0.9, 0.9)
                # in here is where each transformation will go.
                # so if 0, do the first transformation and so on.
                # some transformations (derivatives) have only 255 points rather than 256
                # so ensure that the ANN in the SaveResults section is organised, or use len()
                # Yep your project is as simple as using my code and pumping through a bunch of options
                # And then recording 100 times more data (10kSps) with a few (5) people
                # and seeing if it improves your accuracy beyond 1-2 %
            # statistics = stats[k]
            home = '/Users/jackmclovin/PycharmProjects Data/BCI Data/RasppiBasedBCI/Transformed Data/'
            actual_file_name = home + to_str(n) + '/' + to_str(j) + '/' + to_str(k) + '/' + to_str(l) + '.json'
            # N is Number person, J is number of test, K is number of channel, L is transformation
            # ANN uses Predicts N from J, comparing different K's and L's over P percent learnt.
            if not os.path.exists(home + to_str(n) + '/'):
                os.makedirs(home + to_str(n) + '/')
            if not os.path.exists(home + to_str(n) + '/' + to_str(j) + '/'):
                os.makedirs(home + to_str(n) + '/' + to_str(j) + '/')
            if not os.path.exists(home + to_str(n) + '/' + to_str(j) + '/' + to_str(k) + '/'):
                os.makedirs(home + to_str(n) + '/' + to_str(j) + '/' + to_str(k) + '/')

            writefile = open(actual_file_name, 'w+')
            writefile.close()
            with open(actual_file_name, 'w') as outfile:
                json.dump(statistics, outfile, sort_keys=True, indent=4,
                          ensure_ascii=False)
        # with open ('outfile', 'rb') as fp:
        # stats = pickle.load(fp)


def to_str(k):
    if k < 10:
        return '00' + str(k)
    elif k < 100:
        return '0' + str(k)
    else:
        return str(k)


def import_prepare_saved():
    # raw data i = , 364 -> 447 2a [84], 337->397 2c [61], 2c1000367, 3a 448->461 [14], 3c0000402
    # 'Raw Data/co2a0000' + 364 + i + '/co2a0000' + 364 + i + '.rd.' + j + '.gz'
    n = 0
    z = 0  # z is missing files
    name = '/Users/jackmclovin/PycharmProjects Data/BCI Data/RasppiBasedBCI'
    for i in range(0, 84):
        for j in range(0, 120):
            try:
                filename = name + '/Raw Data/co2a0000' + str(364+i) + '/co2a0000' + str(364+i)
                actual_file_name = filename + '.rd.' + to_str(j)
                readfile = open(actual_file_name, 'r')
                lines = readfile.readlines()  # document which files exist to prevent try except
                do_something_special(lines, n, j)
            except FileNotFoundError:
                z += 1
        n += 1
    for i in range(0, 61):
        for j in range(0, 120):
            try:
                filename = name + '/Raw Data/co2c0000' + str(337 + i) + '/co2c0000' + str(337+i)
                actual_file_name = filename + '.rd.' + to_str(j)
                readfile = open(actual_file_name, 'r')
                lines = readfile.readlines()  # document which files exist to prevent try except
                do_something_special(lines, n, j)
            except FileNotFoundError:
                z += 1
        n += 1

    for i in range(0, 14):
        for j in range(0, 120):
            try:
                filename = name + '/Raw Data/co3a0000' + str(448 + i) + '/co3a0000' + str(448+i)
                actual_file_name = filename + '.rd.' + to_str(j)
                readfile = open(actual_file_name, 'r')
                lines = readfile.readlines()  # document which files exist to prevent try except
                do_something_special(lines, n, j)
            except FileNotFoundError:
                z += 1
        n += 1

    for j in range(0, 120):
        try:
            filename = name + '/Raw Data/co2c1000' + str(367) + '/co2c1000' + str(367)
            actual_file_name = filename + '.rd.' + to_str(j)
            readfile = open(actual_file_name, 'r')
            lines = readfile.readlines()  # document which files exist to prevent try except
            do_something_special(lines, n, j)
        except FileNotFoundError:
            z += 1
    n += 1
    for j in range(0, 120):
        try:
            filename = name + '/Raw Data/co3c0000' + str(402) + '/co3c0000' + str(402)
            actual_file_name = filename + '.rd.' + to_str(j)
            readfile = open(actual_file_name, 'r')
            lines = readfile.readlines()  # document which files exist to prevent try except
            do_something_special(lines, n, j)
        except FileNotFoundError:
            z += 1
    n += 1


import_prepare_saved()

#plt.plot(y[1])
#plt.ylabel('inverse of custom')
#plt.show()

# save maxed data
# include triple fourier and wavelets

# convert above to function and don't call
# create function for importing max data

# use ANN on a level spec, save level spec check error after X, test on remaining 1/N data

