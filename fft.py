#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
