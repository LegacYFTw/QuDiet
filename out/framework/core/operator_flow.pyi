from _typeshed import Incomplete
from framework.circuit_library.standard_gates.cx import CXGate as CXGate
from framework.circuit_library.standard_gates.h import HGate as HGate
from framework.circuit_library.standard_gates.measurement import Measurement as Measurement
from framework.circuit_library.standard_gates.x import XGate as XGate
from framework.circuit_library.standard_gates.z import ZGate as ZGate
from framework.core.moment import Moment as Moment

class OperatorFlow:
    debug: bool
    debugger: Incomplete
    def __init__(self, *args: Moment) -> None: ...
    def peek(self) -> list: ...
    def populate_opflow(self, *args: Moment) -> bool: ...
    def exec(self): ...
