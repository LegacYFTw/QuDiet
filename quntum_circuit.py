import copy
import itertools
import numpy as np
import scipy
import dask.array as da
import functools
import re
from collections import OrderedDict, defaultdict, namedtuple

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
    x = QuantumCircuit((3,3),1)
    This will basically create a QuantumCircuit with RegisterLength = 3, meaning there shall be 3 qudits, with energy
    level 3 or in essence a 3 qutrit register and one classical register.

    y = QuantumCircuit([2,2,3,3], 1)
    This will create a QuantumCircuit with RegisterLength = len(Iterable) (here 4) with the energy levels 2,2,3,3 or in
    other words this will create a two qubits and two qutrits and one classical register.
    """

    def __init__(self,
                 qregs: Union[Tuple[int, int], List[int]],
                 cregs: Optional[int] = 1,
                 name: Optional[str] = None
                 ):
        if not isinstance(qregs, (Tuple, List)):
            raise ValueError(
                "The registers must be defined as a tuple of two integers or a list of integers"
            )
        self.qregs = qregs
        self.cregs = cregs
        self.name = name

    def register_length(self):
        """"
                    Returns the size of the quantum register
        """
        qregs = self.qregs
        size_of_register = 0
        if type(qregs) == Tuple:
            size_of_register = qregs[0]
        else:
            size_of_register = len(qregs)

        return size_of_register

    def generate_circuit_data(self):
        """
                    Expands the wires into an array of dictionaries containing the wire identity and the energy level
        """
        qregs = self.qregs
        full_config = {}
        if type(qregs) == tuple:
            for idx in range(qregs[0]):
                print("Tuple")
                full_config["wire_{0}".format(idx)] = qregs[1]
        elif type(qregs) == list:
            for idx in range(len(qregs)):
                print("List")
                full_config["wire_{0}".format(idx)] = qregs[idx]

        return full_config
