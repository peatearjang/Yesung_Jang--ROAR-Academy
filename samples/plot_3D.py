## This is course material for Introduction to Python Scientific Programming
## Example code: plot_3D.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from mpl_toolkits import mplot3d # plotting a 3d dimension
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")

# new axis!
z_line = np.linspace(0, 15, 1000)
x_line = np.cos(z_line)*z_line # using z as x to get a spiral shape
y_line = np.sin(z_line)*z_line # using z as x to get a spiral shape
ax.plot3D(x_line, y_line, z_line, 'gray')

z_points = 15 * np.random.random(100)
x_points = np.cos(z_points)*z_points + 1 * np.random.randn(100) # the multiplication to increase noise -> randn means random noise, 100 points that deviate from the line
y_points = np.sin(z_points)*z_points + 1 * np.random.randn(100)
ax.scatter3D(x_points, y_points, z_points, c=z_points, cmap='hsv') # c=z_points means that it is using the z points to use as color

plt.show()