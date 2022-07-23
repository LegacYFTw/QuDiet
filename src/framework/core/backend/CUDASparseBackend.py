from framework.core.backend import Backend, CUDA_HOME

if CUDA_HOME:
    from cupyx.scipy import sparse
    import cupy as cp
else:
    assert False
    raise Exception("CUDA Backend is disabled.")

import os
import numpy as np

class CUDASparseBackend(Backend):
    def __getattribute__(self, name):
        if not CUDA_HOME:
            raise Exception("CUDA Backend is disabled.")
        super().__getattribute__(name)

    @staticmethod
    def kron(a, b):
        return sparse.kron(a, b)

    @staticmethod    
    def dot(a, b):
        return sparse.csr_matrix.dot(a, b)
    
    @staticmethod    
    def eye(n, m):
        return sparse.eye(n=n, m=m)

    @staticmethod    
    def matrix(a):
        if isinstance(a, np.ndarray):
            a = cp.array(a)
        return sparse.csr_matrix(a)
    
    @staticmethod
    def nonzero(a):
        return a.nonzero()