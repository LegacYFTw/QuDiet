from itertools import product
from itertools import groupby
from typing import Union

from qudiet.circuit_library import ArbitaryGate
from qudiet.core.backend.core import Backend
from qudiet.core.backend.NumpyBackend import NumpyBackend
import numpy as np

from pprint import pprint

def generate_combinations(base_list):
    # Use itertools.product to generate all combinations
    return list(product(*(range(base) for base in base_list)))

def toffoli_dm(qargs, plus, dims, ):
    # dims = [2, 3, 2, 4, 3]
    # qargs = ([0, 1], 3)
    # plus = 3

    c, t = qargs

    # 0, 3
    lb, ub = min(c + [t]), max(c + [t])

    # 1, 2, 1, 1
    max_cap = [ dims[x] - 1 for x in range(lb, ub + 1) ] # highest activates state

    # 24
    size_exp = np.product([ dims[x] for x in range(lb, ub + 1) ]) # size_exp x size_exp Matrix

    # Ordered indexes
    # 0000 0001 0010 0011 0100 0101 0110 0111 0200 0201 0210 0211 ... 1210 1211 (24 elements)
    indexes = generate_combinations( [ dims[x] for x in range(lb, ub + 1) ] )
    assert len(indexes) == size_exp


    replacement_dict = {}
    replacement_dict_human = {}

    idx_to_consider = []
    matindexes_to_consider = []

    # c1, c2 = c
    # for idx, mat_index in enumerate(indexes):
    #     if mat_index[c1 - lb] == max_cap[c1 - lb] and mat_index[c2 - lb] == max_cap[c2 - lb]:
    #         idx_to_consider.append(idx)

    nindex = np.array(indexes)
    recalc_c = [_c -lb for _c in c]
    rows_columns = np.where(np.all(nindex.T[recalc_c].T == np.array(max_cap)[recalc_c], axis=1))

    idx_to_consider = list(rows_columns[0])


    while idx_to_consider:
        idx = idx_to_consider.pop(0)
        ctl_index = list(indexes[idx])
        tgt_index = ctl_index.copy()
        tgt_index[t - lb] = (tgt_index[t - lb] + plus) % dims[t]
        tgt_index = tuple(tgt_index)
        tgt_index_at = indexes.index(tgt_index)
        replacement_dict[idx] = tgt_index_at
        replacement_dict_human[tuple(ctl_index)] = tgt_index
    
    # pprint(replacement_dict_human)


    I = np.identity(size_exp)

    create_identity = []

    for row_idx in range(size_exp):
        idx = replacement_dict.get(row_idx, row_idx)
        create_identity.append(I[idx])
    
    return np.array(create_identity).T, lb, ub

class Toffoli(ArbitaryGate):
    def __init__(self, qreg: int, dims: Union[int, tuple], plus:int = 1, backend: Backend = NumpyBackend):
        _unitary, lb, ub = toffoli_dm(qreg, plus, dims)
        self._acting_on = list(range(lb, ub+1)) 
        super().__init__(qreg, [dims[a] for a in self._acting_on], backend)
        self._unitary = _unitary
        self._plus = plus
        self.controls = qreg[0]
        self.target = qreg[1]
        print(f"[debug] inside Toffoli constructor: controls={self.controls} target={self.target}")