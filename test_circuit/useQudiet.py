from circuit import Circuit, Gate
from qudiet.core.quantum_circuit import QuantumCircuit


def RUN_CIRC(n, input_states=None):
    circ = Circuit(n)
    circ.simulate()

    qubits = {circ.actual_mapping.get(item) for item in circ.qubits}
    qutrits = {circ.actual_mapping.get(item) for item in circ.qutrits}
    ququads = {circ.actual_mapping.get(item) for item in circ.ququads}

    print("qubits", qubits)
    print("qutrits", qutrits)
    print("ququads", ququads)

    qregs = [2] * n
    init_states = input_states if input_states is not None else [1] * n  # all 1 unless specified
    # init_states = [1] * n
    # init_states[-1] = 1
    # init_states[-2] = 1
    # init_states[-3] = 1

    # print(init_states)

    for index, _ in enumerate(qregs):
        if index in ququads:
            qregs[index] = 4
        elif index in qutrits:
            qregs[index] = 3

    print("reg is ", qregs)

    qc = QuantumCircuit(qregs=qregs, init_states=init_states)

    plus_mapping = {"Ternary": 1, "Quaternary": 2}

    # temp = circ.final_levels[:3]

    # print(n)
    # print(circ.final_levels)
    # print("===========")

    for decomp in circ.final_levels:  # list of list of tuples
        for l in decomp:  # list of tuples
            left, right = l

            if left is not None:
                control, target, plus = make_CNOT_gate(left, circ.actual_mapping)
                qc.cx(acting_on=(control, target), plus=plus)

            if right is not None:
                control, target, plus = make_CNOT_gate(right, circ.actual_mapping)
                qc.cx(acting_on=(control, target), plus=plus)

    qc.measure_all()

    res = qc.run()

    output = list(res[0].keys())[0]
    # print(output)

    return output


def make_CNOT_gate(g: Gate, mapping: dict):
    target, control = mapping.get(g.target), mapping.get(g.control)

    plus = -1 if g.inc_or_dec == "-" else 1

    # print(f'c={control}, t={target} -> {"+" if plus == 1 else "-"}')

    return control, target, plus
