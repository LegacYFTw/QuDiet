from scipy.sparse import csr_matrix, csc_matrix, coo_matrix
from scipy import sparse


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
            raise Exception('Please check values of dim and state')
        else:
            self.dim = dim
            self.state = state
            self.qreg = qreg
            self.init_state = sparse.eye(dim, n=1)
            self.init_state[state] = 1

    def get_init_states(self) -> sparse:
        return self.init_state


