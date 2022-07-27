from framework.core.backend.core import Backend as Backend
from scipy import sparse as sparse
from scipy.sparse import csr_matrix as csr_matrix, dok_matrix as dok_matrix
from typing import Any

class InitState:
    dim: Any
    state: Any
    qreg: Any
    init_state: Any
    backend: Any
    def __init__(self, dim: int, state: int, qreg: int, backend: Backend) -> None: ...
    def get_init_states(self) -> sparse: ...
    @property
    def unitary(self) -> sparse: ...
