import numpy as np
from numba import njit


def get_index(src, trgt):
    for i, v in enumerate(src):
        if np.all(v == trgt):
            return i

