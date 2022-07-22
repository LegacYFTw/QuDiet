## Time taken = 0.19376320100127487

import timeit
import_module = '''
from framework.core.quantum_circuit import QuantumCircuit
'''
testcode = ''' 
def test(): 
    qc = QuantumCircuit(qregs=[2, 2, 2, 3, 2])

    qc.cx(1, 3)
    qc.x(3)
    qc.cx(0, 3)
    qc.cx(3, 4)
    qc.cx(0, 3)
    qc.cx(2, 3)
    qc.cx(3, 4)
    qc.cx(2, 3)
    qc.cx(3, 4)

'''


print(timeit.timeit(stmt=testcode, setup=import_module))