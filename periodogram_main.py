#Main code for the periodogram
import numpy as np
import matplotlib.pyplot as plt

#Generating a time series 
Fs = 60                         # sampling rate
Ts = 1.0/Fs                      # sampling interval
t = np.arange(0,1,Ts)            # time vector
ff = 1                          # frequency of the signal
y = np.sin(2 * np.pi * ff * t)
# Plotting time series
plt.plot(t,y,'k-')
plt.xlabel('time')
plt.ylabel('amplitude')

###Here comes Detrending


###tapering


### FFT


## statistics

##periodogram plot
