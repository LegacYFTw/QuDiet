## Time taken = 0.19620991899864748

import timeit
import_module = '''
from framework.core.quantum_circuit import QuantumCircuit
'''
testcode = ''' 
def test(): 
    qc = QuantumCircuit(qregs=[2, 3, 2, 2, 2, 2])

    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.cx(0, 1)
    qc.cx(1, 3)
    qc.cx(0, 1)
    qc.cx(0, 3)
    qc.cx(0, 1)
    qc.cx(1, 4)
    qc.cx(0, 1)
    qc.cx(1, 4)
    qc.cx(0, 5)
    qc.cx(0, 1)
    qc.cx(1, 5)
    qc.cx(0, 1)
    qc.cx(1, 5)
    qc.x(3)
    qc.x(4)
    qc.x(5)

'''


print(timeit.timeit(stmt=testcode, setup=import_module))