from abc import ABC
from qudiet.circuit_library.standard_gates.quantum_gate import QuantumGate as QuantumGate
from qudiet.core.backend.core import Backend as Backend
from qudiet.utils.linalg import ttg as ttg
from qudiet.utils.numpy import get_index as get_index
from scipy import sparse as sparse
from scipy.sparse import csr_matrix as csr_matrix
from typing import Any, Tuple

class CXGate(QuantumGate, ABC):
    backend: Any
    def __init__(self, qreg: tuple[int, int], acting_on: tuple[int, int], plus: int, backend: Backend) -> None: ...
    @property
    def dims(self) -> int: ...
    @property
    def is_controlled(self) -> bool: ...
    @property
    def is_single_qudit(self) -> bool: ...
    @property
    def unitary(self) -> sparse: ...
    @staticmethod
    def update(index, row, plus, target, target_i): ...
    @property
    def acting_on(self) -> Tuple[int, int]: ...
