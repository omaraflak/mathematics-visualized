#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# function, range, and dx
function = lambda x : np.sin(x)
xmin, xmax = 0, 2 * np.pi
dx = 0.1

fig, ax = plt.subplots(figsize=(10, 4))

for x in np.arange(xmin, xmax, dx):
    ax.add_patch(Rectangle(xy=(x, 0), width=dx, height=function(x), color=(1, 0, 0, 0.2)))

x = np.arange(xmin, xmax, 0.01)
y = function(x)

ax.grid(True)
ax.plot(x, y)
plt.show()