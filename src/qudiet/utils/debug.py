import numpy as np

def moment_to_repr(moment):
    _repr_ = []
    for op in moment._operations:
        op_name = type(op).__name__
        op_unitary = op.unitary.toarray().shape
        _repr_ += [ (op_name, op_unitary) ]
    return _repr_

def weak_compare(qc1, qc2):
    if len(qc1.op_flow._opflow_list) != len(qc2.op_flow._opflow_list):
        for index, (qc1_op, qc2_op) in enumerate(zip(qc1.op_flow._opflow_list, qc2.op_flow._opflow_list)):
            if np.all(moment_to_repr(qc1_op) == moment_to_repr(qc2_op)):
                continue
            else:
                return f"Layer {index}", (qc1_op, qc2_op)