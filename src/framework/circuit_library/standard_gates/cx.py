#               This file is part of the Framework package.
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
from typing import Tuple, Union

import numpy as np
from scipy import sparse
from scipy.sparse import csr_matrix

from framework.circuit_library.standard_gates.quantum_gate import QuantumGate
from framework.utils.linalg import ttg
from framework.utils.numpy import get_index


class CXGate(QuantumGate, ABC):
    def __init__(
        self, qreg: "tuple[int, int]", acting_on: "tuple[int, int]", plus: int
    ):
        """
        This generates the CX Gate object for a given set of dimension and a qreg tuple representing control and target.

        :param qreg: (control, target). This represents the control and the target qudits on which the CXGate shall act
                     on. This is a two qudit quantum gate.
        :param dims: This represents the dimensions of the CXGate
        :param acting_on: This represents the control and target qudit register for the CXGate
        :param plus: This represents the value by which the target qudit changes
        """
        self._qreg = qreg
        # self._dims = dims
        self._plus = plus
        self._acting_on = acting_on

    @property
    def dims(self) -> int:
        return np.prod(self._qreg)

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

        source_i, target_i = self.acting_on
        # When self.acting on = (1, 4) and self._qreg = [3, 4, 3, 3],
        # self._qreg[source_i] gets the value 4 and self._qreg[target_i] gives IndexError
        # as there is no value at index 4
        # So, resetting target_i to 4 - 1 = 3 and source_i = 0
        target_i = target_i - source_i
        source_i = 0
        # source denotes the dim of control qudit, source_i is the index of the
        # control qudit
        source = self._qreg[source_i]
        # target denotes the dim of target qudit, target_i is the index of the
        # target qudit
        target = self._qreg[target_i]

        # _from is the trigger condition for the CXGate
        _from = source - 1

        # Total dimension of the matrix gate
        dim = np.prod(self._qreg)

        rows = np.array([i for i in range(dim)])

        # This creates the Truth Table that is used to index the rows & cols
        index = ttg(self._qreg)

        _slice = rows[:: dim // source]
        _slice = np.array([*_slice, rows[-1]])

        _from, _to = _slice[_from], _slice[_from + 1]

        # This will act as a base matrix for our gate
        I = np.eye(dim)

        for x in range(_from, _to + 1):
            I[x] = self.update(index, I[x], self._plus, target, target_i)

        return csr_matrix(I)

    @staticmethod
    def update(index, row, plus, target, target_i):
        src_index = np.where(row == 1)[0]
        src_in_truth_table = index[src_index][0]

        # apply transform
        target_change_to = (src_in_truth_table[target_i] + abs(target - plus)) % target

        trgt_in_truth_table = src_in_truth_table.copy()
        trgt_in_truth_table[target_i] = target_change_to

        # get the index of transformed
        transformed_target_index = get_index(index, trgt_in_truth_table)

        res = np.zeros(len(row))
        res[transformed_target_index] = 1

        return res

    @property
    def acting_on(self) -> Tuple[int, int]:
        """
        Gets the index of the acting qudit in the QuantumRegister

        :return: Indices of the QuantumRegisters [Control, Target]
        """
        return self._acting_on
