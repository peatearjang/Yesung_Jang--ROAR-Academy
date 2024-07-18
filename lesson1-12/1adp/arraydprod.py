from mpl_toolkits import mplot3d # plotting a 3d dimension
import numpy as np
import matplotlib.pyplot as plt

v = np.array([2.,2.,4.]) # an array that will represent the x,y,z

e0, e1, e2 = v

fig = plt.figure()
ax = plt.axes(projection="3d")

# new axis!
e2 = np.linspace(0, e2)
e0 *= e2
e1 *= e2
ax.plot3D(e0, e1, e2, "blue")

plt.show()