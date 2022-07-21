from framework.utils.numpy import bin_to_Nbase, Nbase_to_bin

def test_bin_to_Nbase():
    _bin = [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    _base = [2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2]

    _repr = bin_to_Nbase(
        _bin, 
        _base
    )

    assert _repr == 23296

    assert bin_to_Nbase([1, 0, 0, 1],  [2, 3, 2, 2]) == 13
    assert bin_to_Nbase([1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2]) == 24576

def test_Nbase_to_bin():

    assert Nbase_to_bin(65, [2, 2, 2, 3, 2, 2]) == [1, 0, 1, 1, 0, 1]
    assert Nbase_to_bin(64, [2, 2, 2, 3, 2, 2]) == [1, 0, 1, 1, 0, 0]

    assert Nbase_to_bin(187, [4, 3, 2, 2, 4]) == [3, 2, 1, 0, 3]
    assert Nbase_to_bin(140, [3, 2, 2, 3, 4][::-1]) == [3, 2, 1, 0, 2]
    
    assert Nbase_to_bin(689, [3, 2, 5, 4, 2, 3]) == [2, 1, 3, 2, 1, 2]

    _repr = 23296
    _base = [2, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2]
    _bin = Nbase_to_bin(_repr, _base)
    
    assert _bin == [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]

