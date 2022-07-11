from core.quantum_circuit import QuantumCircuit

qc = QuantumCircuit(qregs=[4, 4, 3, 2], init_states=[0, 0, 0, 0])

qc.h(qreg=0)
qc.z(qreg=1)
qc.x(qreg=2)
qc.h(qreg=0)
qc.z(qreg=1)
qc.x(qreg=2)
qc.h(qreg=3)
qc.cx(acting_on=(1, 3), plus=2)


qc.measure_all()
qc.print_opflow_list()
print(qc.run())