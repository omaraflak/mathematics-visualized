import numpy as np
import matplotlib.pyplot as plt

# amplitude, phase, frequency
apf = [(1, 0, 1), (2, 0, 1), (1, np.pi / 4, 1), (1, 0, 3)]

fig, axs = plt.subplots(nrows=len(apf))

for idx, (a, p, f) in enumerate(apf):
    function = lambda t : a * np.sin(f * t + p)
    time = np.arange(0, 2*np.pi, 0.001)
    signal = function(time)
    axs[idx].plot(time, signal)

plt.show()