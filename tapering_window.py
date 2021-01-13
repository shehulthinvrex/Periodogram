#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:13:05 2021

@author: jithin
"""
# Those who curious about why do we need to apply a tepering window prior
# to the FFT, go through the following link for a laymans description.
#  https://www.edn.com/windowing-functions-improve-fft-results-part-i/
import numpy as np
from scipy import signal

def tapering_window(tseries,method="Hanning"):
    """
    Returns Tapered 1D time series.
   Input:
        1) tseries : 1D variable containing time series data.
        2) method  : Use any one of the teppering window given below.
                    "Hanning" (default)
                    "Hamming"
                    "Boxcar"
                    "Tukey"
                    "Blackman-Harris"
                    "Kaiser".
    Output:
    1) tseries_tapered    : Time series after applaying tapering window

    Example:
        tapering_window(time_series)
        tapering_window(time_series,"Tukey")
    """
    length=len(tseries)
    if method=="Hanning":
        # The Hanning window is a taper formed by using a weighted cosine.
        # w(n)=  0.5-0.5*cos(2*pi*n/(M-1)))
        #  with      0<=M<=1
        wind_hanning=np.hanning(length)
        tseries_tapered=tseries*wind_hanning
        print("Hanning window is applied.....")
    elif method=="Hamming":
        # The Hanning window is a taper formed by using a weighted cosine.
        # w(n)=  0.54-0.46*cos(2*pi*n/(M-1)))
        #  with      0<=M<=1
        wind_hamming=np.hamming(length)
        tseries_tapered=tseries*wind_hamming
        print("Hamming window is applied.....")
    elif method=="Boxcar":
        wind_boxcar=signal.boxcar(length)
        tseries_tapered=tseries*wind_boxcar
        print("Boxcar window is applied.....")
    elif method=="Tukey":
       # Also called "Planck-taper" window is a bump function
        wind_tukey = signal.tukey(length)
        tseries_tapered=tseries*wind_tukey
        print("Tukey window is applied.....")
    elif method=="Blackman-Harris":
       # A generalization of the Hamming family
       # w(n)=a0-a1cos(2*pi*n/N)+a2cos(4*pi*n/N)-a3cos(6*pi*n/N)
        wind_buckman=signal.blackmanharris(length)
        tseries_tapered=tseries*wind_buckman
        print("Blackman-Harris window is applied.....")
    elif method=="Kaiser":
      # The Kaiser window is a taper formed by using a Bessel function.
      # w(n)=I0(beta*sqrt(1=(4*n^2/(M-1)^2))/(I0*beta)
      # with
      #   -(M-1)/2<=n<=(M-1)/2
      # The Kaiser can approximate many other windows by varying
      # the beta parameter.
        beta=14.0
        wind_kaiser=np.kaiser(length,beta)
        tseries_tapered=tseries*wind_kaiser
        print("kaiser window is applied.....")
    return tseries_tapered
