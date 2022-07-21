import numpy as np
from numba import njit


def get_index(src, trgt):
    for i, v in enumerate(src):
        if np.all(v == trgt):
            return i


def bin_to_Nbase(target, base=2):
    if isinstance(base, int):
        base = [base] * len(target)
    else:
        assert len(target) == len(base)

    # base[0] = 1 # Anything to the power of 0 is 1
    scale = np.array(base[::-1]).cumprod()
    scale = [1, *scale[:-1]]
    return np.sum(scale[::-1] * np.array(target))


def Nbase_to_bin(_repr, base=2):
    if isinstance(base, int):
        base = [base] * 998
    base = base[::-1]
    digits = []
    while _repr:
        _base = base[len(digits)]
        digits += [int(_repr % _base)]
        _repr //= _base
    return digits[::-1]
