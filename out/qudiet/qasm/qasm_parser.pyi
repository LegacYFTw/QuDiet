from qudiet.core.backend import DefaultBackend as DefaultBackend
from qudiet.core.backend.core import Backend as Backend
from qudiet.core.quantum_circuit import QuantumCircuit as QuantumCircuit
from qudiet.utils.numpy import Nbase_to_bin as Nbase_to_bin
from unittest import result as result

def parse_qasm(filename: str, backend: Backend = ...): ...
