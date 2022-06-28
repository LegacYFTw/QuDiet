from scipy.sparse import csr_matrix, csc_matrix, coo_matrix
from scipy import sparse


class NState:
    def __init__(self, dim: int, state: int):
        if dim < state or dim < 2:
            raise Exception('Please check values of dim and state')
        else:
            self.dim = dim
            self.state = state
            init_state = sparse.eye(dim, n=1)
            init_state[state] = 1

        def get_init_states(self) -> sparse:
            return init_state



