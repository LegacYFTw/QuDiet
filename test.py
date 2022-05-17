from quntum_circuit import QuantumCircuit
import numpy as np
from scipy import sparse
np.set_printoptions(threshold=np.inf)

quantum_circuit = QuantumCircuit([3,3,3])

# qreg_length = quantum_circuit.register_length()
circuit_data = quantum_circuit.generate_circuit_data()
# print(qreg_length)
init_state = quantum_circuit.initialize_states()
hadamard = quantum_circuit.h(2)

print(init_state)
print(circuit_data)
print(hadamard)