from mpl_toolkits import mplot3d # plotting a 3d dimension
import numpy as np
import matplotlib.pyplot as plt

figure, axes = plt.subplots(figsize=(5,5))

x = np.arange(-100, 100)
y = np.piecewise(x, [x < 2, x >= 2], [lambda x: 2*x, lambda x: -3*x+10])

axes.set_xlim([1,3])
axes.set_ylim([1,4])

plt.plot(x,y,c="blue")
plt.show()