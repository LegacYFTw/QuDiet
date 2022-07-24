## Time taken = 0.18038925994187593

import time
from framework.core.quantum_circuit import QuantumCircuit

def test(): 
    qc = QuantumCircuit(qregs=[2, 2, 2, 2, 3, 3, 3])

    qc.cx((3, 4), plus=1)
    qc.cx((1, 4), plus=1)
    qc.cx((0, 4), plus=1)
    qc.cx((4, 5), plus=1)
    qc.cx((0, 4), plus=1)
    qc.cx((0, 4), plus=1)
    qc.cx((4, 6), plus=1)
    qc.cx((0, 4), plus=1)
    qc.cx((4, 6), plus=1)
    qc.x(6)
    qc.cx((2, 6), plus=1)
    qc.cx((6, 5), plus=1)
    qc.cx((2, 6), plus=1)
    qc.cx((2, 5), plus=1)
    qc.cx((5, 6), plus=1)
    qc.cx((2, 5), plus=1)
    qc.measure_all()
    qc.run

start = time.time()
test()
end = time.time()
print(start - end)