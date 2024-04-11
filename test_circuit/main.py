import math

from circuit import Circuit
from useQudiet import RUN_CIRC

from qudiet.core.quantum_circuit import QuantumCircuit
from qudiet.core.backend.NumpyBackend import NumpyBackend


def mathematical_expectation(n: int):
    c: int = n - 1
    tern = 4 * (c // 4) + 5
    quat = (4 * (c // 2)) - (4 * (c // 4)) - 4

    if c % 2 == 0:
        tern -= 2

    # print(f"tern: {tern}, quat: {quat}, total: {quat + tern}")

    qb = (c // 2) - (c // 4) + 1
    qt = 2 * (c // 4) + 2
    qq = (c // 2) - (c // 4) - 1

    return tern, quat, qb, qt, qq


def runner():
    # for n in [3, 4, 5, 6, 7, 8, 20, 23, 55, 65, 20, 19, 18, 16, 15, 32]:
    for n in [19]:
        Circ = Circuit(n)
        Circ.simulate()

        print("c -->", n - 1)
        counter_ternary, counter_quaterary = 0, 0

        for d in Circ.final_levels:
            # print("----------------")
            for l in d:
                print([ll.__str__() for ll in l])

                ###############################
                left, right = l
                if left is not None:
                    if left.tq == "Ternary":
                        counter_ternary += 1
                    else:
                        counter_quaterary += 1

                if right is not None:
                    if right.tq == "Ternary":
                        counter_ternary += 1
                    else:
                        counter_quaterary += 1
            ###############################

            print("----------------")
        print("========")

        print("counted: ")
        print("tern: ", counter_ternary, "quat: ", counter_quaterary, "total: ", counter_ternary + counter_quaterary)

        # print(Circ.qubits)
        # print(Circ.qutrits)
        # print(Circ.ququads)
        #
        print("actual:")
        print(f"tern: {Circ.tern}, quat: {Circ.quat}, total: {Circ.tern + Circ.quat}")
        # print("qubits -> ", len(Circ.qubits))
        # print("qutrits -> ", len(Circ.qutrits))
        # print("ququads -> ", len(Circ.ququads))

        t, q, qb, qt, qq = mathematical_expectation(n)

        print("expected:")
        print(f"tern: {t}, quat: {q}, total: {t + q}")
        # print("qubits -> ", qb)
        # print("qutrits -> ", qt)
        # print("ququads -> ", qq)

        if t != Circ.tern and q != Circ.quat and qb != len(Circ.qubits) and qt != len(Circ.qutrits) and qq != len(
                Circ.ququads):
            print("=========\nNOOOOOOOOOOOOOOOOOOOOO for ", n, "\n=========")


if __name__ == '__main__':
    # runner()

    # # state of the registers
    # qc = QuantumCircuit(qregs=[3, 4, 4], init_states=[2, 1, 2])
    #
    # # acting_on=(control, target), plus = how much to increment
    # qc.cx(acting_on=(0, 2), plus=1)
    # qc.cx(acting_on=(2, 1), plus=1)
    #
    # qc.cx(acting_on=(2, 1), plus=-1)
    # qc.cx(acting_on=(0, 2), plus=-1)
    #
    # qc.measure_all()
    # result = qc.run()
    #
    # print(result)

    # number of lines qubits, circuit inputs, expectation
    d = [
        [5, [1, 1, 1, 1, 1], '|11110>'],
        [6, [1, 1, 1, 1, 1, 1], '|111110>'],
        [7, [1, 1, 1, 1, 1, 1, 1], '|1111110>'],
        [5, [1, 0, 1, 1, 1], '|10111>'],
        [6, [1, 1, 1, 0, 0, 1], '|111001>'],
        [7, [0, 0, 0, 0, 1, 1, 1], '|0000111>'],
        [5, [0, 0, 0, 0, 0], '|00000>'],
        [6, [0, 0, 0, 0, 0, 1], '|000001>'],
        [10, [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], '|1010101010>'],
        [8, [0, 0, 0, 0, 1, 1, 1, 1], '|00001111>'],
        [9, [1, 1, 1, 1, 1, 1, 0, 1, 0], '|111111010>'],
        [8, [0, 0, 0, 0, 0, 0, 0, 0], '|00000000>'],
        [11, [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], '|11111111000>'],
    ]

    for n, i, e in d:
        RUN_CIRC(n, i)

    # RUN_CIRC(9)
