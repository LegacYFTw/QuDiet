#               This file is part of the QuDiet package.
#              https://github.com/LegacYFTw/qubit-qudit-sim
#
#                      Copyright (c) 2022.
#                      --.- ..- -.. .. . -
#
# Turbasu Chatterjee, Subhayu Kumar Bala, Arnav Das
# Dr. Amit Saha, Prof. Anupam Chattopadhyay, Prof. Amlan Chakrabarti
#
#
# SPDX-License-Identifier: AGPL-3.0
#
#  This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import warnings

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from typing import Optional, Union

from qudiet.circuit_library.standard_gates.cx import CXGate
from qudiet.circuit_library.standard_gates.h import HGate
from qudiet.circuit_library.standard_gates.i import IGate
from qudiet.circuit_library.standard_gates.measurement import Measurement
from qudiet.circuit_library.standard_gates.x import XGate
from qudiet.circuit_library.standard_gates.z import ZGate
from qudiet.circuit_library.standard_gates.quantum_gate import QuantumGate
from qudiet.core.backend import DefaultBackend
from qudiet.core.backend.core import Backend
from qudiet.core.backend.SparseBackend import SparseBackend
from qudiet.core.init_states import InitState
from qudiet.core.moment import Moment
from qudiet.core.operator_flow import OperatorFlow
from qudiet.core.output import Output, OutputMethod, OutputType
from qudiet.utils.linalg import isiterable


