from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


order = 20
fsample= 44100
fc= 300
wn= 2*fc/fsample
b, a = signal.butter(order, wn, btype='low', analog=False,output='ba', fs=fsample)
w, h = signal.freqs(b, a)
plt.semilogx(w, 20* np.log10(abs(h)))
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0.1,0.1)
plt.grid(which='both', axis='both')
plt.axvline(fc, color='green') # cutoff frequency
plt.show()
