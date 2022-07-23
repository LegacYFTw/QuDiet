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

from framework.core.backend import CUDA_HOME, Backend

if CUDA_HOME:
    import cupy as cp
    from cupyx.scipy import sparse
else:
    assert False
    raise Exception("CUDA Backend is disabled.")

import os

import numpy as np


class CUDABackend(Backend):
    def __getattribute__(self, name):
        if not CUDA_HOME:
            raise Exception("CUDA Backend is disabled.")
        super().__getattribute__(name)

    @staticmethod
    def kron(a, b):
        return cp.kron(a, b)

    @staticmethod
    def dot(a, b):
        return cp.dot(a, b)

    @staticmethod
    def eye(n, m):
        return cp.eye(N=n, M=m)

    @staticmethod
    def matrix(a):
        if isinstance(a, np.ndarray):
            a = cp.array(a)
        s = a.shape
        if len(s) == 1:
            a = a.reshape((*s, 1))
        return a

    @staticmethod
    def nonzero(a):
        return a.nonzero()
