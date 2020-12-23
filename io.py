import numpy as np
import matplotlib.pyplot as plt
#
# Calling new function for smoothing
from func_smooth import smooth
#
# Input file taken from code snippet given by Amol
filename_ascii = 'ssh_u.dat'
ssh_file = np.loadtxt(filename_ascii)
time = ssh_file[:, 0]
ugeo = ssh_file[:, 1]
# 
smu  = smooth(ugeo,11,'hamming')
plt.plot(smu)

