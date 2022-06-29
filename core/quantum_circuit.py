import numpy as np
from scipy import sparse
from scipy.linalg import circulant
from scipy.sparse import csr_matrix, csc_matrix, coo_matrix
from init_states import InitState

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
                 name: Optional[str] = None,
                 init_state: Optional[List[int]] = None,
                 ):
        if not isinstance(qregs, (Tuple, List)):
            raise ValueError(
                "The registers must be defined as a tuple of two integers or a list of integers"
            )
        self.qregs = qregs
        self.cregs = cregs
        self.name = name
        self.init_state = init_state

    def get_circuit_config(self):
        raise NotImplementedError

    def initialize_states(self):
        """
        Initializes the qudits to |0> state or |N> state depending on the dimensions of the qubits
        """
        if self.init_state is None:
            # If init states are None, we will initialize all the qudits to |0> state
            if type(self.qregs) == Tuple:
                for _ckt in range(self.qregs[0]):
                    # TODO: Add Operator flow object and push the init object into Operator Flow stack

                    pass
            pass
