## Time taken = 0.19810904799669515

import timeit
import_module = '''
from framework.core.quantum_circuit import QuantumCircuit
'''
testcode = ''' 
def test(): 
    qc = QuantumCircuit(qregs=[2, 2, 3, 2, 3, 3])

    qc.cx(3, 2)
    qc.cx(0, 2)
    qc.cx(2, 3)
    qc.cx(0, 2)
    qc.cx(3, 2)
    qc.cx(2, 4)
    qc.cx(1, 4)
    qc.cx(4, 2)
    qc.cx(1, 4)
    qc.cx(2, 4)
    qc.cx(3, 5)
    qc.cx(1, 5)
    qc.cx(5, 3)
    qc.cx(1, 5)
    qc.cx(3, 5)

'''


print(timeit.timeit(stmt=testcode, setup=import_module))