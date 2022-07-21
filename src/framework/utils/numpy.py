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


def get_index(src, trgt):
    for i, v in enumerate(src):
        if np.all(v == trgt):
            return i


def bin_to_Nbase(target, base=2):
    if isinstance(base, int):
        base = [base] * len(target)
    else:
        assert len(target) == len(base)

    # base[0] = 1 # Anything to the power of 0 is 1
    scale = np.array(base[::-1]).cumprod()
    scale = [1, *scale[:-1]]
    return np.sum(scale[::-1] * np.array(target))


def Nbase_to_bin(_repr, base=2):
    if isinstance(base, int):
        base = [base] * 998
    base = base[::-1]
    digits = []
    while _repr:
        _base = base[len(digits)]
        digits += [int(_repr % _base)]
        _repr //= _base
    return digits[::-1]
