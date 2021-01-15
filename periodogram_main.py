#Main code for the periodogram
import numpy as np
import matplotlib.pyplot as plt
import fft
import detrend
from sys import exit
from tapering_window import tapering_window
def periodogram_main(tseries,t,tap_method="Hanning",deterend="cubic",plot="no"):
    pass
    #
    ''' Function for generate a periodogram 
        1) tseries : 1D variable containing time series data.
        2) Time axis
        3)tap_method  : Use any one of the teppering window given below.
                    "Hanning" (default)
                    "Hamming"
                    "Boxcar"
                    "Tukey"
                    "Blackman-Harris"
                    "Kaiser"
                    "none"
       4)deterend= Detrending method
                   "cubic"
                   "none"
       5) plot= "yes" plots 
               "no" returns data
       
               Output:
    1) powerspectral density
    3) frequency
    2) plot

    Example:
      periodogram_main(tseries,t,tap_method="Hanning",deterend="cubic",plot='no')
    
    '''
    
    if deterend=="cubic":
        tseries_dtrend=detrend.detrend_scipy(tseries)
    elif deterend=='none':
        tseries_dtrend=tseries
    if tap_method=="none":        
        tseries_tapered=tseries_dtrend
    else:
        tseries_tapered=tapering_window(tseries,tap_method)
        
        
    [abs_fft,f]=fft.npfft(tseries_tapered,1)
    if plot=="yes":
        plt.subplot(1,2,1)
        plt.plot(t,tseries,'k-')
        plt.xlabel('time')
        plt.ylabel('amplitude') 
        plt.subplot(1,2,2)
        plt.plot(f,abs_fft,'k-')
        plt.xlabel('frequency')
        plt.ylabel('psd')
        plt.show()    
    else:
        return abs_fft,f
        
        
        
print('check:ok')    
        
