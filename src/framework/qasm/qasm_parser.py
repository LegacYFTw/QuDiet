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

import re
from unittest import result

from framework.core.quantum_circuit import QuantumCircuit
from framework.utils.numpy import Nbase_to_bin


def parse_qasm(filename: str):
    # TODO : Need to create a proper reader.
    with open(filename, "r") as f:
        # _data = list(filter(None, f.read().split("\n")))
        _data = re.split("\n\.(qudit\s\d+|begin|end)", f.read())
        _data.pop(6)
        _data.pop(5)
        _data.pop(3)
        _data.pop(1)
        _data.pop(0)

    _qregs = [
        int(re.findall("\d+", _dims)[0]) for _dims in re.findall("\d+\)", _data[0])
    ]
    qc = QuantumCircuit(qregs=_qregs)

    _gates = list(filter(None, _data[1].split("\n")))

    for _gate in _gates:
        if re.search("^X", _gate):
            _gate_qreg = int(re.findall("\d+", _gate.split()[1])[0])
            qc.x(qreg=_gate_qreg)

        if re.search("^H", _gate):
            _gate_qreg = int(re.findall("\d+", _gate.split()[1])[0])
            qc.h(qreg=_gate_qreg)

        if re.search("^Z", _gate):
            _gate_qreg = int(re.findall("\d+", _gate.split()[1])[0])
            qc.z(qreg=_gate_qreg)

        elif re.search("^CX", _gate):
            _gate_qreg = (
                int(re.findall("\d+", _gate.split()[1])[0]),
                int(re.findall("\d+", _gate.split()[2])[0]),
            )
            if len(_gate.split()) == 4:
                _plus = int(re.findall("\d+", _gate.split()[3])[0])
            else:
                _plus = 1
            qc.cx(acting_on=_gate_qreg, plus=_plus)

    qc.measure_all()

    return qc
