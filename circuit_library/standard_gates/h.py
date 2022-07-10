import math
from abc import ABC
from typing import Union

import numpy as np
from numba import njit
from scipy.linalg import circulant
from scipy.sparse import csr_matrix

from circuit_library.standard_gates.quantum_gate import QuantumGate


class HGate(QuantumGate, ABC):
    @njit
    def __init__(self,
                 qreg: int,
                 dims: int
                 ):
        """
        This generates the Hadamard Gate object for a given set of dimensions and a qreg number
        :param qreg: Integer representing the id of the quantum register
        :param dims: Integer representing the dimension of the gate
        """
        self.qreg = qreg
        self.dims = dims

    @property
    @njit
    def is_controlled(self) -> bool:
        """
        Check if the gate is controlled or not
        :return: True or False, depending on the scenario
        """
        return False

    @property
    @njit
    def is_single_qudit(self) -> bool:
        """
        Check if the gate is a single qudit or multi-qudit
        :return: True or False, depending on the scenario
        """

        return True

    @property
    @njit
    def unitary(self) -> csr_matrix:
        """
        This is the gate unitary which shall be used to do any calculation
        :return: The gate unitary
        """
        _roots_of_unity_build_list = np.zeros(self.dims + 1)
        _roots_of_unity_build_list[0] = 1
        _roots_of_unity_build_list[self.dims] = -1
        _roots_of_unity = np.roots(_roots_of_unity_build_list)
        _usable_roots_of_unity = np.delete(_roots_of_unity, len(_roots_of_unity) - 1)
        _unitary_builder = circulant(_usable_roots_of_unity)
        _unitary_builder_first_row = np.ones(len(_usable_roots_of_unity))
        _unitary_first = np.vstack([_unitary_builder_first_row, _unitary_builder])
        _unitary_first_column = np.ones(len(_usable_roots_of_unity) + 1)
        _unitary_unnormalized = np.c_[_unitary_first_column, _unitary_first]
        _unitary = 1 / (math.sqrt(self.dims)) * _unitary_unnormalized

        return csr_matrix(_unitary)

    @property
    @njit
    def acting_on(self) -> Union[int, list]:
        """
        Gets the index of the acting qudit in the QuantumRegister
        :return: Index of the QuantumRegister if it is a single qudit gate or a list if multiqudit
        """
        return self.qreg
