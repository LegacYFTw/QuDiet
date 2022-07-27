from abc import ABC
from framework.circuit_library.standard_gates.quantum_gate import QuantumGate as QuantumGate
from framework.core.backend.core import Backend as Backend
from scipy import sparse as sparse
from typing import Any

class IGate(QuantumGate, ABC):
    qreg: Any
    dims: Any
    backend: Any
    def __init__(self, qreg: int, dims: int, backend: Backend) -> None: ...
    @property
    def is_controlled(self) -> bool: ...
    @property
    def is_single_qudit(self) -> bool: ...
    @property
    def unitary(self) -> sparse: ...
    @property
    def acting_on(self) -> int: ...
