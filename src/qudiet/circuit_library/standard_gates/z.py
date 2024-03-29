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

from abc import ABC
from typing import Union

import numpy as np
from scipy.sparse import csr_matrix

from qudiet.circuit_library.standard_gates.quantum_gate import QuantumGate
from qudiet.core.backend.core import Backend


class ZGate(QuantumGate, ABC):
    def __init__(self, qreg: int, dims: int, backend: Backend):
        """
        This generates the Z-Pauli Gate object for a given set of dimensions and a qreg number
        :param qreg: Integer representing the id of the quantum register
        :param dims: Integer representing the dimension of the gate
        """
        self.qreg = qreg
        self.dims = dims
        self.backend = backend

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

        return self.backend.matrix(_unitary)

    @property
    def acting_on(self) -> Union[int, list]:
        """
        Gets the index of the acting qudit in the QuantumRegister
        :return: Index of the QuantumRegister if it is a single qudit gate or a list if multiqudit
        """
        return self.qreg
