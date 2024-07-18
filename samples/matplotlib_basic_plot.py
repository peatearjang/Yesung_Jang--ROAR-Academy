## This is course material for Introduction to Python Scientific Programming
## Example code: matplotlib_basic_plot.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import matplotlib.pyplot as plt #plt is cutsom shorthand for pyplot
import numpy as np

# generate a basic sample point array on x-axis
x = np.arange(0,2*np.pi,0.1) # arange will return just like a regular range (start, stop, step)

# Create a sin function sample
y0 = np.sin(x) # set your y-axis as sin()
plt.plot(x, y0, color = 'r', linewidth = 3) # x = domain of function, y0 = type of function, "r" = red color, linewidth = thickness of line

# Create a dash cos function sample
y1 = np.cos(x)
plt.plot(x, y1, 'b--', linewidth = 1) # plot x and y1 onto the plot, b-- = blue color with dashed line
plt.ylim(-1, 1) # limit of the graph of the y-axis is from -1 to 1
plt.xlim(0,2*np.pi) #limit of the graph of the x-axis from 0 to 2*np.pi
plt.xticks(np.arange(0,2*np.pi,np.pi/4), ['0', 'pi/4', 'pi/2', '3pi/4', 'pi', '5pi/4', '3pi/2', '7pi/4']) # these are showing that in each pi value, instead of showing integers as the x-axis, it replaces them with the pi in values.
plt.show() # show the plot