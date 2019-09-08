import numpy as np
import matplotlib.pyplot as plt

# data
t = np.arange(0, 5, 0.001)
signal = 2*np.cos(2 * np.pi * 3 * t) + np.cos(2 * np.pi * 4 * t) + np.sin(2 * np.pi * 1.5 * t)
fourier = [np.mean(signal * np.exp(-2 * np.pi * f * t * 1j)) for f in t]

# figure
fig, axs = plt.subplots(nrows=4, figsize=(6, 6))

# original signal
axs[0].grid(True)
axs[0].set_ylabel('f(t)')
axs[0].plot(t, signal)

# real part fourier transform
axs[1].grid(True)
axs[1].set_ylabel('Re(F{f})')
axs[1].plot(t, np.real(fourier))

# imaginary part fourier transform
axs[2].grid(True)
axs[2].set_ylabel('Im(F{f})')
axs[2].plot(t, np.imag(fourier))

# module fourier transform
axs[3].grid(True)
axs[3].set_ylabel('|F{f}|')
axs[3].plot(t, np.absolute(fourier))

# show
fig.suptitle("f(t) = 2*cos(2 * pi * 3 * t) + cos(2 * pi * 4 * t) + sin(2 * pi * 1.5 * t)")
fig.canvas.set_window_title('Fourier Transform')
plt.show()