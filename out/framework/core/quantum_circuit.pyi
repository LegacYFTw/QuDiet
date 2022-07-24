from _typeshed import Incomplete
from framework.circuit_library.standard_gates.cx import CXGate as CXGate
from framework.circuit_library.standard_gates.h import HGate as HGate
from framework.circuit_library.standard_gates.i import IGate as IGate
from framework.circuit_library.standard_gates.measurement import Measurement as Measurement
from framework.circuit_library.standard_gates.x import XGate as XGate
from framework.circuit_library.standard_gates.z import ZGate as ZGate
from framework.core.backend import DefaultBackend as DefaultBackend
from framework.core.backend.SparseBackend import SparseBackend as SparseBackend
from framework.core.backend.core import Backend as Backend
from framework.core.init_states import InitState as InitState
from framework.core.moment import Moment as Moment
from framework.core.operator_flow import OperatorFlow as OperatorFlow
from framework.core.output import Output as Output, OutputMethod as OutputMethod, OutputType as OutputType
from framework.utils.linalg import isiterable as isiterable
from typing import Literal, Optional, Union

class QuantumCircuit:
    backend: Incomplete
    debug_backend: Incomplete
    output_processor: Incomplete
    qregs: Incomplete
    cregs: Incomplete
    name: Incomplete
    init_states: Incomplete
    op_flow: Incomplete
    def __init__(self, qregs: Union[tuple[int, int], list[int]], cregs: Optional[int] = ..., name: Optional[str] = ..., init_states: Optional[list[int]] = ..., backend: Backend = ..., output: Output = ..., debug: bool = ...) -> None: ...
    def get_circuit_config(self): ...
    def h(self, qreg: int, dims: Optional[int] = ...) -> bool: ...
    def x(self, qreg: int, dims: Optional[int] = ..., plus: Optional[int] = ...) -> bool: ...
    def z(self, qreg: int, dims: Optional[int] = ...) -> bool: ...
    def toffoli(self, qreg, plus: int = ...) -> bool: ...
    def cx(self, acting_on: tuple[int, int], plus: int, dims: Optional[int] = ...) -> bool: ...
    def measure(self, qreg: int) -> NotImplementedError: ...
    def measure_all(self) -> Literal[True]: ...
    def run(self): ...
    def print_opflow_list(self) -> None: ...
