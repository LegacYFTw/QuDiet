import copy
import itertools
import numpy as np
import scipy
import dask.array as da
import functools
import re
from collections import OrderedDict, defaultdict, namedtuple
from typing import (
    Union,
    Optional,
    List,
    Dict,
    Tuple,
    Type,
    TypeVar,
    Sequence,
    Callable,
    Mapping,
    Set,
    Iterable,
)
import typing


class QuantumCircuit:
    instances = 0
    prefix = "circuit"

    # Class variable OPENQASM header
    header = "OPENQASM 2.0;"
    extension_lib = 'include "qelib1.inc";'

    def __init__(self,
                 *regs: Union[Register, int, Sequence[Bit]],
                 name: Optional[str] = None,
                 global_phase: ParameterValueType = 0,
                 metadata: Optional[Dict] = None,
                 ):

        if any(not isinstance(reg, (list, QuantumRegister, ClassicalRegister)) for reg in regs):
            # check if inputs are integers, but also allow e.g. 2.0
            try:
                valid_reg_size = all(reg == int(reg) for reg in regs)
            except (ValueError, TypeError):
                valid_reg_size = False

            if not valid_reg_size:
                raise CircuitError(
                    "Circuit args must be Registers or integers. (%s '%s' was "
                    "provided)" % ([type(reg).__name__ for reg in regs], regs)
                )
            regs = tuple(int(reg) for reg in regs)  # cast to int
            self._base_name = None
            if name is None:
                self._base_name = self.cls_prefix()
                self._name_update()
            elif not isinstance(name, str):
                raise CircuitError(
                    "The circuit name should be a string (or None to auto-generate a name)."
                )
            else:
                self._base_name = name
                self.name = name
            self._increment_instances()

            # Data contains a list of instructions and their contexts,
            # in the order they were applied.
            self._data = []
            # A stack to hold the instruction sets that are being built up during for-, if- and
            # while-block construction.  These are stored as a stripped down sequence of instructions,
            # and sets of qubits and clbits, rather than a full QuantumCircuit instance because the
            # builder interfaces need to wait until they are completed before they can fill in things
            # like `break` and `continue`.  This is because these instructions need to "operate" on the
            # full width of bits, but the builder interface won't know what bits are used until the end.
            self._control_flow_scopes = []

            self.qregs = []
            self.cregs = []
            self._qudits = []
            self._clbits = []

            # Dict mapping Qubit or Clbit instances to tuple comprised of 0) the
            # corresponding index in circuit.{qubits,clbits} and 1) a list of
            # Register-int pairs for each Register containing the Bit and its index
            # within that register.
            self._qudit_indices = {}
            self._clbit_indices = {}

            self._ancillas = []
            self._calibrations = defaultdict(dict)
            self.add_register(*regs)

            # Parameter table tracks instructions with variable parameters.
            self._parameter_table = ParameterTable()

            # Cache to avoid re-sorting parameters
            self._parameters = None

            self._layout = None
            self._global_phase: ParameterValueType = 0
            self.global_phase = global_phase

            self.duration = None
            self.unit = "dt"
            if not isinstance(metadata, dict) and metadata is not None:
                raise TypeError("Only a dictionary or None is accepted for circuit metadata")
            self._metadata = metadata

            @property
            def data(self) -> QuantumCircuitData:
                """Return the circuit data (instructions and context).
                Returns:
                    QuantumCircuitData: a list-like object containing the tuples for the circuit's data.
                    Each tuple is in the format ``(instruction, qargs, cargs)``, where instruction is an
                    Instruction (or subclass) object, qargs is a list of Qubit objects, and cargs is a
                    list of Clbit objects.
                """
                return QuantumCircuitData(self)

            @data.setter
            def data(
                    self, data_input: List[Tuple[Instruction, List[QuditSpecifier], List[ClbitSpecifier]]]
            ):
                """Sets the circuit data from a list of instructions and context.
                Args:
                    data_input (list): A list of instructions with context
                        in the format (instruction, qargs, cargs), where Instruction
                        is an Instruction (or subclass) object, qargs is a list of
                        Qubit objects, and cargs is a list of Clbit objects.
                """

                # If data_input is QuantumCircuitData(self), clearing self._data
                # below will also empty data_input, so make a shallow copy first.
                data_input = data_input.copy()
                self._data = []
                self._parameter_table = ParameterTable()

                for inst, qargs, cargs in data_input:
                    self.append(inst, qargs, cargs)

            @property
            def calibrations(self) -> dict:
                """Return calibration dictionary.
                The custom pulse definition of a given gate is of the form
                    {'gate_name': {(qubits, params): schedule}}
                """
                return dict(self._calibrations)

            @calibrations.setter
            def calibrations(self, calibrations: dict):
                """Set the circuit calibration data from a dictionary of calibration definition.
                Args:
                    calibrations (dict): A dictionary of input in the format
                        {'gate_name': {(qubits, gate_params): schedule}}
                """
                self._calibrations = defaultdict(dict, calibrations)

            @property
            def metadata(self) -> dict:
                """The user provided metadata associated with the circuit
                The metadata for the circuit is a user provided ``dict`` of metadata
                for the circuit. It will not be used to influence the execution or
                operation of the circuit, but it is expected to be passed between
                all transforms of the circuit (ie transpilation) and that providers will
                associate any circuit metadata with the results it returns from
                execution of that circuit.
                """
                return self._metadata

            @metadata.setter
            def metadata(self, metadata: Optional[dict]):
                """Update the circuit metadata"""
                if not isinstance(metadata, dict) and metadata is not None:
                    raise TypeError("Only a dictionary or None is accepted for circuit metadata")
                self._metadata = metadata

            def __str__(self) -> str:
                return str(self.draw(output = "text"))

            def __eq__(self, other) -> bool:
                if not isinstance(other, QuantumCircuit):
                    return False

                # TODO: remove the DAG from this function
                from qiskit.converters import circuit_to_dag

                return circuit_to_dag(self) == circuit_to_dag(other)

            @classmethod
            def _increment_instances(cls):
                cls.instances += 1

            @classmethod
            def cls_instances(cls) -> int:
                """Return the current number of instances of this class,
                useful for auto naming."""
                return cls.instances

            @classmethod
            def cls_prefix(cls) -> str:
                """Return the prefix to use for auto naming."""
                return cls.prefix

            def _name_update(self) -> None:
                """update name of instance using instance number"""
                if not is_main_process():
                    pid_name = f"-{mp.current_process().pid}"
                else:
                    pid_name = ""

                self.name = f"{self._base_name}-{self.cls_instances()}{pid_name}"

            def has_register(self, register: Register) -> bool:
                """
                Test if this circuit has the register r.
                Args:
                    register (Register): a quantum or classical register.
                Returns:
                    bool: True if the register is contained in this circuit.
                """
                has_reg = False
                if isinstance(register, QuantumRegister) and register in self.qregs:
                    has_reg = True
                elif isinstance(register, ClassicalRegister) and register in self.cregs:
                    has_reg = True
                return has_reg

            def reverse_ops(self) -> "QuantumCircuit":
                """Reverse the circuit by reversing the order of instructions.
                This is done by recursively reversing all instructions.
                It does not invert (adjoint) any gate.
                Returns:
                    QuantumCircuit: the reversed circuit.
                Examples:
                    input:
                    .. parsed-literal::
                             ┌───┐
                        q_0: ┤ H ├─────■──────
                             └───┘┌────┴─────┐
                        q_1: ─────┤ RX(1.57) ├
                                  └──────────┘
                    output:
                    .. parsed-literal::
                                         ┌───┐
                        q_0: ─────■──────┤ H ├
                             ┌────┴─────┐└───┘
                        q_1: ┤ RX(1.57) ├─────
                             └──────────┘
                """
                reverse_circ = QuantumCircuit(
                    self.qudits, self.clbits, *self.qregs, *self.cregs, name = self.name + "_reverse"
                )

                for inst, qargs, cargs in reversed(self.data):
                    reverse_circ._append(inst.reverse_ops(), qargs, cargs)

                reverse_circ.duration = self.duration
                reverse_circ.unit = self.unit
                return reverse_circ
