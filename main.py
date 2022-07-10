import time
from core.quantum_circuit import QuantumCircuit

start_time = time.time()
qc = QuantumCircuit(qregs=[3, 4, 3, 3], init_states=[2, 3, 4, 5])

qc.h(qreg=0, dims=3)
qc.z(qreg=1, dims=3)
qc.x(qreg=2, dims=3)
qc.h(qreg=0, dims=3)
qc.z(qreg=1, dims=3)
qc.x(qreg=2, dims=3)
qc.h(qreg=3, dims=3)

# qc.cx(acting_on=(0, 2), plus=4, dims=3)

qc.measure_all()
qc.print_opflow_list()
print(qc.run())

end_time = time.time()
print(f"Time elapsed: {end_time - start_time}s")