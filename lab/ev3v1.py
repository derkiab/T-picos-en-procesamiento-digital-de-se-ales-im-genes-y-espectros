import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def design_lowpass_filter(fc, fs, ripple_db, attenuation_db, order):
    # Cálculo de la frecuencia de corte normalizada
    wn = (2 * fc) / fs

    # Diseño del filtro Butterworth
    b, a = signal.butter(order, wn, btype='lowpass', analog=False, output='ba')

    return b, a

# Especificaciones del filtro
fc = 300  # Frecuencia de corte en Hz
fs = 44100  # Frecuencia de muestreo en Hz
ripple_db = 10  # Ondulación en banda de paso en dB
attenuation_db = 100  # Atenuación en banda de rechazo en dB
order = 20  # Orden del filtro

# Diseñar el filtro paso bajo
b, a = design_lowpass_filter(fc, fs, ripple_db, attenuation_db, order)

# Obtener la respuesta en frecuencia del filtro
w, h = signal.freqz(b, a)

# Graficar la respuesta en frecuencia (magnitud)
plt.figure()
plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.axvline(0.3, color='green', linestyle='--')  # Línea vertical en la frecuencia de corte
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud (dB)')
plt.title('Respuesta en Frecuencia del Filtro Paso Bajo')
plt.grid(True)

# Generar señales sintéticas
t = np.linspace(0, 1, num=44100)  # Tiempo de 1 segundo
X1 = 0.01 * np.sin(2 * np.pi * 100 * t)  # Señal X1
X2 = 0.01 * np.sin(2 * np.pi * 1500 * t)  # Señal X2
e = np.random.normal(0, np.sqrt(0.5e-3), len(t))  # Ruido blanco aditivo

# Señal 1: X1
signal_1 = X1

# Señal 2: X1 + X2
signal_2 = X1 + X2

# Señal 3: X1 + X2 + e
signal_3 = X1 + X2 + e

# Filtrar las señales
filtered_signal_1 = signal.lfilter(b, a, signal_1)
filtered_signal_2 = signal.lfilter(b, a, signal_2)
filtered_signal_3 = signal.lfilter(b, a, signal_3)

# Graficar las señales antes y después del filtrado
plt.figure()

# Señal 1
plt.subplot(3, 2, 1)
plt.plot(t, signal_1, 'b')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal 1: Antes del filtrado')

plt.subplot(3, 2, 2)
plt.plot(t, filtered_signal_1, 'r')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal 1: Después del filtrado')

# Señal 2
plt.subplot(3, 2, 3)
plt.plot(t, signal_2, 'b')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal 2: Antes del filtrado')

plt.subplot(3, 2, 4)
plt.plot(t, filtered_signal_2, 'r')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal 2: Después del filtrado')

# Señal 3
plt.subplot(3, 2, 5)
plt.plot(t, signal_3, 'b')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal 3: Antes del filtrado')

plt.subplot(3, 2, 6)
plt.plot(t, filtered_signal_3, 'r')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal 3: Después del filtrado')

plt.tight_layout()

# Mostrar todos los gráficos juntos
plt.show()

# Obtener el espectro de frecuencia de las señales antes y después del filtrado
freq_signal_1, spectrum_signal_1 = signal.freqz(signal_1)
freq_filtered_signal_1, spectrum_filtered_signal_1 = signal.freqz(filtered_signal_1)
freq_signal_2, spectrum_signal_2 = signal.freqz(signal_2)
freq_filtered_signal_2, spectrum_filtered_signal_2 = signal.freqz(filtered_signal_2)
freq_signal_3, spectrum_signal_3 = signal.freqz(signal_3)
freq_filtered_signal_3, spectrum_filtered_signal_3 = signal.freqz(filtered_signal_3)

# Mostrar todos los gráficos juntos
plt.show()