from abc import ABC
from typing import Union

from scipy import sparse

from circuit_library.standard_gates.quantum_gate import QuantumGate


class CXGate(QuantumGate, ABC):
    def __init__(self,
                 qreg: tuple[int, int],
                 dims: int
                 ):
        """
        :param qreg:
        :param dims:


        """

    @property
    def is_controlled(self) -> bool:
        """
        Check if the gate is controlled or not
        :return: True or False, depending on the scenario
        """
        return True

    @property
    def is_single_qudit(self) -> bool:
        """
        Check if the gate is a single qudit or multi-qudit
        :return: True or False, depending on the scenario
        """
        return False

    @property
    def unitary(self) -> sparse:
        """
        This is the gate unitary which shall be used to do any calculations
        :return: The gate unitary
        """
        return None

    @property
    def acting_on(self) -> Union[int, list]:
        """
        Gets the index of the acting qudit in the QuantumRegister
        :return: Index of the QuantumRegister if it is a single qudit gate or a list if multiqudit
        """
        return 0
