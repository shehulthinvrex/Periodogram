#Main code for the periodogram
import numpy as np
import matplotlib.pyplot as plt
import fft
import detrend
import tapering_window
def periodogram_main(tseries,t,test='no',tap_method="Hanning",deterend="cubic"):
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
       5) test= just for testing no input data required
               "yes"
               "no"
       
               Output:
    1) powerspectral density
    3) frequency
    2) plot

    Example:
      periodogram_main(tseries,t,tap_method="Hanning",deterend="cubic",test='no')
    
    '''
    if test=="yes":
        Fs = 60                         # sampling rate
        Ts = 1.0/Fs                      # sampling interval
        t = np.arange(0,1,Ts)            # time vector
        ff = 100                         # frequency of the signal
        y = np.sin(2 * np.pi * ff * t)
        
        # Plotting time series
        plt.subplot(1,2,1)
        plt.plot(t,y,'k-')
        plt.xlabel('time')
        plt.ylabel('amplitude')
        
        [abs_fft,f]=fft.npfft(y,t)  
        plt.subplot(1,2,2)
        plt.plot(f[: len(f)//2],abs_fft,'k-')
        plt.xlabel('frequency')
        plt.ylabel('psd')
        plt.show()
    if deterend=="cubic":
        tseries_dtrend=detrend.detrend_scipy(tseries)
    elif deterend=='none':
        tseries_dtrend=tseries
    if tap_method=="none":        
        tseries_tapered=tseries_dtrend
    else:
        tseries_tapered=tapering_window(tseries,tap_method)
        
        
    [abs_fft,f]=fft.npfft(tseries_tapered,t)
    plt.subplot(1,2,1)
    plt.plot(t,tseries,'k-')
    plt.xlabel('time')
    plt.ylabel('amplitude') 
    plt.subplot(1,2,2)
    plt.plot(f[: len(f)//2],abs_fft,'k-')
    plt.xlabel('frequency')
    plt.ylabel('psd')
    plt.show()    
    
        
        
        
print('haha')    
        
