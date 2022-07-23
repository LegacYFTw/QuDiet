from framework.qasm.qasm_parser import parse_qasm
from framework.utils.numpy import Nbase_to_bin

def test_qasm_1():
    filename = "test.qasm" # "src/testbench/tof_qutrit/..."
    circuit = parse_qasm(filename)
    circuit.run()
    assert circuit.run().nonzero() == (8, 0)