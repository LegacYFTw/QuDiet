## Time taken = 0.19710884999949485

import timeit
import_module = '''
from framework.core.quantum_circuit import QuantumCircuit
'''
testcode = ''' 
def test(): 
    qc = QuantumCircuit(qregs=[2, 3, 3, 2, 2])

    qc.cx(0, 2)
    qc.cx(2, 3)
    qc.cx(0, 2)
    qc.cx(1, 2)
    qc.cx(2, 4)
    qc.cx(1, 2)
    qc.cx(1, 2)
    qc.cx(2, 3)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.cx(1, 3)
    qc.cx(0, 1)
    qc.x(1)
    qc.x(2)
    qc.cx(1, 2)
    qc.cx(2, 4)
    qc.cx(1, 2)
    qc.x(0)
    qc.cx(0, 4)

'''


print(timeit.timeit(stmt=testcode, setup=import_module))