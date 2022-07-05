from circuit_library.standard_gates.h import HGate
from typing import (
    Union,
    Optional,
)

from circuit_library.standard_gates.h import HGate
from circuit_library.standard_gates.i import IGate
from circuit_library.standard_gates.measurement import Measurement
from circuit_library.standard_gates.x import XGate
from circuit_library.standard_gates.z import ZGate
from circuit_library.standard_gates.cx import CXGate
from core.moment import Moment
from core.operator_flow import OperatorFlow
from init_states import InitState
from utils.numpy import clip


class QuantumCircuit:
    def __init__(self,
                 qregs: 'Union[tuple[int, int], list[int]]',
                 cregs: Optional[int] = None,
                 name: Optional[str] = None,
                 init_states: 'Optional[list[int]]' = None,
                 ):
        """
        x = QuantumCircuit((3,3))
        This will basically create a QuantumCircuit with RegisterLength = 3, meaning there shall be 3 qudits, with energy
        level 3 or in essence a 3 qutrit register and one classical register.

        y = QuantumCircuit([2,2,3,3])
        This will create a QuantumCircuit with RegisterLength = len(Iterable) (here 4) with the energy levels 2,2,3,3 or in
        other words this will create a two qubits and two qutrits and one classical register.
        
        :param qregs: This can either be a tuple of two integers, where the first one is the register length and the second
                       one is their dimension, or a list of multiple integers each denoting their dimension.
        :param cregs:
        :param name: 
        :param init_states: This is a list of integers, where their values correspond to the dimension and the index of
                             each number is their qreg number
        """

        if not isinstance(qregs, (tuple, list)):
            raise ValueError(
                "The registers must be defined as a tuple of two integers or a list of integers"
            )
        self.qregs = qregs
        self.cregs = cregs or 0
        self.name = name or ""
        self.init_states = init_states or []

        self.op_flow = OperatorFlow()

        self._is_qregs_tuple = type(self.qregs) == tuple
        self._is_qregs_list = type(self.qregs) == list

        if self._is_qregs_tuple:
            self._reg_length = self.qregs[0]
            self._reg_dims = self._reg_length * self.qregs[1]

        elif self._is_qregs_list:
            self._reg_length = len(self.qregs[0])
            self._reg_dims = self.qregs[1]

        if self._reg_length > len(self.init_states):
            self.init_states.extend((self._reg_length - len(self.init_states)) * [0])

        self.__initialize_states()

    def get_circuit_config(self):
        raise NotImplementedError

    def __validate_gate_inputs(self, qreg: int, dims: Optional[int]):
        """
        Responsible for checking if the register number or the dimension of the gates are in the correct bounds.

        :param qreg: The quantum register number for putting the gate
        :param dims: The dimension of the gate
        """
        if dims > self._reg_dims:
            raise ValueError("Input dimension is greater than the register dimension.")
        if qreg > self._reg_length:
            raise ValueError("Illegal placement of gate. Register specified is out of circuit bounds.")

    def __add_moment_to_opflow(self, qreg: int, gate_obj: Union[HGate, XGate, ZGate]) -> bool:
        """
        Creates Moment objects for the given QuantumGate object and pushes it into the OperatorFlow object created earlier

        :param qreg: The quantum register number for putting the gate
        :param gate_obj: Object of one of QuantumGate's child classes, e.g. HGate, XGate, etc.
        :return: True if everything goes well, else False
        """
        _moment_data = []
        for _reg in range(self._reg_length):
            _igate = IGate(qreg=_reg, dims=gate_obj.dims)
            _moment_data.append(_igate)
        _moment_data[qreg] = gate_obj

        _curr_moment = Moment(*_moment_data)
        _result = self.op_flow.populate_opflow(_curr_moment)
        return _result

    def h(self, qreg: int, dims: Optional[int] = None) -> bool:
        """
        Responsible for creating the HGate and adding it to OperatorFlow through another function call

        :param qreg: The quantum register number for putting the gate
        :param dims: The dimension of the gate
        :return: True if everything goes well, else False
        """
        self.__validate_gate_inputs(qreg, dims)
        _hgate = HGate(qreg=qreg, dims=dims or self._reg_dims)
        _result = self.__add_moment_to_opflow(qreg, _hgate)
        return _result

    def x(self, qreg: int, dims: Optional[int] = None) -> bool:
        """
        Responsible for creating the XGate and adding it to OperatorFlow through another function call

        :param qreg: The quantum register number for putting the gate
        :param dims: The dimension of the gate
        :return: True if everything goes well, else False
        """
        self.__validate_gate_inputs(qreg, dims)
        _xgate = XGate(qreg=qreg, dims=dims or self._reg_dims)
        _result = self.__add_moment_to_opflow(qreg, _xgate)
        return _result

    def z(self, qreg: int, dims: Optional[int] = None) -> bool:
        """
        Responsible for creating the ZGate and adding it to OperatorFlow through another function call

        :param qreg: The quantum register number for putting the gate
        :param dims: The dimension of the gate
        :return: True if everything goes well, else False
        """
        self.__validate_gate_inputs(qreg, dims)
        _zgate = ZGate(qreg=qreg, dims=dims or self._reg_dims)
        _result = self.__add_moment_to_opflow(qreg, _zgate)
        return _result
    
    def cx(self, acting_on:Tuple[int, int], plus:int) -> bool:
        """
        Responsible for creating the CXGate and adding it to OperatorFlow through another function call

        :param qreg: The quantum register number for putting the gate
        :param dims: The dimension of the gate
        :return: True if everything goes well, else False
        """
        
        active_qregs, acting_on = clip(self.qregs, acting_on)
        _cxgate = CXGate(active_qregs, acting_on=acting_on, plus=plus)

        _result = self.__add_moment_to_opflow(qreg, _cxgate)
        return _result
    

    def measure(self, qreg: int) -> NotImplementedError:
        """
        Responsible for creating the Measurement Gate and adding it to OperatorFlow through another function call

        :param qreg: The quantum register number for putting the gate
        :param dims: The dimension of the gate
        :return: True if everything goes well, else False
        """
        raise NotImplementedError

    def measure_all(self) -> bool:
        """
        Responsible for creating the Measurement Gate and adding it to OperatorFlow through another function call.
        Contrary to the measure function, this method applies a Measurement Gate across all gates in a single Moment.


        :return: True if everything goes well, else False
        """
        if self._is_qregs_tuple:
            _measurement_moment = []
            for _index, _state in enumerate(self.init_states):
                # Adds Operator flow object and push the Measurement object into Operator Flow stack
                _measurement = Measurement(qreg=_index)
                _measurement_moment.append(_measurement)

        _m = Moment(*_measurement_moment)
        self.op_flow.populate_opflow(_m)

    def __initialize_states(self):
        """
        Initializes the qudits to |0> state or |N> state depending on the dimensions of the qubits
        """
        if self._is_qregs_tuple:
            _init_moment = []
            for _index, _element in enumerate(self.init_states):
                # Adds Operator flow object and push the init object into Operator Flow stack
                _init_state = InitState(dim=_element, state=0, qreg=_index)
                _init_moment.append(_init_state)

        _m = Moment(*_init_moment)
        self.op_flow.populate_opflow(_m)
