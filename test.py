from quntum_circuit import QuantumCircuit

quantum_circuit = QuantumCircuit((4,4), cregs = 2)

qreg_length = quantum_circuit.register_length()
# circuit_data = quantum_circuit.generate_circuit_data()
print(qreg_length)
# print(circuit_data)
