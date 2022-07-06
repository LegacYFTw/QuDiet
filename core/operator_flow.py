import numpy as np

from circuit_library.standard_gates.h import HGate
from circuit_library.standard_gates.measurement import Measurement
from circuit_library.standard_gates.x import XGate
from circuit_library.standard_gates.z import ZGate

from core.moment import Moment


# Can be used to find dot product of more than two matrices


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
        :return: True if every register doesn't have a Measurement gate acting on it, else False
        """
        for _curr_moment in args:
            _curr_moment_list = _curr_moment.peek_list()
            if self._opflow_list:
                # Checks if all the registers have a measurement. If yes, returns False
                if all(self._measurement_count):
                    return False
                
                # Finds the register number of either of HGate, Xgate or ZGate present in the current moment
                _qreg = _curr_moment_list.index(
                    next(
                        _gate
                        for _gate in _curr_moment_list
                        if isinstance(_gate, (HGate, XGate, ZGate))
                    )
                )
                
                # Loops through the OperatorFlow list, checks if any of the earlier Moment(s) have an IGate.
                # If yes, replaces it with HGate, XGate or ZGate of the current Moment.
                _pos_of_first_moment_with_igate = len(self._opflow_list) - 1
                for _index, _curr_earlier_moment in enumerate(self._opflow_list[:0:-1]):
                    _curr_earlier_moment: Moment = _curr_earlier_moment
                    _is_igate_in_earlier_moment = _curr_earlier_moment.check_igate_at_qreg(_curr_moment_list[_qreg])

                    if _is_igate_in_earlier_moment:
                        _pos_of_first_moment_with_igate = _pos_of_first_moment_with_igate - 1
                    else:
                        _first_moment_with_igate: Moment = self._opflow_list[_pos_of_first_moment_with_igate + 1]
                        _added_gate_to_earlier_moment = _first_moment_with_igate.replace_igate(_curr_moment_list[_qreg])
                        if _added_gate_to_earlier_moment:
                            break
                    _added_gate_to_earlier_moment = False
                
                # Checks if the current Moment's HGate, XGate or ZGate has been added to any earlier Moment.
                # If no, takes the last Moment in OperatorFlow list and points it to the current Moment, thereby
                # adding it to the OperatorFlow list.
                if not _added_gate_to_earlier_moment:
                    _prev_moment: Moment = self._opflow_list[-1]
                    _prev_moment.next_pointer = _curr_moment
                    _curr_moment.prev_pointer = _prev_moment
                    self._opflow_list.append(_curr_moment)
            
            else:
                # If OperatorFlow list is empty, initiate _measurement_count list with register length times 0.
                # Also, append the current moment to OperatorFlow list.
                self._measurement_count = len(_curr_moment_list) * [0]
                self._opflow_list.append(_curr_moment)

            _has_measurement = self.__detect_measurement_and_add_count(_curr_moment)

        return True


    def __detect_measurement_and_add_count(self,
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


    def __exec(self, *args: Moment):
        """
        This function takes multiple Moment objects, traverses them from last to first, performing kronecker product
        on each of the Gates of every Moment, then performs dot product on the resultant kronecker products of all 
        the Moments and finally returns it.

        :param *args: Accepts multiple Moment objects
        :return: ndarray
        """
        
        # Creates a list _all_moments from all the passed Moments from args
        _all_moments = list(args)
        
        # Pops out the last Moment and stores it in _moment
        _moment = _all_moments.pop()

        # Sets _dot_product as None
        _dot_product = None
        
        # Run a loop while there is a Moment present in the _all_moments list
        while _all_moments:
            
            # Get the moment list from the current Moment (_moment) and reverse it for FIFO operation. 
            _moment_list = _moment.peek_list()
            _moment_list = _moment_list[::-1]
            
            # Pops out the first Gate from the _moment_list and get it's Unitary property to _kron_product
            _kron_product = _moment_list.pop()
            _kron_product = _kron_product.unitary

            # Run a loop while there is a Gate present in the _moment_list
            while _moment_list:
                
                # Pops a Gate from _moment_list and stores it's Unitary property to _curr_gate
                _curr_gate = _moment_list.pop()
                _curr_gate = _curr_gate.unitary

                # Computes the kronecker product of the current _kron_product and _curr_gate, and store 
                # the kronecker product of the two in _kron_product
                _kron_product = np.kron(_kron_product, _curr_gate)
            
            # If _dot_product does not have a value, assigns the value of _kron_product to _dot_product
            # else, calculates the dot product of _dot_product and _kron_product and assigns it to _dot_product.
            # NOTE: The if condition evaluates to True only for the first run of the parent while loop.
            if not _dot_product:
                _dot_product = _kron_product
            else:
                _dot_product = np.dot(_dot_product, _kron_product)

            # Pops a Moment from _all_moments and assigns it to _moment
            _moment = _all_moments.pop()
        
        # Once the parent while loop ends, returns the final _dot_product
        return _dot_product


    def __placeholder_identity(self,
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
