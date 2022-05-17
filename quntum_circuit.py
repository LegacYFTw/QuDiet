import copy
import itertools
import math

import numpy as np
from scipy import sparse
from scipy.linalg import circulant
from scipy.sparse import csr_matrix, csc_matrix, coo_matrix

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
        self.circuit_data = self.generate_circuit_data()
        self.register_length = self.register_length()

    def register_length(self):
        """"
        Returns the size of the quantum register
        """
        qregs = self.qregs
        size_of_register = 0
        if type(qregs) == tuple:
            print("Tuple")
            size_of_register = qregs[0]
        elif type(qregs) == list:
            print("List")
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
                full_config["wire_{0}".format(idx)] = qregs[1]
        elif type(qregs) == list:
            for idx in range(len(qregs)):
                full_config["wire_{0}".format(idx)] = qregs[idx]

        return full_config

    def initialize_states(self):
        """
        Initializes the qudits to |0> state
        """
        circuit_config = self.circuit_data
        # dim_0 = list(circuit_config.keys())[0]
        # init_0 = sparse.eye(m=2**dim_0, n=1)
        init_state = sparse.eye(m = (list(circuit_config.values())[0]), n = 1)
        if len(circuit_config.keys()) > 1:
            for idx in range(1, len(circuit_config)):
                init_2_idx = sparse.eye(m = (list(circuit_config.values())[idx]), n = 1)
                init_state = sparse.kron(init_state, init_2_idx)
        return init_state

    def h(self,
          qudit: int,
          ):
        """
        Applies the generalised Hadamard gate
        """
        circuit_config = self.circuit_data
        if qudit > len(circuit_config):
            raise IndexError('Qudit specified is out of range.')

        dim = circuit_config['wire_{0}'.format(qudit)]
        roots_of_unity_build_list = np.zeros(len(circuit_config) + 1)
        roots_of_unity_build_list[0] = 1
        roots_of_unity_build_list[len(circuit_config)] = -1
        roots_of_unity = np.roots(roots_of_unity_build_list)
        # print("============================================")
        # print("Roots of Unity are: ", roots_of_unity)
        # print("============================================")
        final_roots_of_unity = np.delete(roots_of_unity, len(roots_of_unity) - 1)
        # print("============================================")
        # print("Final roots of Unity are: ", final_roots_of_unity)
        # print("============================================")
        circulant_matrix = circulant(final_roots_of_unity)
        first_row_circ = np.ones(len(final_roots_of_unity))
        circ_first = np.vstack([first_row_circ, circulant_matrix])
        first_col_circ = np.ones(len(final_roots_of_unity) + 1)
        circulant_final = np.c_[first_col_circ, circ_first]
        # print("============================================")
        # print("Circulant matrix is given by: ", circulant_final)
        # print("============================================")
        h_gate = 1 / (math.sqrt(dim)) * circulant_final

        h_gate = csr_matrix(h_gate)

        if qudit != 0:
            gate_state = sparse.eye(m = (list(circuit_config.values())[0]))
            if len(circuit_config.keys()) > 1:
                for idx in range(1, len(circuit_config)):

                    if idx == qudit:
                        gate_state = sparse.kron(gate_state, h_gate)
                    else:
                        gate_2_idx = sparse.eye(m = (list(circuit_config.values())[idx]))
                        gate_state = sparse.kron(gate_state, gate_2_idx)

        else:
            gate_state = h_gate
            if len(circuit_config.keys()) > 1:
                for idx in range(1, len(circuit_config)):
                    gate_2_idx = sparse.eye(m = (list(circuit_config.values())[idx]))
                    gate_state = sparse.kron(gate_state, gate_2_idx)

        return gate_state

    def x(self,
          qubit: int,
          dim: int,
          ):
        """
        Applies the generalised X Pauli Matrix
        """
        pass
