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

from scipy import sparse
import numpy as np
from qudiet.core.backend.core import Backend


class SparseBackend(Backend):
    @staticmethod
    def kron(a, b):
        return sparse.kron(a, b)

    @staticmethod
    def dot(a, b):
        return sparse.csr_matrix.dot(a, b)

    @staticmethod
    def eye(n, m):
        return sparse.eye(n=n, m=m)

    @staticmethod
    def matrix(a):
        return sparse.csr_matrix(a)

    @staticmethod
    def nonzero(a):
        return a.nonzero()

    @staticmethod
    def is_unitary(a):
        return np.allclose(np.eye(len(a)), a.dot(a.T.conj()))