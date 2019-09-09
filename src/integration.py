import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# function, range, and dx
function = lambda x : np.sin(x)
xmin, xmax = 0, 2 * np.pi
dx = 0.1

# figure
fig, ax = plt.subplots(figsize=(15, 8))

# draw rectangles
patches = []
for x in np.arange(xmin, xmax, dx):
    patches.append(ax.add_patch(Rectangle(xy=(x, 0), width=dx, height=function(x), color=(1, 0, 0, 0.2))))

# draw function
x = np.arange(xmin, xmax, 0.01)
y = function(x)
ax.plot(x, y)

# labels
p = patches[8]
x_arrow, y_arrow = p.get_xy()
arrow = dict(facecolor='black', shrink=0.01, width=1, headwidth=5, headlength=5)
ax.annotate('f(x)', xy=(x_arrow, y_arrow + p.get_height() / 2), xytext=(0, 0.5), arrowprops=arrow, size=15)
ax.annotate('dx', xy=(x_arrow + p.get_width() / 2, y_arrow), xytext=(0, -0.5), arrowprops=arrow, size=15)
ax.plot([x_arrow, x_arrow + dx], [y_arrow, y_arrow], color='purple')
ax.plot([x_arrow, x_arrow], [y_arrow + p.get_height(), y_arrow], color='purple')

# show
ax.grid(True)
plt.suptitle('∫f(x)dx = Σ f(x)dx')
plt.show()