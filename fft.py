# plt.show()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 08:49:52 2020

@author: subeesh
"""

import numpy as np

"""
https://www.ritchievink.com/blog/2017/04/23/understanding-the-fourier-transform-by-example/
"""

# def DFT(x):
#     """
#     Compute the discrete Fourier Transform of the 1D array x
#     :param x: (array)
#     """

#     N = x.size
#     n = np.arange(N)
#     k = n.reshape((N, 1))
#     e = np.exp(-2j * np.pi * k * n / N)
#     return np.dot(e, x),N

def npfft(x,t):
    '''Return the normalised amplitude of fft and frequency using fast FFT in Numpy'''
    import numpy as np
    N=x.size
    fft = np.fft.fft(x)
    T = t[1] - t[0]  # sampling interval 
    # 1/T = frequency
    ff = np.linspace(0, 1 / T, N)
    f=ff[:N // 2]
    abs_fft=np.abs(fft)[:N//2] * 1 / N
    return abs_fft,f
