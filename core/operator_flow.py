from circuit_library.standard_gates.measurement import Measurement
from core.init_states import InitState
from moment import Moment


class OperatorFlow:
    def __init__(self,
                 *args: Moment
                 ):
        """
        This creates the OperatorFlow object. Each OperatorFlow object is a collection of Moments. The OperatorFlow
        maintains the order of the Moments and is responsible for any changes and optimization to the gate sequence in
        each Moment object. This OperatorFlow is also accessible by the optimization module which would be responsible
        for optimizing the gate and placements.

        :param args: This constitutes the many Moments, with which the OperatorFlow would be built
        """
        self._moments = args
        self._opflow_list = []
        self._measurement_count = [0]

    def peek(self) -> list:
        """
        Responsible for peeking the list of Moments
        :return: The list of Moments
        """
        return self._opflow_list


    def populate_opflow(self,
                         *args: Moment
                         ) -> bool:
        """
        Responsible for populating the Opflow list
        :param args: These are Moment objects which need to be pushed in order into the _opflow_list
        :return: True if every register has a Measurement gate acting on it, else False
        """
        for _curr_moment in args:
            if self._opflow_list:
                if all(self._measurement_count):
                    return False
                _prev_moment: Moment = self._opflow_list[-1]
                _prev_moment.next_pointer = _curr_moment
                _curr_moment.prev_pointer = _prev_moment
            else:
                _curr_moment_list = _curr_moment.peek_list()
                self._measurement_count = len(_curr_moment_list)*[0]
            self._opflow_list.append(_curr_moment)
            
            _has_measurement = self.__detect_measurement__(_curr_moment)

        return True

    def __detect_measurement__(self,
                               moment: Moment
                               ) -> bool:
        """
        Responsible for detecting whether a Moment object has a measurement gate in it. This function is used for the
        __exec__()
        :param moment: A Moment object
        :return: True if found and False if not found
        """
        _curr_moment_list = moment.peek_list()
        for _index, _gate in enumerate(_curr_moment_list):
            if isinstance(_gate, Measurement):
                self._measurement_count[_index] = 1
                return True
        return False


    def __placeholder_identity__(self,
                                 moment: Moment
                                 ) -> bool:
        """
        Pushes a placeholder Identity Operator into the Moment list for an absent gate in order to complete a moment.
        Let's say that a QuantumCircuit object is as follows:

        qreg_0: |0> -- H -- X \n
        qreg_1: |0> -- Z ----

        We can see that the QuantumCircuit has 2 registers. qreg_0 has H gate and an X gate in sequence. ``qreg_1`` has just
        a ``Z`` gate. This means that the Moment ``m1`` will consist of ``[H,Z]`` and Moment ``m2`` will consist of [X].
        We would now want to insert a second gate ``I`` in position 1. This would complete the moment.

        In the event we have the following circuit:

        qreg_0: |0> -- H ---- \n
        qreg_1: |0> -- Z -- X

        We see ``m1`` will consist of ``[H,Z]`` and ``m2`` will consist of [X]. In order to fill out the position of the
        identity operator, we will need to access the instance variables of the quantum gate (X here) and accordingly get
        the position on which it is acting on. So if X.acting_register() returns us 1, as in the case above, we shall,
        accordingly fill out Identity operators before (or after) X.acting_register.

        :param moment: Moment object to be accessed
        :return: True, if success
        """
        pass
