## This is course material for Introduction to Python Scientific Programming
## Example code: matplotlib_sigmoid.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.arange(-10., 10., 0.2) # 100 elements in the range -> (-10, 10) has a range or 20 but skips by 0.2 so there are 100 elements
sig = sigmoid(x) #the graph

fig = plt.figure()
ax1 = fig.add_subplot(1, 3, 1) # 1 x 3 graph

# add_subplot(x,y, graph_number)
"""
let's say x = 3 , y = 2

this will generate a 3 x 2 plot to put 6 graphs inside the window
the graph spots are going to be show like this:
graph1, graph2, graph3
graph4, graph5, graph6

it's not going to show on the created window, but it will be the options where you can put you graph in
"""

# Plot without customization
plt.plot(x,sig, linewidth = 3)

ax2 = fig.add_subplot(1, 3, 2)
# Move left y-axis and bottim x-axis to centre
ax2.spines['left'].set_position('center') # moving left axis to center
ax2.spines['bottom'].set_position('center') # moving bottom axis to center
# Eliminate upper and right axes
ax2.spines['right'].set_color('none') # right axis is there, but now you don't see the plot
ax2.spines['top'].set_color('none') # top axis is there, but now you don't see the plot
# Plot the customized (x-y) axes
plt.plot(x,sig, linewidth = 3) #

ax3 = fig.add_subplot(1,3,3)
# Move left y-axis to centre
ax3.spines['left'].set_position('center') #moving left axis to the center
ax3.spines['bottom'].set_position(('data',0)) # setting bottom axis respect to the location of your data. For example, you data's 0 is at the bottom, so the x-axis will be set at where the 
# Eliminate upper and right axes
ax3.spines['right'].set_color('none') # right axis is there, but now you don't see the plot
ax3.spines['top'].set_color('none') # top axis is there, but now you don't see the plot
# Plot the customized (x-y) axes
plt.plot(x,sig,  linewidth = 3)

plt.show()