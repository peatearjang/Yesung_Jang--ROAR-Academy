import numpy as np

def set_array(L, rows, cols):
    ans = ""

    for _ in range(rows):
        for _ in range(cols):
            ans += str(L) + " "
        ans = ans[:-1]
        ans += "; "
    
    return np.matrix(ans[:-2])

print(set_array(2, 3, 2))