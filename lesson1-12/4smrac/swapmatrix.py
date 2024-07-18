import numpy as np

def swap_rows(M, a, b):
    newm = M.copy()
    # a, b = M[b-1], M[a-1]
    btoa, atob = M[a], M[b]

    newm[a], newm[b] = atob, btoa
    return newm

def swap_cols(M, a, b):
    if type(a) != int or type(b) != int:
        raise TypeError("Type must be an integer!")
    elif a > len(M) or b > len(M):
        raise ValueError("Values must be in the index of your matrix!")
    else:
        newm = M.copy()
        
        for i in range(len(M)):
            newm[i:i+1,b], newm[i:i+1,a] = M[i:i+1,a], M[i:i+1,b]

        return newm

print(swap_cols(np.matrix("1,2,3;4,5,6;7,8,9"), 0, 2))