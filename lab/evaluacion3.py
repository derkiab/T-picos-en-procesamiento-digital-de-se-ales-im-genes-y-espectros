import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 44100  # Sampling frequency
# Generate the time vector properly
t = np.arange(100000) / fs
fc = 300  # Cut-off frequency of the filter
w = fc*2 / fs # Normalize the frequency
b, a = signal.butter(20, w, 'low')


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

output = signal.filtfilt(b, a, signalc)
plt.plot(t, output, label='filtered')
plt.legend()
plt.show()