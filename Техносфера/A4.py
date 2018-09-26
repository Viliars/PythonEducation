import pandas as pd
import numpy as np
"""
def peak_finder(s):
    bufer = []
    for (i, every) in enumerate(s[1:-1]):
        if every >= s[i+2] and every >= s[i]:
            bufer += [i+1]
    return np.array(bufer)
"""
def peak_finder(s):
    bufer = []
    for i in range(1,len(s)-1):
        if s[i] >= s[i+1] and s[i] > s[i-1]:
            bufer += [i]
    return np.array(bufer)



if __name__ == '__main__':
    s = pd.Series([5, 1, 1, 5])
    r = peak_finder(s)
    print(r)
