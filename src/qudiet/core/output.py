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

from enum import Enum

import numpy as np

from qudiet.utils.numpy import Nbase_to_bin


class OutputType(Enum):
    print = 0
    state = 1


class OutputMethod(Enum):
    probability = 0
    amplitude = 1

class Output:
    def __init__(
        self,
        base,
        type: OutputType = OutputType.print,
        method: OutputMethod = OutputMethod.probability,
        append_braket: bool = True,
    ):
        self.base = base
        self.output_type = type
        self.output_method = method
        self.append_braket = append_braket

    def __call__(self, result):
        if "sparse" in str(type(result)).lower() or hasattr(result, "toarray"):
            result = result.toarray()
        value = result.nonzero()[0]
        distribution = result[value, 0]
        qoutput = []
        for (v, d) in zip(value, distribution):
            val = Nbase_to_bin(v, self.base)
            # qoutput += [{
            #     "probability": d**2,
            #     "value" : Nbase_to_bin(v, self.base)
            # }]
            state = Nbase_to_bin(v, self.base)

            qoutput += [
                {
                    (
                        f"|{''.join([str(s) for s in state])}>" if self.append_braket else f"{''.join([str(s) for s in state])}"
                        if self.output_type == OutputType.print
                        else tuple(state)
                    ): (d**2 if self.output_method == OutputMethod.probability else d)
                }
            ]
        return qoutput

    def distribution(
        self,
    ):
        pass

    def value(
        self,
    ):
        pass
