## Time taken = 0.19592224899679422

import timeit
import_module = '''
from framework.core.quantum_circuit import QuantumCircuit
'''
testcode = ''' 
def test(): 
    qc = QuantumCircuit(qregs=[2, 2, 3])

    qc.cx(1, 2)
    qc.cx(2, 0)
    qc.cx(1, 2)
    qc.cx(2, 1)
    qc.cx(1, 2)
    qc.cx(0, 2)
    qc.cx(2, 1)

'''


print(timeit.timeit(stmt=testcode, setup=import_module))