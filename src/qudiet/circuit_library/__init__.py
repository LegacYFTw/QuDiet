#               This file is part of the QuDiet package.
#              https://github.com/LegacYFTw/qubit-qudit-sim
#
#                      Copyright (c) 2022.
#                      --.- ..- -.. .. . -
#
# Turbasu Chatterjee, Subhayu Kumar Bala, Arnav Das
# Dr. Amit Saha, Prof. Anupam Chattopadhyay, Prof. Amlan Chakrabarti
#
#
# SPDX-License-Identifier: AGPL-3.0
#
#  This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

#               This file is part of the QuDiet package.
#              https://github.com/LegacYFTw/qubit-qudit-sim
#
#                      Copyright (c) 2022.
#                      --.- ..- -.. .. . -
#
# Turbasu Chatterjee, Subhayu Kumar Bala, Arnav Das
# Dr. Amit Saha, Prof. Anupam Chattopadhyay, Prof. Amlan Chakrabarti
#
#
# SPDX-License-Identifier: AGPL-3.0
#
#  This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import math
from abc import ABC
from typing import Union

import numpy as np
from scipy.linalg import circulant
from scipy.sparse import csr_matrix

from qudiet.circuit_library.standard_gates.quantum_gate import QuantumGate
from qudiet.core.backend.core import Backend


class ArbitaryGate(QuantumGate, ABC):
    def __init__(self, qreg: int, dims: Union[int, tuple], backend: Backend):
        """
        This generates the Hadamard Gate object for a given set of dimensions and a qreg number
        :param qreg: Integer representing the id of the quantum register
        :param dims: Integer representing the dimension of the gate
        """
        self.qreg = qreg
        self.dims = dims
        self.backend = backend

        # Blank Unitary
        self._unitary = 1

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
        if not self.backend.is_unitary(self._unitary):
            raise Exception(f"The defined gate is not \"unitary\". Please use a unitary matrix / tensor to define the gate.")

        # Dimension Check
        if type(self.dims) == int:
            assert self._unitary.shape == (self.dims, self.dims)
        elif type(self.dims) == list:
            if len(self.dims) == 1:
                assert self._unitary.shape == (self.dims[0], self.dims[0])
            if len(self.dims) == 2:
                assert self._unitary.shape == self.dims
            if len(self.dims) > 2:
                raise Exception(f'The defined gate can have `at most` connected 2 registers. One target and One for Control.')


        # Qudit Dimesnion, suppose 3, the check if the shape is 3 x 3
        # Qudit Dimesnion, suppose 2 and 3, the check if the shape is 2 x 3
        return self.backend.matrix(self._unitary)

    @property
    def acting_on(self) -> Union[int, list]:
        """
        Gets the index of the acting qudit in the QuantumRegister
        :return: Index of the QuantumRegister if it is a single qudit gate or a list if multiqudit
        """
        return self.qreg
