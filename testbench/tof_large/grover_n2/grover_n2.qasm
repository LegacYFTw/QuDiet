# Created by Arnav Das
# Grover's with 2 qudits.

.qudit 2

qudit x0
qudit x1

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
