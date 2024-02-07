from useQudiet import RUN_CIRC
import unittest
import random

def generateTestCases(number_of_tests: int, range_low: int, range_high: int) -> list[list[int, list[int], str]]:
    """Generates Test cases. Implicitly does additional tests where all inputs are 1, with last input as 1 or 0.
    Number of tests performed in total = number_of_tests + 2x(range_high - range_low + 1)

    Args:
        number_of_tests (number): Number of random tests to perform
        range_low (number): lower bound for number of qubits present in the circuit
        range_high (number): upper bound for the number of qubits present in the circuit

    Returns:
        _type_: _description_
    """

    flip = lambda n : 0 if n == 1 else 1

    test_cases = []

    how_many_qudits_to_use = random.choices(range(range_low, range_high+1), k=number_of_tests)

    for number_of_qudits_for_circuit in how_many_qudits_to_use:
        input_config_last_1 = random.choices([0,1], k=number_of_qudits_for_circuit)

        input_config_copy = [x for x in input_config_last_1]

        if 0 not in input_config_last_1[:-1]: # all but the end
            input_config_last_1[-1] = flip(input_config_last_1[-1])
        
        expectation_last_1 = f"|{''.join([str(elem) for elem in input_config_last_1])}>"

        test_cases.append(
            [number_of_qudits_for_circuit,
             input_config_copy,
             expectation_last_1]
        )
    
    # might aswell add the test cases where the inputs is all ones and the last bit is 1 + all the inputs are one and the last bit is a 0
        
    for number_of_qudits_for_circuit in range(range_low, range_high+1):
        input_config_last_1 = [1]*number_of_qudits_for_circuit
        expectation_last_1 = [1]*(number_of_qudits_for_circuit-1) + [0]

        # all one, expectation = last qudit flipped to 0
        test_cases.append(
            [number_of_qudits_for_circuit,
             input_config_last_1,
             f"|{''.join([str(elem) for elem in expectation_last_1])}>"]
        )


        input_config_last_0 = [1]*(number_of_qudits_for_circuit-1) + [0]
        expectation_last_0 = [1]*number_of_qudits_for_circuit

        # all one except last, expectation = last qudit flipped to 1
        test_cases.append(
            [number_of_qudits_for_circuit,
             input_config_last_0,
             f"|{''.join([str(elem) for elem in expectation_last_0])}>"]
        )

    return test_cases

class TestingCircuit(unittest.TestCase):
    pass


def generateTest(n, inp, exp, testNo):
    def test(self):
        print(f"testing input config of size({n}): {inp} \n expectation: {exp}" )
        self.assertEqual(RUN_CIRC(n, inp), exp, f"Test Case #${testNo} fail")

    return test


if __name__ == '__main__':

    # number of tests to perform, lower limit, upper limit of qudits in the circuit
    # then performs 2x(upperlimit - lowerlimit  + 1 ) extra tests
    testcases = generateTestCases(10, 4, 12)

    for index, (_n, _inp, _exp) in enumerate(testcases, start=1):
        test_name = f'test_case_${index}'
        current_test = generateTest(_n, _inp, _exp, index)
        setattr(TestingCircuit, test_name, current_test)
    unittest.main()
