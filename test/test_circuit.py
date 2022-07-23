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

    assert result == [{"|1110100000000>": 1.0}]


def test_qudit_cx():
    qc = QuantumCircuit(
        qregs=[2, 3, 3, 3, 2],
        init_states=[1, 1, 1, 2, 1],
    )
    qc.cx([0, 3], 1)
    qc.measure_all()
    result = qc.run()

    assert result == [{"|11101>": 1.0}]


def test_qudit_reverse_cx():
    qc = QuantumCircuit(
        qregs=[2, 3, 3, 3, 2],
        init_states=[1, 1, 1, 2, 1],
    )
    qc.cx([3, 1], 1)
    qc.measure_all()
    result = qc.run()

    assert result == [{"|12121>": 1.0}]


def test_qudit_hadamard():
    from framework.core.backend.NumpyBackend import NumpyBackend

    qc = QuantumCircuit(qregs=[2, 3], init_states=[0, 0], backend=NumpyBackend)
    qc.h(0)
    qc.cx([0, 1], 1)
    qc.measure_all()
    result = qc.run()
    processed_result = Output([2, 3], OutputType.print, OutputMethod.amplitude)(result)

    assert processed_result == [
        {"|00>": 0.7071067811865475},
        {"|11>": 0.7071067811865475},
    ]


def test_qudit_toffoli():
    qc = QuantumCircuit(
        qregs=[2, 3, 4, 3, 2],
        init_states=[1, 2, 2, 0, 1],
    )
    qc.toffoli(([1, 2], 3))
    qc.measure_all()
    result = qc.run()

    assert result == [{"|12211>": 1.0}]
