import numpy as np
from numba import njit


def clip(qreg: list, start: int, end: int):
    return qreg[start:end+1]


def ttg(qreg):
    '''
    qreg = [2, 3, 4]

    return 

       j= 0 1 2
    i=0 [ 0 0 0 ]
    i=1 [ 0 0 1 ]
    i=1 [ 0 0 2 ]
    i=1 [ 0 0 3 ]
    i=2 [ 0 1 0 ]
    i=3 [ 0 1 1 ]
    i=3 [ 0 1 2 ]
    i=3 [ 0 1 3 ]
    i=4 [ 0 2 0 ]
    i=5 [ 0 2 1 ]
    i=5 [ 0 2 2 ]
    i=5 [ 0 2 3 ]
    i=6 [ 1 0 0 ]
    i=7 [ 1 0 1 ]
    i=7 [ 1 0 2 ]
    i=7 [ 1 0 3 ]
    i=8 [ 1 1 0 ]
    i=9 [ 1 1 1 ]
    i=9 [ 1 1 2 ]
    i=9 [ 1 1 3 ]
   i=10 [ 1 2 0 ]
   i=11 [ 1 2 1 ]
   i=11 [ 1 2 2 ]
   i=11 [ 1 2 3 ]
    rep= 12 4 0

    '''
    result = [[0] * len(qreg)]
    rows = np.prod(qreg)
    cols = len(qreg)

    col_list = []

    for i, q in enumerate(qreg):
        rept = np.prod(qreg[i + 1:])
        times = np.prod(qreg[:i])
        # print(rept, times)
        col = np.array([x for x in range(q)])
        col = np.repeat(col, rept)
        col = [*col] * int(times)
        col_list += [np.array(col)]

    arr = np.array(col_list)

    return np.swapaxes(arr, 0, 1)
