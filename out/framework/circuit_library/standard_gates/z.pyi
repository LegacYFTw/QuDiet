from abc import ABC
from qudiet.circuit_library.standard_gates.quantum_gate import QuantumGate as QuantumGate
from qudiet.core.backend.core import Backend as Backend
from scipy.sparse import csr_matrix as csr_matrix
from typing import Any, Union

class ZGate(QuantumGate, ABC):
    qreg: Any
    dims: Any
    backend: Any
    def __init__(self, qreg: int, dims: int, backend: Backend) -> None: ...
    @property
    def is_controlled(self) -> bool: ...
    @property
    def is_single_qudit(self) -> bool: ...
    @property
    def unitary(self) -> csr_matrix: ...
    @property
    def acting_on(self) -> Union[int, list]: ...
