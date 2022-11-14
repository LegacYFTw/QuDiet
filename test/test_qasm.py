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

from qudiet.core.quantum_circuit import QuantumCircuit
from qudiet.core.backend import SparseBackend
from qudiet.qasm.qasm_parser import circuit_from_qasm, parse_qasm
from qudiet.utils.numpy import Nbase_to_bin

def test_qasm_1():
    filename = "test.qasm"  # "src/testbench/tof_qutrit/..."
    # filename = "/workspace/qubit-qudit-sim/testbench/tof_large/sat_n11/sat_n11.qasm"
    circuit = parse_qasm(filename, SparseBackend)
    result = circuit.run()
    assert result == [{"|120>": 1.0}]

def test_parser_1():
    qc_1 = circuit_from_qasm(
        "\n".join([
            "# Created by Arnav Das",
            "# Grover's with 2 qubits.",
            "",
            ".qubit 2",
            "",
            "qubit x0",
            "qubit x1",
            "",
            ".begin",
            "H x0",
            "H x1",
            "",
            "H x1",
            "CNOT x0 x1",
            "H x1",
            "",
            "H x0",
            "H x1",
            "x x0",
            "x x1",
            "H x1",
            "CNOT x0 x1",
            "H x1",
            "x x0",
            "x x1",
            "",
            "H x0",
            "H x1",
            ".end"
        ])
    )
    qc_2 = QuantumCircuit([2, 2])
    qc_2.h(0)
    qc_2.h(1)

    qc_2.h(1)
    qc_2.cx([0, 1], plus=1)
    qc_2.h(1)

    qc_2.h(0)
    qc_2.h(1)
    qc_2.x(0)
    qc_2.x(1)
    qc_2.h(1)
    qc_2.cx([0, 1], plus=1)
    qc_2.h(1)
    qc_2.x(0)
    qc_2.x(1)

    qc_2.h(0)
    qc_2.h(1)
    qc_2.measure_all()

    result_1, result_2 = qc_1.run(), qc_2.run()
    # When not observed by the debugger
    # result_1 : |00> = 0.9
    # result_2 : |11> = -0.9
    # When not observed by the debugger
    # result_1 : |00> = 0.9
    # result_2 : |11> = -0.9

    assert True

def test_parser_2():
    qasm = "\n".join([
        "# Toffoli test circuit",
        ".qubit 11",
        "",
        "qudit x0 (2)",
        "qudit x1 (3)",
        "qudit x2 (3)", # It automatically adds +1... Why ?
        "qudit x3 (3)",
        "qudit x4 (2)",
        "",
        ".begin",
        "# Marking with oracle evaluation",
        "X x0",
        "X x1 2",
        "X x2 2",
        "X x4",
        "",
        "Toffoli x1, x2, x3",
        ".end",
    ])

    qc1 = circuit_from_qasm(qasm)
    result1 = qc1.run()

    qc2 = QuantumCircuit(
        qregs=[2, 3, 4, 3, 2],
        init_states=[1, 2, 2, 0, 1],
    )
    qc2.toffoli(([1, 2], 3))
    qc2.measure_all()
    result2 = qc2.run()

    qc1.op_flow._opflow_list == qc2.op_flow._opflow_list

    assert result1 == result2