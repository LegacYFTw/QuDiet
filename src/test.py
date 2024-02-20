from qudiet.core.quantum_circuit import QuantumCircuit
from qudiet.circuit_library.standard_gates.toffoli_utility import Toffoli

n = 4
qc = QuantumCircuit(qregs=[4 for i in range(n)])
ctrls, target = [], n-1

# ctrls.append(0)
# qc.toffoli((ctrls, target), 1)
# ctrls = []
# ctrls.append(0)
# ctrls.append(1)
# qc.toffoli((ctrls, target), 2)


for i in range(n-1):
	ctrls.append(i)
	print(f"({tuple(ctrls)}, {target})")
	qc.toffoli([ctrls, target], i)

qc.measure_all()
print(qc)


for index, moment in enumerate(qc.op_flow.peek()):
	print(f"{index+1}th moment")
	for op in moment.peek_list():
		print('\t', op)
		if isinstance(op, Toffoli):
			print(f'\t\t[got a Toffoli] {op.qreg}')
	print()

# class A:
# 	def __init__(self, x: list):
# 		self.x = x.copy()
# 	def __str__(self) -> str:
# 		return f"{self.x}"

# l1 = [[0], 1]
# a = A(l1)
# l1.append('bummer')
# print(a)