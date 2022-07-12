import time
from core.quantum_circuit import QuantumCircuit
import time

start_time = time.time()

qc = QuantumCircuit(qregs=[2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2], init_states=[1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0])

# qc.cx(acting_on=(0, 2), plus=1)
# qc.cx(acting_on=(2, 5), plus=1)
# qc.cx(acting_on=(0, 2), plus=2)
# qc.cx(acting_on=(1, 2), plus=1)
# qc.cx(acting_on=(2, 6), plus=1)
# qc.cx(acting_on=(1, 2), plus=2)
# qc.cx(acting_on=(0, 3), plus=1)
# qc.cx(acting_on=(3, 7), plus=1)
# qc.cx(acting_on=(0, 3), plus=2)
# qc.cx(acting_on=(1, 3), plus=1)
# qc.cx(acting_on=(3, 8), plus=1)
# qc.cx(acting_on=(1, 3), plus=2)
# qc.cx(acting_on=(0, 4), plus=1)
# qc.cx(acting_on=(4, 9), plus=1)
# qc.cx(acting_on=(0, 4), plus=2)
# qc.cx(acting_on=(1, 4), plus=1)
# qc.cx(acting_on=(4, 10), plus=1)
# qc.cx(acting_on=(1, 4), plus=2)
# qc.cx(acting_on=(6, 11), plus=1)
# qc.cx(acting_on=(7, 11), plus=1)
# qc.cx(acting_on=(8, 12), plus=1)
# qc.cx(acting_on=(9, 12), plus=1)
# qc.h(qreg=0)
# qc.z(qreg=1)
# qc.x(qreg=2)
# qc.h(qreg=0)
# qc.z(qreg=1)
# qc.x(qreg=2)
# qc.h(qreg=3)
# qc.cx(acting_on=(1, 3), plus=2)


qc.measure_all()
# qc.print_opflow_list()
print(qc.run())


end_time = time.time()
print(f"Time elapsed: {end_time - start_time}s")
