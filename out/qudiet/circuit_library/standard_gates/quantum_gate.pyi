import abc
from abc import ABC, abstractmethod
from scipy import sparse as sparse
from typing import Union

class QuantumGate(ABC, metaclass=abc.ABCMeta):
    @property
    @abstractmethod
    def is_controlled(self) -> bool: ...
    @property
    @abstractmethod
    def is_single_qudit(self) -> bool: ...
    @property
    @abstractmethod
    def unitary(self) -> sparse: ...
    @property
    @abstractmethod
    def acting_on(self) -> Union[int, list]: ...
