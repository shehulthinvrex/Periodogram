""" To remove the trend from timeseries data (detrend the timeseries data) """ 

import numpy as np
from scipy import signal
from matplotlib import pyplot as plt


""" Function for detrending timeseries data"""
def detrend(x_tseries,y_tseries):
	n_tseries=np.size(x_tseries)
	mean_x = np.mean(x_tseries)
	mean_y = np.mean(y_tseries)
	A_xy = np.sum(y_tseries*x_tseries - n_tseries*mean_y*mean_x)
	B_xx = np.sum(x_tseries*x_tseries - n_tseries*mean_x*mean_x)
		
	m = A_xy/B_xx
	c = mean_y - m*mean_x
	#print(m,c)
	trend_line = m * x_tseries + c
	detrend_line = y_tseries - trend_line
	return trend_line,detrend_line

""" function to compare the new detrend function"""	 
def detrend_scipy(tseries):
	tseries_dtrend = signal.detrend(tseries)
	return tseries_dtrend

