from abc import ABC
from typing import Union

import numpy as np
from scipy import sparse
from scipy.linalg import circulant
from scipy.sparse import csr_matrix

from circuit_library.standard_gates.quantum_gate import QuantumGate


class CXGate(QuantumGate, ABC):
    def __init__(self,
                 qreg: "tuple[int, int]",
                 dims: int
                 ):
        """
        This generates the CX Gate object for a given set of dimension and a qreg tuple representing control and target.
        :param qreg: (control, target). This represents the control and the target qudits on which the CXGate shall act
                     on. This is a two qudit quantum gate.
        :param dims: This represents the dimensions of the CXGate
        """
        self._qreg = qreg
        self._dims = dims

    @property
    def is_controlled(self) -> bool:
        """
        Check if the gate is controlled or not
        :return: True or False, depending on the scenario
        """
        return True

    @property
    def is_single_qudit(self) -> bool:
        """
        Check if the gate is a single qudit or multi-qudit
        :return: True or False, depending on the scenario
        """
        return False

    @property
    def unitary(self) -> sparse:
        """
        This is the gate unitary which shall be used to do any calculations
        :return: The gate unitary
        """

        _x_unitary_builder = np.zeros(shape=(self._dims, 1))
        _x_unitary_builder[1] = 1
        _x_unitary = csr_matrix(circulant(_x_unitary_builder))

        _O = np.zeros((self._dims, self._dims))
        _I = np.eye(self._dims)

        for _ in range(self._dims):
            _hstack_list = []
            for __ in range(self._dims):
                _hstack_p = [_O for _ in range(__)]
                _hstack_m = _x_unitary if _ == __ == (self._dims - 1) else _I
                _hstack_s = [_O for _ in range(self._dims - __ - 1)]

                _hstack_list += [np.hstack((*_hstack_p, _hstack_m, *_hstack_s))]

            _vstack_list = np.vstack(_hstack_list)

        return csr_matrix(_vstack_list)

    @property
    def acting_on(self) -> Union[int, list]:
        """
        Gets the index of the acting qudit in the QuantumRegister
        :return: Index of the QuantumRegister if it is a single qudit gate or a list if multiqudit
        """
        return 0
