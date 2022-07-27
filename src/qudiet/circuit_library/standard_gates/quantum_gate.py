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

from abc import ABC, abstractmethod
from typing import Union

from scipy import sparse


class QuantumGate(ABC):
    """
    The QuantumGate abstract class presents a template of all quantum gates to be constructed.
    """

    @property
    @abstractmethod
    def is_controlled(self) -> bool:
        """
        Check if the gate is controlled or not
        :return: True or False, depending on the scenario
        """
        pass

    @property
    @abstractmethod
    def is_single_qudit(self) -> bool:
        """
        Check if the gate is a single qudit or multi-qudit
        :return: True or False, depending on the scenario
        """
        pass

    @property
    @abstractmethod
    def unitary(self) -> sparse:
        """
        This is the gate unitary which shall be used to do any calculations
        :return: The gate unitary
        """
        pass

    @property
    @abstractmethod
    def acting_on(self) -> Union[int, list]:
        """
        Gets the index of the acting qudit in the QuantumRegister
        :return: Index of the QuantumRegister if it is a single qudit gate or a list if multiqudit
        """
        pass
