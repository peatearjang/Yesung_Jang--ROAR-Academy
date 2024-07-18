import numpy as np

a = np.array([list(range(i*10, i*10 + 6)) for i in range(6)])
print(a)
a1 = a[:,1]
b = a[1, 2:4]
# c = a[]