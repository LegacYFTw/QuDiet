# Created by Arnav Das
# Grover's with 2 qubits.

.qubit 2

qubit x0
qubit x1

.begin
H x0
H x1

H x1
CNOT x0 x1
H x1

H x0
H x1
x x0
x x1
H x1
CNOT x0 x1
H x1
x x0
x x1

H x0
H x1
.end
