from quntum_circuit import QuantumCircuit

quantum_circuit = QuantumCircuit((300, 12), cregs = 2)

# qreg_length = quantum_circuit.register_length()
circuit_data = quantum_circuit.generate_circuit_data()
# print(qreg_length)
init_state = quantum_circuit.initialize_states()
print(init_state.toarray().shape)
print(circuit_data)
