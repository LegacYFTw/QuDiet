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
