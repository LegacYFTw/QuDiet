from circuit_library.standard_gates import quantum_gate


class Moment:
    def __init__(self,
                 *args: quantum_gate
                 ):
        """
        This is the Moment class. This is essentially a list of quantum gates that spans across quantum registers.
        For eg., consider the following poorly drawn quantum circuit

        qreg_0: |0> -- H -- X
        qreg_1: |1> -- H ----

        This circuit consists of two Moments objects m1 and m2. m1 has a list that maintains the two H gates. Whereas
        m2 has a stack that maintains X in position 0 (for qreg_0) and I (Identity Operator) in position 1.

        The contents of the lists in any two moments can be compared at any point to allow further planned optimization
        functions. The lists can be peeked to allow for reading without disturbing the alignment of the elements.

        """
        self._number_of_gates = len(args)
        self._gates = args
        self._moment_list = []

        # TODO: Initialize these values properly
        # TODO: Make sure the push method and the peek method works as expected
        # TODO: Run unit tests

    def _push_list(self,
                   gate : quantum_gate
                   ) -> bool:
        """

        :param args: The actual gates that will be pushed into the Moment
        :return: True for success
        """
        # TODO: Complete this function
        return True

    def peek_list(self) -> list:
        """
        Function used to peek the list
        :param self: Peeks the current list
        :return: Returns the list held in the Moment object
        """
        # TODO: Complete this function
        return self._moment_list

