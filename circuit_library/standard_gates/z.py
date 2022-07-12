from abc import ABC
from typing import Union

import numpy as np
from numba import njit
from scipy.sparse import csr_matrix

from circuit_library.standard_gates.quantum_gate import QuantumGate


class ZGate(QuantumGate, ABC):
    
    def __init__(self,
                 qreg: int,
                 dims: int
                 ):
        """
        This generates the Z-Pauli Gate object for a given set of dimensions and a qreg number
        :param qreg: Integer representing the id of the quantum register
        :param dims: Integer representing the dimension of the gate
        """
        self.qreg = qreg
        self.dims = dims

    @property
    
    def is_controlled(self) -> bool:
        """
        Check if the gate is controlled or not
        :return: True or False, depending on the scenario
        """
        return False

    @property
    
    def is_single_qudit(self) -> bool:
        """
        Check if the gate is a single qudit or multi-qudit
        :return: True or False, depending on the scenario
        """

        return True

    @property
    
    def unitary(self) -> csr_matrix:
        """
        This is the gate unitary which shall be used to do any calculation
        :return: The gate unitary
        """
        _roots_of_unity_build_list = np.zeros(self.dims + 1)
        _roots_of_unity_build_list[0] = 1
        _roots_of_unity_build_list[self.dims] = -1
        _roots_of_unity = np.roots(_roots_of_unity_build_list)
        _roots_of_unity = np.flipud(_roots_of_unity)
        _unitary = np.diag(np.flipud(_roots_of_unity))

        return csr_matrix(_unitary)

    @property
    
    def acting_on(self) -> Union[int, list]:
        """
        Gets the index of the acting qudit in the QuantumRegister
        :return: Index of the QuantumRegister if it is a single qudit gate or a list if multiqudit
        """
        return self.qreg
