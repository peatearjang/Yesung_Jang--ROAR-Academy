## This is course material for Introduction to Python Scientific Programming
## Example code: matplotlib_clock.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use


# ctrl + c -> terminal - WILL KILL THE WINDOW THAT KEEPS POPPING UP

from datetime import datetime
import matplotlib.pyplot as plt
import os
import numpy as np

# Initialization, define some constant
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/airplane.bmp'
background = plt.imread(filename)

"""
the origin of a picture is top left but the origin of matplotlib is bottom left
"""

# setting dimensions of clock hands
second_hand_length = 200
second_hand_width = 2
minute_hand_length = 150
minute_hand_width = 6
hour_hand_length = 100
hour_hand_width = 10
center = np.array([256, 256])

# clock hand vector calculations based on your time
# time range [0, 59] because minutes and hours are from 0-60
# **ALSO THE CLOCK COORDINATES AND IMAGE COORDINATES ARE DIFFERENT!!**
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# rreeeeeeeeeeeaaaaaaad this fuuuunnnnccttiiiiiiiiooooooooon
# PLOTTING: angle(theta) = image angle(theta - 90) --> cos(theta-(pi/2))=sin(theta) ; sin(theta-(pi/2)) = cos(theta)

def clock_hand_vector(angle, length):
    return np.array([length * np.sin(angle), -length * np.cos(angle)])

# draw an image background
# fig, ax = plt.subplots()

while True:
    # plt.imshow(background)

    # First retrieve the time
    now_time = datetime.now() # get actual current time
    hour = now_time.hour
    if hour>12: hour = hour - 12 # if over 12 hours, subtract because clock has only 12 hours
    minute = now_time.minute
    second = now_time.second

    # just calculating end points of hour, minute, second
    second_vector = clock_hand_vector(second/60*2*np.pi, second_hand_length)
    print(second)
    # minute_vector = clock_hand_vector(minute/60*2*np.pi, minute_hand_length)
    # hour_vector = clock_hand_vector(hour/12*2*np.pi, hour_hand_length)


    # moving the origin to the center, not at (0,0), which is not at the center of the screen
    # plt.arrow(center[0], center[1], hour_vector[0], hour_vector[1], head_length = 3, linewidth = hour_hand_width, color = 'black')
    # plt.arrow(center[0], center[1], minute_vector[0], minute_vector[1], linewidth = minute_hand_width, color = 'black')
    # plt.arrow(center[0], center[1], second_vector[0], second_vector[1], linewidth = second_hand_width, color = 'red')

    # plt.axis("off") #removing axes

    #pause. why? because the program will run faster than time.
    # plt.pause(0.0000001)
    # clear plot. why? because this will clear your past drawing.
    # plt.clf()