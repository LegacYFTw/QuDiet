import copy
import itertools
import numpy as np
import scipy
import dask.array as da
import functools
import re
from collections import OrderedDict, defaultdict, namedtuple
from  .exceptions import CircuitError

from typing import (
    Union,
    Optional,
    List,
    Dict,
    Tuple,
    Type,
    TypeVar,
    Sequence,
    Callable,
    Mapping,
    Set,
    Iterable,
)
import typing

class QuantumCircuit:
    """"
    x = QuantumCircuit((3,3))
    This will basically create a QuantumCircuit with RegisterLength = 3, meaning there shall be 3 qudits, with energy
    level 3 or in essence a 3 qutrit register.

    y = QuantumCircuit([2,2,3,3])
    This will create a QuantumCircuit with RegisterLength = len(Iterable) (here 4) with the energy levels 2,2,3,3 or in
    other words this will create a two qubits and two qutrits.
    """


    def __init__(self,
                 qregs: Union[Tuple[int, int], List[int]],
                 name: Optional[str] = None
                 ):
        if any(not isinstance(reg, (Tuple, List)) for reg in qregs):
            raise ValueError(
                "The registers must be defined as a tuple of two integers or a list of integers"
            )

        def register_length(qregs):
            """"
            Returns the size of the quantum register
            """
            size_of_register = 0
            if type(qregs) == Tuple:
                size_of_register = qregs(1)
            else:
                size_of_register = len(qregs)

            return size_of_register












