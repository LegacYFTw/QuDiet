from numba import njit
from scipy import sparse
from scipy.sparse import csr_matrix, dok_matrix
import numpy as np


class InitState:

    
    def __init__(self, dim: int, state: int, qreg: int):
        """
        This is the InitState class which initializes the lines on the QuantumRegister object.
        :param dim:   Represents the dimension of the current wire. Takes integer values. Eg.: 3 represents a qutrit
                      and 4 represents a ququart state.
        :param state: Represents the state in which it is to be initialized.
        :param qreg:   Represents the position of the init state in the circuit.
        """
        if dim < state or dim < 2:
            raise ValueError('Please check values of dim and state')
        else:
            self.dim = dim
            self.state = state
            self.qreg = qreg
            self.init_state = dok_matrix(np.zeros((dim, 1)))
            self.init_state[state] = 1
            self.init_state = csr_matrix(self.init_state)

        print("------------------------------------------------")
        print(f"State {self.state} initialized \n")
        print("Statevector given by: ")
        print(self.get_init_states().todense())


    
    def get_init_states(self) -> sparse:
        return self.init_state
    
    @property
    def unitary(self) -> sparse:
        return self.init_state
