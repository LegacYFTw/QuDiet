from qudiet.core.backend.core import Backend as Backend

class SparseBackend(Backend):
    @staticmethod
    def kron(a, b): ...
    @staticmethod
    def dot(a, b): ...
    @staticmethod
    def eye(n, m): ...
    @staticmethod
    def matrix(a): ...
    @staticmethod
    def nonzero(a): ...