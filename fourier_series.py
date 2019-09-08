#! /usr/bin/python3

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from svgpathtools import svg2paths

def integrate(f, a, b):
    s = 0
    dt = 0.001
    for t in np.arange(a, b, dt):
        s += f(t)*dt
    return s

def fourier_coef(data, n):
    f = lambda t : get(data, t)*np.exp(-2*np.pi*n*t*1j)
    return integrate(f, 0, 1)

def get(data, t):
    return np.conj(data(t))

def init():
    for line in lines:
        line.set_data([], [])
        line.set_color((0, 0, 0, 0.2))
    lines[len(lines) - 1].set_data([], [])
    lines[len(lines) - 1].set_color((0.5, 0, 0.3, 0.8))
    return lines

def animate(i):
    center = 0+0j
    for idx, item in enumerate(coef):
        n, c = item['n'], item['c']
        f = lambda t : c * np.exp(2*np.pi*n*t*1j)
        tip = f((i+1)/frames) + center
        lines[idx].set_data([center.real, tip.real], [center.imag, tip.imag])
        center = tip
    pencil = lines[len(lines) - 1]
    pencil.set_xdata(np.append(pencil.get_xdata(), [center.real]))
    pencil.set_ydata(np.append(pencil.get_ydata(), [center.imag]))
    return lines

print("read svg...")
paths, _ = svg2paths("res/pi.svg")
data = paths[0].point

print("computing coefficients...")
N = 30
coef_n = [0] + [i*j for i in range(N) for j in [1, -1]]
coef = [{'n': n, 'c': fourier_coef(data, n)} for n in coef_n]

print("plot...")
points = [np.sum([item['c']*np.exp(2*np.pi*item['n']*t*1j) for item in coef]) for t in np.arange(0, 1, 0.01)]
center = np.average(points)
diff = np.max(np.absolute(points-center)) + 5
xcenter, ycenter = center.real, center.imag
fig = plt.figure()
ax = plt.axes(xlim=(xcenter-diff, xcenter+diff), ylim=(ycenter-diff, ycenter+diff))
ax.set_aspect("equal")
lines = [ax.plot([], [])[0] for i in range(len(coef))]
lines.append(ax.plot([], [])[0])

frames = 200
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=40, blit=True, repeat=True)

plt.show()