from _typeshed import Incomplete
from abc import ABC
from qudiet.circuit_library.standard_gates.quantum_gate import QuantumGate as QuantumGate
from qudiet.core.backend.core import Backend as Backend
from scipy import sparse as sparse

class IGate(QuantumGate, ABC):
    qreg: Incomplete
    dims: Incomplete
    backend: Incomplete
    def __init__(self, qreg: int, dims: int, backend: Backend) -> None: ...
    @property
    def is_controlled(self) -> bool: ...
    @property
    def is_single_qudit(self) -> bool: ...
    @property
    def unitary(self) -> sparse: ...
    @property
    def acting_on(self) -> int: ...
