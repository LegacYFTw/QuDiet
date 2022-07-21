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


def test_qudit_init():
    qc = QuantumCircuit(
        qregs=[2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2],
        init_states=[1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    )
    qc.measure_all()
    result = qc.run()

    assert result.nonzero() == ([23296], [0])
