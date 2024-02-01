from useQudiet import RUN_CIRC
import unittest
import random

testcases = [
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
    # [20, [1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1,1,1,1,1], '|11111111111111111110>'],
]


def generateTestCases(number_of_tests, range_low, range_high):

    # pick x from the provided range
    # generate a combination of x number of 0s and 1s
    # if number is of length x and the first x-1 numbers are 1, result should be the same number with the output flipped

    def flip(n):
        return 0 if n == 1 else 1

    test_cases = []

    how_many_qudits_to_use = random.choices(range(range_low, range_high+1), k=number_of_tests)

    for number_of_qudits_for_circuit in how_many_qudits_to_use:
        input_config = random.choices([0,1], k=number_of_qudits_for_circuit)
        
        if 0 not in input_config[:-1]: # all but the end
            input_config[-1] = flip(input_config[-1])
        
        expectation = f"{''.join([str(elem) for elem in input_config])}>"

        test_cases.append(
            [number_of_qudits_for_circuit,
             input_config,
             expectation]
        )
    
    # might aswell add the test cases where the inputs is all ones
        
    for number_of_qudits_for_circuit in range(range_low, range_high+1):
        input_config = [1]*number_of_qudits_for_circuit
        expectation = [1]*(number_of_qudits_for_circuit-1) + [0]

        test_cases.append(
            [number_of_qudits_for_circuit,
             input_config,
             expectation]
        )

    return test_cases

class TestingCircuit(unittest.TestCase):
    pass


def generateTest(n, inp, exp, testNo):
    def test(self):
        self.assertEqual(RUN_CIRC(n, inp), exp, f"Test Case #${testNo} fail")

    return test


if __name__ == '__main__':

    ans = generateTestCases(10, 4, 11)
    print(ans)

    for index, (_n, _inp, _exp) in enumerate(testcases, start=1):
        test_name = f'test_case_${index}'
        current_test = generateTest(_n, _inp, _exp, index)
        setattr(TestingCircuit, test_name, current_test)
    unittest.main()
