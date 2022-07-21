from _typeshed import Incomplete
from scipy import sparse as sparse

class InitState:
    dim: Incomplete
    state: Incomplete
    qreg: Incomplete
    init_state: Incomplete
    def __init__(self, dim: int, state: int, qreg: int) -> None: ...
    def get_init_states(self) -> sparse: ...
    @property
    def unitary(self) -> sparse: ...
