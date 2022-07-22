## Time taken = 0.19883476302493364s

import timeit
import_module = '''
from framework.core.quantum_circuit import QuantumCircuit
'''
testcode = ''' 
def test(): 
    qc = QuantumCircuit(qregs=[2, 3, 3], init_states=[0, 1, 0])
    qc.cx(0, 2)
    qc.cx(2, 1)
    qc.cx(1, 2)
    qc.cx(2, 0)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.cx(1, 2)
'''


print(timeit.timeit(stmt=testcode, setup=import_module))


