import numpy as np
def smooth(x, window_len=11, window='hanning'):
    '''
    Using inbuilt convolve function of numpy
    input:
        x: signal
        window_len: the dimension of the smoothing window; should be an odd integer
        window: type of window from 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'
    output:
        the smoothed signal
    '''

    if window_len < 3:  return x

    if x.ndim != 1: raise (StandardError('smooth only accepts 1 dimension arrays.'))
    if x.size < window_len:  raise (StandardError('Input vector smaller than window size.'))
    win_type = ['flat', 'hanning', 'hamming']
    if window not in win_type: raise( StandardError('Unknown window type'))

    s = np.r_[x[window_len-1:0:-1],x,x[-2:-window_len-1:-1]]
    if window == 'flat': #moving average
        w=np.ones(window_len,'d')
    else:
        w=eval('np.'+window+'(window_len)')
    y=np.convolve(w/w.sum(),s,mode='valid')
    return y
