import numpy as np

def zeros_insert(k, n):
    bufer = [k[0]]
    for every in k[1:]:
        for i in range(0,n):
            bufer += [0]
        bufer += [every]
    return np.array(bufer)

if __name__ == '__main__':
    k = np.array([2, 3, 4, 1, 0])
    #k = [1]
    n = 3
    r = zeros_insert(k, n)
    print(r)

