
import time
from framework.core.quantum_circuit import QuantumCircuit

def test(): 
    qc = QuantumCircuit(qregs=[3, 3, 3], init_states=[0, 0, 0])
    qc.cx((0, 1), plus=1)
    qc.cx((1, 2), plus=1)
    qc.cx((2, 0), plus=1)
    qc.cx((1, 2), plus=1)
    qc.x(2)
    qc.cx((2, 1), plus=1)
    qc.cx((0, 2), plus=1)
    qc.cx((1, 2), plus=1)
    qc.cx((2, 0), plus=1)
    qc.cx((1, 2), plus=1)

    qc.measure_all()
    qc.run()

start = time.time()
test()
end = time.time()
print(end-start)