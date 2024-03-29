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

import numpy as np

from qudiet.core.backend.NumpyBackend import NumpyBackend
from qudiet.core.backend.SparseBackend import SparseBackend
from qudiet.core.quantum_circuit import QuantumCircuit
from qudiet.circuit_library import ArbitaryGate
from qudiet.circuit_library.standard_gates.i import IGate
from qudiet.utils.numpy import Nbase_to_bin


def test_qudit_init():
    qc = QuantumCircuit(
        qregs=[2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2],
        init_states=[1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    )
    qc.measure_all()
    result = qc.run()

    assert result == [{"|1110100000000>": 1.0}]


def test_qudit_test():
    qc = QuantumCircuit(
        qregs=[ 4, ],
        init_states=[ 3, ],
    )
    qc.h(0)
    qc.measure_all()
    result = qc.run()

    assert result

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


def test_circuit_config():
    qc = QuantumCircuit(
        qregs=[2, 3, 3, 3, 2],
        init_states=[1, 1, 1, 2, 1],
    )
    qc.cx([3, 1], 1)
    qc.h(0)
    qc.cx([1, 2], 1)
    qc.measure_all()

    config = qc.get_circuit_config()
    assert config["width"] == 5
    assert config["depth"] == 2


def test_qudit_hadamard():
    qc = QuantumCircuit(qregs=[2, 3], init_states=[0, 0], backend=NumpyBackend)
    qc.h(0)
    qc.cx([0, 1], 1)
    qc.measure_all()
    result = qc.run()

    assert result == [
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


def test_qudit_multi_controlled_toffoli():
    qc = QuantumCircuit(
        qregs=[2, 3, 4, 3, 2],
        # init_states=[1, 2, 2, 0, 1],
        init_states=[1, 2, 3, 0, 1],
    )
    qc.toffoli(([0, 1, 2], 3))
    # qc.multi_controlled_toffoli(([0, 1, 2], 3))
    qc.measure_all()
    result = qc.run()

    assert result == [{"|12311>": 1.0}] # 12311


def test_arbitary_gate():
    class GateXYZ(ArbitaryGate):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            k = 1
            self._unitary = np.array([[k, 0, 0], [0, k, 0], [0, 0, k], ])

    qc = QuantumCircuit(
        qregs=[2, 3, 4, 3, 2],
        init_states=[1, 2, 2, 0, 1],
        backend=SparseBackend,
    )
    qc.gate(GateXYZ, 3)
    qc.measure_all()
    result = qc.run()

    assert result == [{'|12201>': 1.0}]
