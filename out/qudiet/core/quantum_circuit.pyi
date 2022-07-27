from qudiet.circuit_library.standard_gates.cx import CXGate as CXGate
from qudiet.circuit_library.standard_gates.h import HGate as HGate
from qudiet.circuit_library.standard_gates.i import IGate as IGate
from qudiet.circuit_library.standard_gates.measurement import Measurement as Measurement
from qudiet.circuit_library.standard_gates.x import XGate as XGate
from qudiet.circuit_library.standard_gates.z import ZGate as ZGate
from qudiet.core.backend import DefaultBackend as DefaultBackend
from qudiet.core.backend.SparseBackend import SparseBackend as SparseBackend
from qudiet.core.backend.core import Backend as Backend
from qudiet.core.init_states import InitState as InitState
from qudiet.core.moment import Moment as Moment
from qudiet.core.operator_flow import OperatorFlow as OperatorFlow
from qudiet.core.output import Output as Output, OutputMethod as OutputMethod, OutputType as OutputType
from qudiet.utils.linalg import isiterable as isiterable
from typing import Any, Optional, Union
from typing_extensions import Literal

class QuantumCircuit:
    backend: Any
    debug_backend: Any
    output_processor: Any
    qregs: Any
    cregs: Any
    name: Any
    init_states: Any
    op_flow: Any
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
