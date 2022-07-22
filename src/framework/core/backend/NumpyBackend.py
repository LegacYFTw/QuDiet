from framework.core.backend.core import Backend
import numpy as np

class NumpyBackend(Backend):

    @staticmethod
    def kron(a, b):
        return np.kron(a, b)

    @staticmethod    
    def dot(a, b):
        return np.dot(a, b)
    
    @staticmethod    
    def eye(n, m):
        return np.eye(N=n, M=m)

    @staticmethod    
    def matrix(a):
        a = np.array(a)
        s = a.shape
        if len(s) == 1:
            a = a.reshape((*s, 1))
        return a
    
    @staticmethod
    def nonzero(a):
        return a.nonzero()