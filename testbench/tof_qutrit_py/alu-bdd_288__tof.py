## Time taken = 0.19586250899737934

import timeit
import_module = '''
from framework.core.quantum_circuit import QuantumCircuit
'''
testcode = ''' 
def test(): 
    qc = QuantumCircuit(qregs=[2, 2, 2, 3, 2, 3, 2])

    qc.cx(0, 5)
    qc.cx(1, 3)
    qc.cx(3, 5)
    qc.cx(1, 3)
    qc.cx(0, 3)
    qc.cx(3, 5)
    qc.cx(0, 3)
    qc.cx(2, 6)
    qc.cx(0, 3)
    qc.cx(3, 6)
    qc.cx(0, 3)
    qc.cx(2, 3)
    qc.cx(3, 6)
    qc.cx(2, 3)
    qc.cx(6, 5)
    qc.cx(4, 5)
    qc.cx(5, 6)
    qc.cx(4, 5)
    qc.x(6)

'''


print(timeit.timeit(stmt=testcode, setup=import_module))