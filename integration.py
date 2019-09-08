#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# function, range, and dx
function = lambda x : np.sin(x)
xmin, xmax = 0, 2 * np.pi
dx = 0.1

# figure
fig, ax = plt.subplots(figsize=(10, 4))

# draw rectangles
for x in np.arange(xmin, xmax, dx):
    ax.add_patch(Rectangle(xy=(x, 0), width=dx, height=function(x), color=(1, 0, 0, 0.2)))

# draw function
x = np.arange(xmin, xmax, 0.01)
y = function(x)
ax.plot(x, y)

# show
ax.grid(True)
plt.show()