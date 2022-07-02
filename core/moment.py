from typing import Union
from circuit_library.standard_gates.i import IGate
from circuit_library.standard_gates.quantum_gate import QuantumGate
from core.init_states import InitState


class Moment:
    def __init__(self,
                 *args: Union(QuantumGate, InitState, IGate)
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
        self._prev_pointer = None
        self._next_pointer = None
        self._number_of_operations = len(args)
        self._operations = list(args)
        self._moment_list = []

        self._result = self.__populate_list__()

        # TODO: Run unit tests

    @property
    def prev_pointer(self):
        return self._prev_pointer

    @prev_pointer.setter
    def prev_pointer(self, pointer):
        self._prev_pointer = pointer

    @property
    def next_pointer(self):
        return self._next_pointer

    @next_pointer.setter
    def next_pointer(self, pointer):
        self._next_pointer = pointer


    def __populate_list__(self) -> bool:
        """
        This function takes a list of InitState and QuantumGate objects, and pushes them into the
        Moment.
        :param operations_list: The list of InitState and QuantumGate objects to be pushed
        :return: True for success
        """
        _n_ops = len(self._operations)
        _ops_iter = iter(self._operations)
        _iteration = 0
        while _iteration < _n_ops:
            _current_item = next(_ops_iter)
            _pushed = self.__push_list__(_current_item)
            if not _pushed:
                return False
            _iteration += 1
        return True


    def __push_list__(self,
                      operation: Union[QuantumGate, InitState, IGate]
                      ) -> bool:
        """
        This function pushes the QuantumGate objects into the Moment list
        :param gate: The actual gates that will be pushed into the Moment
        :return: True for success
        """
        self._moment_list.append(operation)

        return True


    def peek_list(self) -> list:
        """
        Function used to peek the list
        :param self: Peeks the current list
        :return: Returns the list held in the Moment object
        """
        return self._moment_list


    def __insert_placeholder_identity__(self,
                                        qregs: int
                                        ) -> bool:
        """
        Pushes a placeholder Identity Operator into the Moment list for an absent gate in order to complete a moment.
        Let's say that a QuantumCircuit object is as follows:

        qreg_0: |0> -- H -- X \n
        qreg_1: |0> ---Z ----

        We can see that the QuantumCircuit has 2 registers. qreg_0 has H gate and an X gate in sequence. ``qreg_1`` has just
        a ``Z`` gate. This means that the Moment ``m1`` will consist of ``[H,Z]`` and Moment ``m2`` will consist of [X].
        We would now want to insert a second gate ``I`` in position 1. This would complete the moment.

        In the event we have the following circuit:

        qreg_0: |0> -- H ----  \n
        qreg_1: |0> -- Z -- X

        We see ``m1`` will consist of ``[H,Z]`` and ``m2`` will consist of [X]. In order to fill out the position of the identity
        operator, we will need to access the instance variables of the quantum gate (X here) and accordingly get the
        position on which it is acting on. So if X.acting_register() returns us 1, as in the case above, we shall,
        accordingly fill out Identity operators before (or after) X.acting_register.

        :param qregs: This denotes the total number of quantum registers
        :return: True if success
        """

        _identity_operator = IGate

        if len(self._moment_list) != qregs:
            if type(self._moment_list) == InitState:
                return True
            else:
                for _index, _operator in enumerate(self._moment_list):
                    if _operator.qreg != _index:
                        self._moment_list.insert(_index, _identity_operator)
        else:
            return False

        return True
