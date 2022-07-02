import numpy as np
from scipy import sparse
from scipy.linalg import circulant
from scipy.sparse import csr_matrix, csc_matrix, coo_matrix
from core.moment import Moment
from core.operator_flow import OperatorFlow
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
    def __init__(self,
                 qregs: 'Union[tuple[int, int], list[int]]',
                 cregs: Optional[int] = None,
                 name: Optional[str] = None,
                 init_states: 'Optional[list[int]]' = None,
                 ):
        """"
        x = QuantumCircuit((3,3))
        This will basically create a QuantumCircuit with RegisterLength = 3, meaning there shall be 3 qudits, with energy
        level 3 or in essence a 3 qutrit register and one classical register.

        y = QuantumCircuit([2,2,3,3])
        This will create a QuantumCircuit with RegisterLength = len(Iterable) (here 4) with the energy levels 2,2,3,3 or in
        other words this will create a two qubits and two qutrits and one classical register.
        
        :params qregs: This can either be a tuple of two integers, where the first one is the register length and the send
                       one is their dimension or a list of multiple integers each denoting their dimension.
        :params cregs: 
        :params name: 
        :params init_states: This is a list of integers, where their values correspond to the dimension and the index of each
                             number is their qreg number
        """

        if not isinstance(qregs, (tuple, list)):
            raise ValueError(
                "The registers must be defined as a tuple of two integers or a list of integers"
            )
        self.qregs = qregs
        self.cregs = cregs or 0
        self.name = name or ""
        self.init_states = init_states or []
        
        self.op_flow = OperatorFlow()

        self._is_qregs_tuple = type(self.qregs) == tuple
        self._is_qregs_list = type(self.qregs) == list

        if self._is_qregs_tuple:
            self._reg_length = self.qregs[0]
        
        elif self._is_qregs_list:
            self._reg_length = len(self.qregs[0])

        if self._reg_length > len(self.init_states):
            self.init_states.extend((self._reg_length - len(self.init_states)) * [0])


    def get_circuit_config(self):
        raise NotImplementedError

    def initialize_states(self):
        """
        Initializes the qudits to |0> state or |N> state depending on the dimensions of the qubits
        """
        if self._is_qregs_tuple:
            _init_moment = []
            for _index, _element in enumerate(self.init_states):
                # Adds Operator flow object and push the init object into Operator Flow stack
                _init_state = InitState(dim=_element, state=0, qreg=_index)
                _init_moment.append(_init_state)

        m = Moment(*_init_moment)
        self.op_flow.__populate_opflow__(m)
