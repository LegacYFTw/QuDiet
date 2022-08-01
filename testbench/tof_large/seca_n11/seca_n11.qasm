# Created by Arnav Das
# Shor's error correction algorithm witH 11 qubits.

.qubit 11

qubit x0
qubit x1
qubit x2
qubit x3
qubit x4
qubit x5
qubit x6
qubit x7
qubit x8
qubit x9
qubit x10

.begin
Z x0
H x0 # secret unitary: hz

# barrier q # Shor's error correction algorithm
CNOT x0 x3
CNOT x0 x6
CNOTZ x0 x3
CNOTZ x0 x6
H x0
H x3
H x6
Z x0
Z x3
Z x6
CNOT x0 x1
CNOT x0 x2
CNOT x3 x4
CNOT x3 x5
CNOT x6 x7
CNOT x6 x8
CNOTZ x0 x1
CNOTZ x0 x2
CNOTZ x3 x4
CNOTZ x3 x5
CNOTZ x6 x7
CNOTZ x6 x8

# Alice starts with qubit 9.
# Bob starts with qubit 10.
# Alice is given qubit 0.
# Bob is given error-correcting qubits 1-8.
# Alice and Bob do not know what has been done to qubit 0.

# barrier q # Alice and Bob entangle their starting qubits.
H x9
CNOT x9 x10

# Alice keeps qubits 0 and 9.
# Bob leaves with qubits 1-8 and 10.

# barrier q # Alice teleports the quantum state of qubit 0 to Bob's qubit.
CNOT x0 x9

H x0
CNOT x9 x10

CNOTZ x0 x10

# barrier q # Bob corrects for bit flips and sign flips
CNOT x10 x1
CNOT x10 x2
CNOT x3 x4
CNOT x3 x5
CNOT x6 x7
CNOT x6 x8
CNOTZ x10 x1
CNOTZ x10 x2
CNOTZ x3 x4
CNOTZ x3 x5
CNOTZ x6 x7
CNOTZ x6 x8
Toffoli x1 x2 x10
Toffoli x5 x4 x3
Toffoli x8 x7 x6
# barrier q # start CCNOTZ gates
H x10
Toffoli x1 x2 x10
H x10
H x3
Toffoli x5 x4 x3
H x3
H x6
Toffoli x8 x7 x6
H x6
# barrier q # end CNOTZ gates
H x10
H x3
H x6
Z x10
Z x3
Z x6
CNOT x10 x3
CNOT x10 x6
CNOTZ x10 x3
CNOTZ x10 x6
Toffoli x3 x6 x10
H x10
Toffoli x3 x6 x10
H x10

# 00 do nothing
# 01 apply X
# 10 apply Z
# 11 apply ZX
H x10
Z x10
.end
