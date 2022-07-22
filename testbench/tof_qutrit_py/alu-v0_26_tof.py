## Time taken = 0.1873249210038921

import timeit
import_module = '''
from framework.core.quantum_circuit import QuantumCircuit
'''
testcode = ''' 
def test(): 
    qc = QuantumCircuit(qregs=[3, 3, 3, 2, 2])

    qc.cx(2, 1)
    qc.cx(2, 0)
    qc.cx(1, 3)
    qc.cx(3, 0)
    qc.cx(1, 3)
    qc.cx(0, 4)
    qc.cx(4, 2)
    qc.cx(0, 4)
    qc.cx(1, 3)
    qc.cx(3, 0)
    qc.cx(1, 3)
    qc.cx(0, 4)
    qc.cx(4, 2)
    qc.cx(0, 4)
    qc.cx(4, 3)
    qc.cx(0, 4)
    qc.cx(4, 2)
    qc.cx(0, 4)
    qc.x(2)

'''


print(timeit.timeit(stmt=testcode, setup=import_module))