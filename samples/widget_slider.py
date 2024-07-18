## This is course material for Introduction to Python Scientific Programming
## Example code: widget_slider.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons # slider and radio buttons will allow you to use a slider and buttons in your window

# Create initial plot and values

# 1. generate the plot
fig, ax = plt.subplots() # generate a figure
plt.subplots_adjust(left=0.25, bottom=0.25)
t = np.arange(0.0, 1.0, 0.001) 
a0 = 5; f0 = 3; delta_f = 0.1; delta_a = 0.1

# 2. generate sine function
s = a0 * np.sin(2 * np.pi * f0 * t)
l, = plt.plot(t, s, lw=2)
ax.margins(x=0)

# |----------------------------------------------|

# Create two sliders
axcolor = 'lightgoldenrodyellow' #color of slider

# the axes that are inputted are all relative from other coordinates:
# [percent from end of left window to start at that point, percent from the bottom of screen to the certain point, percentage from end of left window to end at that point, width of slider ]
axfreq = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0, valstep=delta_f)
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0, valstep=delta_a)

# slider update actions
def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t)) # refresh plot
    fig.canvas.draw_idle() # draw_idle -> first you draw it, then you freeze the data so people can see the new, updated plot

# **SPECIFY EVENTS WHENEVER MAKING INTERACTIVE THINGS**
"""
for this kind of library, you don't have to have a roever while loop to check if there is change so you have to create and delete each frame
The on_changed function and os will automatically will do it for you
it will just sit there waiting for you to do something
"""
# this function will help update the graph, even if you slide. you can update the wdiget slider, but you will not affect the graph
sfreq.on_changed(update) # on the event of on_changed in sfreq, call your def update(val) function
samp.on_changed(update) # on the event of on_changed in samp, call your def update(val) function


# |----------------------------------------------|


# Create a radio button
#again, [start 2.5% to the right, start 50% up, end 15% to the right, width]
rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)
l.set_color(radio.value_selected)

# radio button update actions
def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()

# similar stuff from the slider function, the on_clicked will check if the buttons are clicked and if they are, they will call the colorfunc fucntion
radio.on_clicked(colorfunc)

# shwo plot
plt.show()
