from _typeshed import Incomplete
from enum import Enum
from qudiet.utils.numpy import Nbase_to_bin as Nbase_to_bin

class OutputType(Enum):
    print: int
    state: int

class OutputMethod(Enum):
    probability: int
    amplitude: int

class Output:
    base: Incomplete
    output_type: Incomplete
    output_method: Incomplete
    def __init__(self, base, type: OutputType = ..., method: OutputMethod = ...) -> None: ...
    def __call__(self, result): ...
    def distribution(self) -> None: ...
    def value(self) -> None: ...
