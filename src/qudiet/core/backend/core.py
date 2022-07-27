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


class Backend:
    def __init__(self):
        pass

    def __call__(self):
        pass

    @staticmethod
    def kron(self, a, b):
        raise NotImplemented()

    @staticmethod
    def dot(self, a, b):
        raise NotImplemented()

    @staticmethod
    def eye(self, n, m):
        raise NotImplemented()

    @staticmethod
    def matrix(self, a):
        raise NotImplemented()

    @staticmethod
    def nonzero(self, a):
        raise NotImplemented()
