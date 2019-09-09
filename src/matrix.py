import numpy as np
import matplotlib.pyplot as plt
from svgpathtools import svg2paths

# load data in array of points
paths, _ = svg2paths("../res/pi.svg")
data = paths[0].point
data = [np.conj(data(t)) for t in np.arange(0, 1, 0.001)]
data = [[np.real(z), np.imag(z)] for z in data]

# build rotation matrix
theta = 45
matrix = [
	[np.cos(theta), -np.sin(theta)],
	[np.sin(theta), np.cos(theta)]
]

# apply transformation on each point
new_data = np.array([np.dot(matrix, point) for point in data])

# plot new data
plt.plot(new_data[:,0], new_data[:,1])
plt.gca().set_aspect('equal')
plt.show()