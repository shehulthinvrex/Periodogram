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
