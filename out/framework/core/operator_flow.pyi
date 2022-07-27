from qudiet.circuit_library.standard_gates.cx import CXGate as CXGate
from qudiet.circuit_library.standard_gates.h import HGate as HGate
from qudiet.circuit_library.standard_gates.measurement import Measurement as Measurement
from qudiet.circuit_library.standard_gates.x import XGate as XGate
from qudiet.circuit_library.standard_gates.z import ZGate as ZGate
from qudiet.core.backend import DefaultBackend as DefaultBackend
from qudiet.core.moment import Moment as Moment
from scipy import sparse as sparse
from typing import Any

class OperatorFlow:
    debug: bool
    debugger: Any
    debug_backend: Any
    def __init__(self, *args: Moment) -> None: ...
    def peek(self) -> list: ...
    def populate_opflow(self, *args: Moment) -> bool: ...
    def exec(self, backend): ...
