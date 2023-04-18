import matplotlib.pyplot as plt 
import numpy as np
from scipy.fftpack import fft, ifft, fftshift

f=10
overSampRate=50
phase= 0 #1/3*np.pi
nCyl = 5 #Number of cycles
fs = overSampRate*f #sampling frequency
t = np.arange(0, nCyl*1/f-1/fs,1/fs) # time base
sin1 = np.sin(2*np.pi*f*t+phase) #replace with cos if a cos ... (no leible)
plt.plot(t,sin1)

plt.xlabel('time(s)')
plt.ylabel('Amplitude')
plt.title('Sine wave f='+ str(f) + 'Hz vs  time(sec)')
plt.grid(True)
plt.savefig('plot-voltage-vs.-time1.png')
plt.show()


A=0.5
sin2= A*np.sin(5*f*2*np.pi*t)
plt.plot(t,sin2)

plt.xlabel('time(s)')
plt.ylabel('voltage (mV)')
plt.title('voltage (mV) vs. time (sec)')
plt.grid(True)
plt.savefig('plot-voltage-vs.-time2.png')
plt.show()

sin3= sin1+ sin2

L=sin3.size
An=0.2
noise= An*np.random.normal(0,1,L)
sin4 = sin3 + noise
plt.plot(t,sin3)
plt.xlabel('time (s)')
plt.ylabel('voltage (mV) vs. time (sec)')
plt.title('voltage (mV) vs.time (sec)')
plt.grid(True)
plt.savefig("plot-voltage-vs.-time3.png")
plt.show()

N= 512 #N-point DFT
X = fft(sin4, N) #compute X(k)
X = ifft(sin4,N) #compute X(n)
fig1, ax= plt.subplots(nrows=1,ncols=1) # create figure handle

nVals = np.arange(start = 0,stop=N) # raw index for FFT plot
ax.plot(nVals, np.abs(X))
ax.set_title('Double Sided FFT- without FFTShift')
ax.set_xlabel('Sample points (N-point DFT)')
ax.set_ylabel('DFT Values')
plt.savefig('plot-voltage-vs.-time4.png')
plt.show()

fig2, ax = plt.subplots(nrows=1, ncols=1)

nVals =np.arange(start=0, stop = N)/N
ax.plot(nVals, np.abs(X))
ax.set_title('Double Sided FFT- without FFTShift')
ax.set_xlabel('Normalized frequency')
ax.set_ylabel('DFT Values')
plt.savefig('plot-voltage-vs.-time5.png')
plt.show()

X=fftshift(fft(sin4,N)) #compute DFT USING FFT
fig3, ax = plt.subplots(nrows=1,ncols=1) #create figure handle
fVals = np.arange(start = -N/2, stop = N/2)/N  # Normalized DFT sample point
ax.plot(fVals, np.abs(X))
ax.set_title('Double Sided FFT- with FFTShift')
ax.set_xlabel('Normalized frequency')
ax.set_ylabel('DFT Values')
ax.autoscale(enable=True, axis='x',tight=True)
ax.set_xticks(np.arange(-0.5,0.5+0.1,0.1))
plt.savefig('plot-voltage-vs.-time6.png')
plt.show()

X=fftshift(fft(sin4,N)) 
fig4, ax = plt.subplots(nrows=1,ncols=1)
fVals= np.arange(start = -N/2, stop = N/2)*fs/N
ax.plot(fVals,np.abs(X), 'b')
ax.set_title('Double Sided FFT- with FFTShift')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('|DFT Values|')
ax.set_xlim(0,100)
ax.set_xticks(np.arange(0,100+10,10))
plt.savefig('plot-voltage-vs.-time7.png')
plt.show()