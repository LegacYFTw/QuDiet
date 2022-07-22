## Time taken = 0.19959545900201192

import timeit
import_module = '''
from framework.core.quantum_circuit import QuantumCircuit
'''
testcode = ''' 
def test(): 
    qc = QuantumCircuit(qregs=[2, 3, 2, 2, 2])

    qc.cx(3, 1)
    qc.cx(2, 0)
    qc.cx(1, 4)
    qc.cx(0, 4)
    qc.cx(0, 1)
    qc.cx(1, 4)
    qc.cx(0, 1)
    qc.cx(3, 1)
    qc.cx(2, 0)

'''


print(timeit.timeit(stmt=testcode, setup=import_module))