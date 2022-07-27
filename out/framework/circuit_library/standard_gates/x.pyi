from abc import ABC
from framework.circuit_library.standard_gates.quantum_gate import QuantumGate as QuantumGate
from framework.core.backend.core import Backend as Backend
from scipy.sparse import csr_matrix as csr_matrix
from typing import Any, Union

class XGate(QuantumGate, ABC):
    qreg: Any
    dims: Any
    backend: Any
    plus: Any
    def __init__(self, qreg: int, dims: int, plus: int, backend: Backend) -> None: ...
    @property
    def is_controlled(self) -> bool: ...
    @property
    def is_single_qudit(self) -> bool: ...
    @property
    def unitary(self) -> csr_matrix: ...
    @property
    def acting_on(self) -> Union[int, list]: ...
