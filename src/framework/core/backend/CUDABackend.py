from framework.core.backend.core import Backend
from cupyx.scipy import sparse

class CUDABackend(Backend):

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
        return sparse.csr_matrix(a)
    
    @staticmethod
    def nonzero(a):
        return a.nonzero()