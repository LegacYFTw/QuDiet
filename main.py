from core.quantum_circuit import QuantumCircuit

qc = QuantumCircuit(qregs=[3, 4, 3, 3], init_states=[0, 0, 0, 0])

qc.h(qreg=0, dims=3)
qc.z(qreg=1, dims=3)
qc.x(qreg=2, dims=3)
qc.h(qreg=0, dims=3)
qc.z(qreg=1, dims=3)
qc.x(qreg=2, dims=3)
qc.h(qreg=3, dims=3)
qc.cx(acting_on=(1, 3), plus=2)


qc.measure_all()
qc.print_opflow_list()
print(qc.run())