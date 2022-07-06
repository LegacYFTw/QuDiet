import numpy as np


def get_index(src, trgt):
    for i, v in enumerate(src):
        if np.all(v == trgt):
            return i

