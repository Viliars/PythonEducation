import numpy as np
import pandas as pd


def df_diag_ones(matrix):
    size = matrix.shape[0] - 1
    for i in range(0,size+1):
        matrix[i][i], matrix[size-i][i] = 1, 1
    return matrix

if __name__ == '__main__':
    df = [[16,  5, 23,  4, 20],
          [24,  8, 15, 24,  9],
          [15, 11,  9,  8,  7],
          [ 5, 17,  8, 13,  1],
          [12, 24,  7, 20, 13]]
    df = pd.DataFrame(df)
    df = df_diag_ones(df)
    print(df.values)
