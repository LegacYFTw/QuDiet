from abc import ABC
from typing import Union

from scipy import sparse

from quantum_gate import QuantumGate


class IGate(QuantumGate, ABC):
    def __init__(self,
                 qreg: int,
                 dims: int
                 ):
        """
        This generates the Identity Gate object for a given set of dimensions and a qreg number
        :param qreg: Integer representing the id of the quantum register
        :param dims: Integer representing the dimension of the gate
        """
        self.qreg = qreg
        self.dims = dims

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
    def unitary(self) -> sparse:
        """
        This is the gate unitary which shall be used to do any calculation
        :return: The gate unitary
        """
        return sparse.eye(n=self.dims, m=self.dims)

    @property
    def acting_on(self) -> Union[int, list]:
        """
        Gets the index of the acting qudit in the QuantumRegister
        :return: Index of the QuantumRegister if it is a single qudit gate or a list if multiqudit
        """
        return self.qreg
