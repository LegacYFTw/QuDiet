from framework.core.quantum_circuit import QuantumCircuit

def test_qudit_init():
    qc = QuantumCircuit(qregs=[2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2], init_states=[1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    qc.measure_all()
    result = qc.run()

    assert result.nonzero() == ([23296], [0])
