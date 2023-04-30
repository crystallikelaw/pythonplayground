import numpy as np
from numpy import sort


def mean(a):
    assert type(a) is list
    _ = 0
    for i in a:
        _ += i
    return _ / len(a)


def var(a):
    _ = 0
    _m = mean(a)
    for i in a:
        _ += (i - _m)**2
    return _ / len(a)


def med(a):
    if len(a) % 2 == 0:
        return [np.sort(a)[int(len(a) / 2) - 1], np.sort(a)[int(len(a) / 2)]]
    else:
        return np.sort(a)[int(np.floor(len(a) / 2))]


a = [10, 2, 38, 23, 38, 23, 21, 5]
b = [-5, 3, 12, 190, -10]

print(sort(a))
print(mean(a))
