from qudiet.core.quantum_circuit import QuantumCircuit

n = 4
qc = QuantumCircuit(qregs=[4 for i in range(n)], init_states=[3, 0, 0, 0])

# qc.cx((1, 1), 1)
# qc.toffoli(([0, 1, 2], 2), 1)
# qc.z(4)

ctrls, tgt = [[0], [0, 2], [0, 1, 2]], n-1

for i in range(n-1):
	# ctrls.append(i)
	print(ctrls[i])
	qc.toffoli((ctrls[i], tgt), 1)
	qc.measure_all()
	# print(qc)
	# qc = QuantumCircuit(qregs=[4 for i in range(n)], init_states=[0, 3, 0])

qc.measure_all()
print(qc)

# try:
# 	print(qc.run())
# except Exception as e:
# 	print(f'failure\n{e}')

# for moment in qc.op_flow.peek():
# 	print(moment.peek_list()[1])
# qc.toffoli(([0], 3), 1)
# qc.toffoli(([0, 1], 3), 1)
# qc.toffoli(([0, 1, 2], 3), 1)
# print(qc)
# print(qc.op_flow.peek()[1].peek_list()[0].qreg)