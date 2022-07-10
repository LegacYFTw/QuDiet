from numba import njit
from scipy import sparse
from scipy.sparse import csr_matrix, dok_matrix


class InitState:

    @njit
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
            self.init_state = dok_matrix(sparse.eye(dim, n=1))
            self.init_state[state] = 1
            self.init_state = csr_matrix(self.init_state)

    @njit
    def get_init_states(self) -> sparse:
        return self.init_state
