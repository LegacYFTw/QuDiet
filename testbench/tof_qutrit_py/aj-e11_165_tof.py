## Time taken = 0.19627560800290667

import timeit
import_module = '''
from framework.core.quantum_circuit import QuantumCircuit
'''
testcode = ''' 
def test(): 
    qc = QuantumCircuit(qregs=[2, 3, 3, 3, 3])

    qc.cx(1, 2)
    qc.cx(2, 3)
    qc.cx(0, 3)
    qc.cx(3, 2)
    qc.cx(0, 3)
    qc.cx(0, 2)
    qc.cx(2, 1)
    qc.cx(1, 2)
    qc.cx(2, 4)
    qc.cx(1, 2)
    qc.cx(3, 4)
    qc.cx(4, 0)
    qc.cx(3, 4)
    qc.cx(1, 2)
    qc.cx(2, 4)
    qc.cx(1, 2)
    qc.cx(3, 4)
    qc.cx(4, 0)
    qc.cx(3, 4)
    qc.cx(1, 2)
    qc.cx(2, 0)
    qc.cx(1, 2)
    qc.cx(0, 3)
    qc.cx(3, 2)
    qc.cx(0, 2)
    qc.cx(2, 3)
    qc.cx(0, 2)
    qc.cx(0, 3)
    qc.cx(3, 1)
    qc.cx(0, 3)
    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.x(3)

'''


print(timeit.timeit(stmt=testcode, setup=import_module))