class QuantumCircuit:
    def __init__(
        self,
        qregs: "Union[tuple[int, int], list[int]]",
        cregs: Optional[int] = None,
        name: Optional[str] = None,
        init_states: "Optional[list[int]]" = None,
        backend: Backend = None,
        output: Output = None,
        debug: bool = True,
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

        self.backend = DefaultBackend if backend is None else backend
        self.debug_backend = self.backend

        if output is None:
            output = Output(qregs, OutputType.print, OutputMethod.amplitude)

        self.output_processor = output

        if not isinstance(qregs, (tuple, list)):
            raise ValueError(
                "The registers must be defined as a tuple of two integers or a list of integers"
            )
        self.qregs = qregs
        self.cregs = cregs or 0
        self.name = name or ""
        self.init_states = init_states or []

        self.op_flow = OperatorFlow()
        self.op_flow.debug_backend = self.debug_backend
        self.op_flow.debug = debug

        self._is_qregs_tuple = type(self.qregs) == tuple
        self._is_qregs_list = type(self.qregs) == list

        if self._is_qregs_tuple:
            self._reg_length = self.qregs[0]
            self._reg_dims = self._reg_length * [self.qregs[1]]

        elif self._is_qregs_list:
            self._reg_length = len(self.qregs)
            self._reg_dims = self.qregs

        if self._reg_length > len(self.init_states):
            self.init_states.extend((self._reg_length - len(self.init_states)) * [0])

        self.__initialize_states()

    def get_circuit_config(self):
        depth = len(self.op_flow._opflow_list) - 1  # For InitStates
        final_moment_composition = [
            m.__class__ for m in self.op_flow._opflow_list[-1]._moment_list
        ]
        if Measurement in final_moment_composition:
            depth -= 1
        else:
            warnings.warn("Measurement has not been added to the circuit yet.")
        return {
            "width": len(self.qregs)
            if isinstance(self.qregs, list)
            else self.qregs + len(self.cregs)
            if isinstance(self.cregs, list)
            else self.qregs,
            "depth": depth,
        }
        raise NotImplementedError

    def __validate_gate_inputs(self, qreg: int, dims: Optional[int]):
        """
        Responsible for checking if the register number or the dimension of the gates are in the correct bounds.

        :param qreg: The quantum register number for putting the gate
        :param dims: The dimension of the gate
        """
        if type(qreg) is list:
            return [self.__validate_gate_inputs(qreg_i, dims) for qreg_i in qreg]

        if qreg > self._reg_length - 1:
            raise ValueError(
                "Illegal placement of gate. Register specified is out of circuit bounds."
            )
        if dims and dims > self._reg_dims[qreg]:
            raise ValueError("Input dimension is greater than the register dimension.")

    def __add_moment_to_opflow(
        self,
        qreg: "Union[int, tuple[int, int]]",
        gate_obj: Union[HGate, XGate, ZGate, CXGate],
    ) -> bool:
        """
        Creates Moment objects for the given QuantumGate object and pushes it into the OperatorFlow object created earlier

        :param qreg: The quantum register number for putting the gate
        :param gate_obj: Object of one of QuantumGate's child classes, e.g. HGate, XGate, etc.
        :return: True if everything goes well, else False
        """
        _moment_data = []
        gate_obj_added = False
        if isiterable(qreg):
            operation_action_space = list(
                range(qreg[0], qreg[1] + 1)
                if qreg[0] < qreg[1]
                else range(qreg[1], qreg[0] + 1)
            )
        else:
            operation_action_space = []
        for _reg in range(self._reg_length):
            if _reg in operation_action_space:
                if not gate_obj_added:
                    _moment_data.append(gate_obj)
                    gate_obj_added = True
            else:
                _igate = IGate(
                    qreg=_reg, dims=self._reg_dims[_reg], backend=self.backend
                )
                _moment_data.append(_igate)
                if _reg == qreg:
                    _moment_data[_reg] = gate_obj
        _curr_moment = Moment(f"Moment{len(self.op_flow._opflow_list)}", *_moment_data)
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
        _hgate = HGate(
            qreg=qreg, dims=dims or self._reg_dims[qreg], backend=self.backend
        )
        _result = self.__add_moment_to_opflow(qreg, _hgate)
        return _result

    def x(self, qreg: int, dims: Optional[int] = None, plus: Optional[int] = 1) -> bool:
        """
        Responsible for creating the XGate and adding it to OperatorFlow through another function call

        :param qreg: The quantum register number for putting the gate
        :param dims: The dimension of the gate
        :return: True if everything goes well, else False
        """
        self.__validate_gate_inputs(qreg, dims)
        _xgate = XGate(
            qreg=qreg,
            dims=dims or self._reg_dims[qreg],
            plus=plus,
            backend=self.backend,
        )
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
        _zgate = ZGate(
            qreg=qreg, dims=dims or self._reg_dims[qreg], backend=self.backend
        )
        _result = self.__add_moment_to_opflow(qreg, _zgate)
        return _result

    def toffoli(self, qreg: "tuple[list[int], int]", plus: int = 1) -> bool:
        controls, target = qreg

        for i in range(len(controls) - 1):
            self.cx([controls[i], controls[i + 1]], 1)

        self.cx([controls[-1], target], plus)

        for i in range(len(controls) - 1):
            self.cx([controls[i], controls[i + 1]], self.qregs[controls[i + 1]] - 1)

        return True

    def cx(
        self, acting_on: "tuple[int, int]", plus: int, dims: Optional[int] = None
    ) -> bool:
        """
        Responsible for creating the CXGate and adding it to OperatorFlow through another function call

        :param qreg: The quantum register number for putting the gate
        :param dims: The dimension of the gate
        :return: True if everything goes well, else False
        """

        # active_qregs = [
        #     self._reg_dims[qreg] for qreg in [range(acting_on[0], acting_on[1] + 1) if acting_on[0] < acting_on[1] else range(acting_on[1], acting_on[0] + 1)]
        # ]
        if acting_on[0] < acting_on[1]:
            active_qregs = self._reg_dims[acting_on[0] : acting_on[1] + 1]
        else:
            active_qregs = self._reg_dims[acting_on[1] : acting_on[0] + 1]

        _cxgate = CXGate(
            qreg=active_qregs, acting_on=acting_on, plus=plus, backend=self.backend
        )

        _result = self.__add_moment_to_opflow(acting_on, _cxgate)

        return _result
    
    def gate(self, gate: QuantumGate, qreg: int, dims: Optional[int] = None) -> bool:
        """
        Responsible for creating any arbitary gate and adding it to OperatorFlow through another function call

        :param gate: The quantum register number for putting the gate
        :param qreg: The quantum register number for putting the gate
        :param dims: The dimension of the gate
        :return: True if everything goes well, else False
        """
        self.__validate_gate_inputs(qreg, dims)
        if type(qreg) is int:
            _gate = gate(
                qreg=qreg, dims=dims or self._reg_dims[qreg], backend=self.backend
            )
        elif type(qreg) is list:
            _gate = gate(
                qreg=qreg, dims=dims or [ self._reg_dims[qreg_i] for qreg_i in qreg ], backend=self.backend
            )
        _result = self.__add_moment_to_opflow(qreg, _gate)
        return _result

    def measure(self, qreg: int) -> NotImplementedError:
        """
        Responsible for creating the Measurement Gate and adding it to OperatorFlow through another function call

        :param qreg: The quantum register number for putting the gate
        :param dims: The dimension of the gate
        :return: True if everything goes well, else False
        """
        raise NotImplementedError

    def measure_all(self) -> Literal[True]:
        """
        Responsible for creating the Measurement Gate and adding it to OperatorFlow through another function call.
        Contrary to the measure function, this method applies a Measurement Gate across all gates in a single Moment.


        :return: True if everything goes well, else False
        """
        # Adds Operator flow object and push the Measurement object into
        # Operator Flow stack
        _measurement_moment = [
            Measurement(qreg=_index) for _index in range(self._reg_length)
        ]
        _m = Moment(f"Moment{len(self.op_flow._opflow_list)}", *_measurement_moment)
        self.op_flow.populate_opflow(_m)

        return True

    def __initialize_states(self):
        """
        Initializes the qudits to |0> state or |N> state depending on the dimensions of the qubits
        """
        # Adds Operator flow object and push the init object into Operator Flow
        # stack
        _init_gates = [
            InitState(
                dim=self._reg_dims[_index],
                state=_element,
                qreg=_index,
                backend=self.backend,
            )
            for _index, _element in enumerate(self.init_states)
        ]

        init_moment = Moment(f"Moment{len(self.op_flow._opflow_list)}", *_init_gates)
        self.op_flow.populate_opflow(init_moment)

    def run(
        self,
    ):
        # FIXIT:  Every time i run `self.op_flow.exec(self.backend)`, the answer changes.
        # FIXED
        return self.output_processor(self.op_flow.exec(self.backend))

    def print_opflow_list(self):
        for i in self.op_flow.peek():
            i: Moment = i
            print(i.peek_list(), "\n")
