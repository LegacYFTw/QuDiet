from core.quantum_circuit import QuantumCircuit

qc = QuantumCircuit([2,2,3,3,3,2,2,2,2,2,2,2,2], init_states=[1,1,1,0,1,0,0,0,0,0,0,0,0])

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