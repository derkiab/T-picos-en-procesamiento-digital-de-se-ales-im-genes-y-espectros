import matplotlib.pyplot as plt 
import numpy as np
from scipy.fftpack import fft, ifft, fftshift




f1=10
phase= 0 #1/3*np.pi
nCyl = 20 #Number of cycles
fs = 1000 #sampling frequency
t = np.arange(0, nCyl*1/f1-1/fs,1/fs) # time base
A=0.5
X= A*np.sin(2*f1*np.pi*t)
plt.plot(t,X)

plt.xlabel('time(s)')
plt.ylabel('freq')
plt.title('freq vs. time (sec)')
plt.grid(True)
plt.savefig('freq-vs.-time2.png')
plt.show()

f2=5
nCyl = 20 #Number of cycles
fs2 = 1000 #sampling frequency
A2=0.5
X2= A2*np.sin(2*f2*np.pi*t)
plt.plot(t,X2)

plt.xlabel('time(s)')
plt.ylabel('freq')
plt.title('freq vs. time (sec)')
plt.grid(True)
plt.savefig('freq-vs.-time2.png')
plt.show()


