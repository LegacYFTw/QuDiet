## Time taken = 0.19810904799669515

import timeit
import_module = '''
from framework.core.quantum_circuit import QuantumCircuit
'''
testcode = ''' 
def test(): 
    qc = QuantumCircuit(qregs=[2, 2, 3, 3])

    qc.cx(2, 3)
    qc.cx(3, 0)
    qc.cx(2, 3)
    qc.cx(2, 3)
    qc.cx(2, 3)
    qc.cx(3, 1)
    qc.cx(2, 3)
    qc.cx(0, 2)
    qc.cx(2, 3)
    qc.cx(0, 2)
    qc.cx(3, 2)
    qc.x(3)

'''


print(timeit.timeit(stmt=testcode, setup=import_module))