## Time taken = 0.18038925994187593

import timeit
import_module = '''
from framework.core.quantum_circuit import QuantumCircuit
'''
testcode = ''' 
def test(): 
    qc = QuantumCircuit(qregs=[2, 2, 2, 2, 3, 3, 3])

    qc.cx(3, 4)
    qc.cx(1, 4)
    qc.cx(0, 4)
    qc.cx(4, 5)
    qc.cx(0, 4)
    qc.cx(0, 4)
    qc.cx(4, 6)
    qc.cx(0, 4)
    qc.cx(4, 6)
    qc.x(6)
    qc.cx(2, 6)
    qc.cx(6, 5)
    qc.cx(2, 6)
    qc.cx(2, 5)
    qc.cx(5, 6)
    qc.cx(2, 5)

'''


print(timeit.timeit(stmt=testcode, setup=import_module))