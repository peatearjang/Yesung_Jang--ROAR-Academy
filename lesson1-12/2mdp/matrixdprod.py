import numpy as np

first, second = "1,0;0,1", "6, -9, 1; 4, 24, 8" #input("Equation: ").split(" * ")
second = np.matrix(second)

try:
    if type(int(first)) == int:
        print(first*second)
except:
    first = np.matrix(first)
    print(np.dot(first,second))
