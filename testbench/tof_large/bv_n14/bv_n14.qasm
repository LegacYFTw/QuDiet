# Created by Arnav Das
# Bernstein-Vazirani witH 14 qudits.
# Hidden string is 1111111111111

.qudit 14

qudit x0
qudit x1
qudit x2
qudit x3
qudit x4
qudit x5
qudit x6
qudit x7
qudit x8
qudit x9
qudit x10
qudit x11
qudit x12
qudit x13

.begin
H x0
H x1
H x2
H x3
H x4
H x5
H x6
H x7
H x8
H x9
H x10
H x11
H x12
X x13
H x13

CNOT x0 x13
CNOT x1 x13
CNOT x2 x13
CNOT x3 x13
CNOT x4 x13
CNOT x5 x13
CNOT x6 x13
CNOT x7 x13
CNOT x8 x13
CNOT x9 x13
CNOT x10 x13
CNOT x11 x13
CNOT x12 x13


H x0
H x1
H x2
H x3
H x4
H x5
H x6
H x7
H x8
H x9
H x10
H x11
H x12
.end
