from _typeshed import Incomplete
from abc import ABC
from framework.circuit_library.standard_gates.quantum_gate import QuantumGate as QuantumGate
from framework.core.backend.core import Backend as Backend
from scipy.sparse import csr_matrix as csr_matrix
from typing import Union

class XGate(QuantumGate, ABC):
    qreg: Incomplete
    dims: Incomplete
    backend: Incomplete
    plus: Incomplete
    def __init__(self, qreg: int, dims: int, plus: int, backend: Backend) -> None: ...
    @property
    def is_controlled(self) -> bool: ...
    @property
    def is_single_qudit(self) -> bool: ...
    @property
    def unitary(self) -> csr_matrix: ...
    @property
    def acting_on(self) -> Union[int, list]: ...
