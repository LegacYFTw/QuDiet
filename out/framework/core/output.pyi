from enum import Enum
from framework.utils.numpy import Nbase_to_bin as Nbase_to_bin
from typing import Any

class OutputType(Enum):
    print: int
    state: int

class OutputMethod(Enum):
    probability: int
    amplitude: int

class Output:
    base: Any
    output_type: Any
    output_method: Any
    def __init__(self, base, type: OutputType = ..., method: OutputMethod = ...) -> None: ...
    def __call__(self, result): ...
    def distribution(self) -> None: ...
    def value(self) -> None: ...
