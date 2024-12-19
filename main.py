import time
from qudiet.core.quantum_circuit import QuantumCircuit
from qudiet.core.backend.SparseBackend import SparseBackend
from qudiet.core.backend.NumpyBackend import NumpyBackend

from collections import Counter

start_time = time.time()

# backend = SparseBackend
backend = NumpyBackend

# qc = QuantumCircuit(
#     qregs=[2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2],
#     init_states=[1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     backend=backend
# )

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


qc = QuantumCircuit(
    qregs=[3, ],
    init_states=[0, ],
    backend=backend,
    shots=1024
)
qc.h(0)

qc.measure_all()

result = qc.run()

end_time = time.time()
print(f"Time elapsed: {end_time - start_time}s")
# print(f"Result: {result}")

result = Counter(result)
print(f"Result: {result}")




