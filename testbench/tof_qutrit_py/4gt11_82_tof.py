## Time taken = 0.19079086801502854

import timeit
import_module = '''
from framework.core.quantum_circuit import QuantumCircuit
'''
testcode = ''' 
def test(): 
    qc = QuantumCircuit(qregs=[2, 2, 2, 2, 3])

    qc.cx(2, 1)
    qc.cx(1, 2)
    qc.cx(3, 2)
    qc.cx(2, 3)
    qc.cx(4, 3)
    qc.cx(3, 4)
    qc.cx(1, 4)
    qc.cx(4, 0)
    qc.cx(1, 4)
    qc.cx(4, 3)
    qc.cx(4, 2)
    qc.cx(4, 1)
    qc.cx(0, 4)
    qc.cx(4, 0)

'''


print(timeit.timeit(stmt=testcode, setup=import_module))