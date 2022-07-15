from abc import ABC
from numba import njit
from typing import Union
from framework.circuit_library.standard_gates.quantum_gate import QuantumGate


class Measurement(QuantumGate, ABC):
    
    def __init__(self, qreg: int):
        self._qreg = qreg

    @property
    
    def is_controlled(self) -> bool:
        """
        Check if the gate is controlled or not
        :return: True or False, depending on the scenario
        """
        return False

    @property
    
    def is_single_qudit(self) -> bool:
        """
        Check if the gate is a single qudit or multi-qudit
        :return: True or False, depending on the scenario
        """
        return True

    @property
    
    def unitary(self) -> None:
        """
        This is the gate unitary which shall be used to do any calculations
        :return: The gate unitary
        """
        return None

    @property
    
    def acting_on(self) -> int:
        """
        Gets the index of the acting qudit in the QuantumRegister
        :return: Index of the QuantumRegister if it is a single qudit gate or a list if multiqudit
        """
        return self._qreg
