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

import numpy as np
from scipy import sparse
from scipy.sparse import csr_matrix, dok_matrix
from framework.core.backend.core import Backend


class InitState:
    def __init__(self, dim: int, state: int, qreg: int, backend: Backend):
        """
        This is the InitState class which initializes the lines on the QuantumRegister object.

        :param dim:   Represents the dimension of the current wire. Takes integer values. Eg.: 3 represents a qutrit
                      and 4 represents a ququart state.
        :param state: Represents the state in which it is to be initialized.
        :param qreg:   Represents the position of the init state in the circuit.
        """
        if dim < state or dim < 2:
            raise ValueError("Please check values of dim and state")
        else:
            self.dim = dim
            self.state = state
            self.qreg = qreg
            # self.init_state = dok_matrix(np.zeros((dim, 1)))
            self.init_state = np.zeros((dim, 1))
            self.init_state[state] = 1
            self.backend = backend

            self.init_state = self.backend.matrix(self.init_state)

        # print("------------------------------------------------")
        # print(f"State {self.state} initialized \n")
        # print("Statevector given by: ")
        # print(self.get_init_states().todense())

    def get_init_states(self) -> sparse:
        return self.init_state

    @property
    def unitary(self) -> sparse:
        return self.init_state
