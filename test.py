from quntum_circuit import QuantumCircuit

quantum_circuit = QuantumCircuit(qregs = [3,3,4,4], cregs = 2)
qreg_length = quantum_circuit.register_length()
print(qreg_length)