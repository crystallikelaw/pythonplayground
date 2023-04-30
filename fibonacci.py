import numpy as np


def fibfiull(n: int) -> int:
    '''
    first n fibbonaci terms
    f(x) = x + f(x-1)
    '''
    assert n > 0
    assert type(n) is int
    _cont = []
    while len(_cont) < n:
        if len(_cont) < 2:
            _cont.append(1)
        else:
            _cont.append(_cont[-1] + _cont[-2])
    return _cont


def fibrec(x):
    assert x > 0
    if switch:
        _cont = []
    while len(_cont) < x:
        if len(_cont) < 2:
            _cont.append(1)
        else:
            _cont.append(fibrec(x - 1))
            switch = 1
            break
        print(_cont)
    return _cont


print(fibrec(20))
