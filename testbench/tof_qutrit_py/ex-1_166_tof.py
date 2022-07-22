## Time taken = 0.1976759880053578

import timeit
import_module = '''
from framework.core.quantum_circuit import QuantumCircuit
'''
testcode = ''' 
def test(): 
    qc = QuantumCircuit(qregs=[2, 2, 3])

    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.cx(2, 0)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.x(0)

'''


print(timeit.timeit(stmt=testcode, setup=import_module))