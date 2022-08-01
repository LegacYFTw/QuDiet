# Created by Arnav Das

.qubit 6

qubit x0
qubit x1
qubit x2
qubit x3
qubit x4
qubit x5

# This initializes 6 quantum registers
.begin
H x0
H x1
H x2
# The first 3 qubits are put into superposition states.

CNOT x2 x4
X x3
CNOT x2 x3
Toffoli x0 x1 x3
X x0
X x1
Toffoli x0 x1 x3
X x0
X x1
X x3

# This applies the secret structure: s=110.

H x0
H x1
H x2
.end
