import numpy as np
import matplotlib.pyplot as plt

# function and its derivative
function = lambda x : x**2
function_derivative = lambda x : 2*x

x = np.arange(-10, 10, 0.01)
y = function(x)

# starting point
xmin = 10
learning_rate = 0.1
xgrad = function_derivative(xmin)

# gradient descent
xmin_array = []
while np.abs(xgrad) > 0.01:
	xmin_array.append(xmin)
	xgrad = function_derivative(xmin)
	xmin -= learning_rate * xgrad
xmin_array = np.array(xmin_array)

# plot
fig, ax = plt.subplots()
ax.plot(x, y, color=(0, 0, 1, 0.5))
ax.plot(xmin_array, function(xmin_array), color=(1, 0, 0, 0.5), marker='.')
plt.show()