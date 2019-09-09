import numpy as np
import matplotlib.pyplot as plt

# data
time = np.arange(-5, 5, 0.01)
freq = np.arange(0, 5, 0.01)
signal = 2*np.cos(2 * np.pi * 3 * time) + np.cos(2 * np.pi * 4 * time) + np.sin(2 * np.pi * 1.5 * time)
fourier = [np.mean(signal * np.exp(-2j * np.pi * f * time)) for f in freq]

# figure
fig, axs = plt.subplots(nrows=4, figsize=(6, 6))

# original signal
axs[0].grid(True)
axs[0].set_ylabel('f(t)')
axs[0].plot(time, signal)

# real part fourier transform
axs[1].grid(True)
axs[1].set_ylabel('Re(F{f})')
axs[1].plot(freq, np.real(fourier))

# imaginary part fourier transform
axs[2].grid(True)
axs[2].set_ylabel('Im(F{f})')
axs[2].plot(freq, np.imag(fourier))

# module fourier transform
axs[3].grid(True)
axs[3].set_ylabel('|F{f}|')
axs[3].plot(freq, np.absolute(fourier))

# show
fig.suptitle("f(t) = 2*cos(2 * pi * 3 * t) + cos(2 * pi * 4 * t) + sin(2 * pi * 1.5 * t)")
fig.canvas.set_window_title('Fourier Transform')
plt.show()