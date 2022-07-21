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

from framework.core.quantum_circuit import QuantumCircuit
from framework.utils.numpy import Nbase_to_bin

def test_qudit_init():
    qc = QuantumCircuit(
        qregs=[2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2],
        init_states=[1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    )
    qc.measure_all()
    result = qc.run()

    assert result.nonzero() == ([23296], [0])

def test_qudit_cx():
    qc = QuantumCircuit(
        qregs=[2, 3, 3, 3, 2],
        init_states=[1, 1, 1, 2, 1],
    )
    qc.cx([0, 3], 1)
    qc.measure_all()
    result = qc.run()

    assert result.nonzero() == ([79], [0])

def test_qudit_reverse_cx():
    qc = QuantumCircuit(
        qregs=[2, 3, 3, 3, 2],
        init_states=[1, 1, 1, 2, 1],
    )
    qc.cx([3, 1], 1)
    qc.measure_all()
    result = qc.run()

    in_base = Nbase_to_bin(result.nonzero()[0][0], [2, 3, 3, 3, 2])

    assert result.nonzero() == ([101], [0])

# def test_qudit_width_depth():
#     qc = QuantumCircuit(
#         qregs=[2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2],
#         init_states=[1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     )
#     qc.cx([1, 3], 2)
#     qc.measure_all()
#     result = qc.run()
#     qc.get_circuit_config()
