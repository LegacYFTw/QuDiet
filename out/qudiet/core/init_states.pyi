from _typeshed import Incomplete
from qudiet.core.backend.core import Backend as Backend
from scipy import sparse as sparse
from scipy.sparse import csr_matrix as csr_matrix, dok_matrix as dok_matrix

class InitState:
    dim: Incomplete
    state: Incomplete
    qreg: Incomplete
    init_state: Incomplete
    backend: Incomplete
    def __init__(self, dim: int, state: int, qreg: int, backend: Backend) -> None: ...
    def get_init_states(self) -> sparse: ...
    @property
    def unitary(self) -> sparse: ...
