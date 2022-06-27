import numpy as np
from scipy import sparse
from scipy.linalg import circulant
from scipy.sparse import csr_matrix, csc_matrix, coo_matrix
from init_states import NState

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
                 name: Optional[str] = None
                 ):
        if not isinstance(qregs, (Tuple, List)):
            raise ValueError(
                "The registers must be defined as a tuple of two integers or a list of integers"
            )
        self.qregs = qregs
        self.cregs = cregs
        self.name = name
        self.register_length = self.register_length()

    def initialize_states(self):
        """
        Initializes the qudits to |0> state
        """
        circuit_config = self.circuit_data
        operator_flow = self._operator_flow
        # dim_0 = list(circuit_config.keys())[0]
        # init_0 = sparse.eye(m=2**dim_0, n=1)
        init_state = sparse.eye(m=(list(circuit_config.values())[0]), n=1)
        if len(circuit_config.keys()) > 1:
            for idx in range(1, len(circuit_config)):
                init_2_idx = sparse.eye(m=(list(circuit_config.values())[idx]), n=1)
                init_state = sparse.kron(init_state, init_2_idx)

        operator_flow.push(init_state)

        return operator_flow
