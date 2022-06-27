from scipy.sparse import csr_matrix, csc_matrix, coo_matrix
from scipy import sparse


class NState:
    def __init__(self, dim: int, state: int):
        if dim < state or dim < 2:
            raise Exception('Please check values of dim and state')
        else:
            self.dim = dim
            self.state = state

    def generate_state(self, dim, state):
        """

        :param dim: Dimension of the circuit line. dim cannot be less than 2 as it represents a qubit. For eg: dim=3
                    represents a qutrit, etc.
        :param state: The exact state that the current circuit line is to be initialized in. For eg:
                  The state |0> in a qubit (dim = 2) is represented by:
                  [1,
                  0]
        :return: Returns a sparse array of the initialized qubit
        """

        init_state = sparse.eye(dim, n=1)
        init_state[state-1] = 1

        return init_state

