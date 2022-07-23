from framework.core.backend import Backend, CUDA_HOME

if CUDA_HOME:
    import cupy as cp
    from cupyx.scipy import sparse
else:
    assert False
    raise Exception("CUDA Backend is disabled.")

import os
import numpy as np

class CUDABackend(Backend):
    def __getattribute__(self, name):
        if not CUDA_HOME:
            raise Exception("CUDA Backend is disabled.")
        super().__getattribute__(name)

    @staticmethod
    def kron(a, b):
        return cp.kron(a, b)

    @staticmethod    
    def dot(a, b):
        return cp.dot(a, b)
    
    @staticmethod    
    def eye(n, m):
        return cp.eye(N=n, M=m)

    @staticmethod    
    def matrix(a):
        if isinstance(a, np.ndarray):
            a = cp.array(a)
        s = a.shape
        if len(s) == 1:
            a = a.reshape((*s, 1))
        return a
    
    @staticmethod
    def nonzero(a):
        return a.nonzero()