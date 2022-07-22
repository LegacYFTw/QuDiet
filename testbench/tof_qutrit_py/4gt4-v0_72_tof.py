## Time taken = 0.19174050900619477

import timeit
import_module = '''
from framework.core.quantum_circuit import QuantumCircuit
'''
testcode = ''' 
def test(): 
    qc = QuantumCircuit(qregs=[2, 3, 3, 3, 3])

    qc.cx(4, 1)
    qc.cx(2, 4)
    qc.cx(4, 0)
    qc.cx(2, 4)
    qc.x(0)
    qc.cx(0, 2)
    qc.cx(2, 1)
    qc.cx(0, 2)
    qc.cx(1, 3)
    qc.cx(3, 4)
    qc.cx(1, 3)
    qc.cx(0, 2)
    qc.cx(2, 1)
    qc.cx(0, 2)
    qc.cx(1, 3)
    qc.cx(3, 4)
    qc.cx(1, 3)
    qc.cx(0, 1)
    qc.cx(1, 4)
    qc.cx(0, 1)
    qc.cx(0, 1)
    qc.cx(1, 3)
    qc.cx(0, 1)
    qc.cx(2, 3)
    qc.cx(3, 5)
    qc.cx(2, 3)
    qc.cx(0, 1)
    qc.cx(1, 3)
    qc.cx(0, 1)
    qc.cx(2, 3)
    qc.cx(3, 5)
    qc.cx(2, 3)
    qc.cx(3, 5)
    qc.cx(5, 4)
    qc.cx(3, 5)
    qc.cx(0, 1)
    qc.cx(1, 3)
    qc.cx(0, 1)
    qc.cx(2, 3)
    qc.cx(3, 5)
    qc.cx(2, 3)
    qc.cx(0, 1)
    qc.cx(1, 3)
    qc.cx(0, 1)
    qc.cx(2, 3)
    qc.cx(3, 5)
    qc.cx(2, 3)
    qc.cx(3, 5)
    qc.cx(5, 4)
    qc.cx(3, 5)

'''


print(timeit.timeit(stmt=testcode, setup=import_module))