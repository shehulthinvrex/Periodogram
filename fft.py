#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 08:49:52 2020

@author: subeesh
"""

import numpy as np

#Main code for the periodogram
import matplotlib.pyplot as plt


"""
https://www.ritchievink.com/blog/2017/04/23/understanding-the-fourier-transform-by-example/
"""

def DFT(x):
    """
    Compute the discrete Fourier Transform of the 1D array x
    :param x: (array)
    """

    N = x.size
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    return np.dot(e, x),N

import numpy as np
def npfft(x,t):
    '''Return the normalised amplitude of fft and frequency using fast FFT in Numpy'''
    import numpy as np
    N=x.size
    fft = np.fft.fft(x)
    T = t[1] - t[0]  # sampling interval 
    # 1/T = frequency
    f = np.linspace(0, 1 / T, N)
    abs_fft=np.abs(fft)[:N // 2] * 1 / N
    return abs_fft,f

# fft.npfft(x, t)
# plt.ylabel("Amplitude")
# plt.xlabel("Frequency [Hz]")
# plt.bar(f[:N // 2], np.abs(fft)[:N // 2] * 1 / N, width=1.5)  # 1 / N is a normalization factor
# plt.show()
