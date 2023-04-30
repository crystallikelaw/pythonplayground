# To find arithmetic-geometric mean of numbers
# agm takes a>b, every iteration a = arithmetic mean of a,b and b = geom mean of a,b
# agm at convergence

# import numpy as np
from numpy import maximum, minimum, isclose, mean
from scipy.stats.mstats import gmean


def agm(x, y, itmax=1000):
    '''
    returns the arithmetic geometric mean of two non-negative numbers
    maxiterations = 1000
    '''
    assert x is int or float and x >= 0
    assert y is int or float and y >= 0
    a = maximum(x, y)
    b = minimum(x, y)
    it = 0
    while not isclose(a, b) and it < itmax:
        a_1 = mean([a, b])
        b_1 = gmean([a, b])
        if not a_1 <= a or not b <= b_1:
            raise RuntimeError('means diverge')
        it += 1
        a = a_1
        b = b_1
    if not it < itmax:
        raise RuntimeError('iteration limit reached')
    return a


def agm_to_unity(a, itmax=1000):
    '''
    steps till agm(1,x) goes to 1
    '''
    it = 0
    # while not isclose(a, 1):
    while a >= 2:
        it += 1
        a = agm(1, a)
        if not it < itmax:
            raise RuntimeError('iteration limit reached')
    return it


def am_to_unity(a, itmax=1000):
    '''
    steps till mean(1,x) goes to 1
    '''
    it = 0
    # while not isclose(a, 1):
    while a >= 2:
        it += 1
        a = mean([1, a])
        if not it < itmax:
            raise RuntimeError('iteration limit reached')
    return it


def gmean_to_unity(a, itmax=1000):
    '''
    steps till gmean(1,x) goes to 1
    '''
    it = 0
    # while not isclose(a, 1):
    while a >= 2:
        it += 1
        a = gmean([1, a])
        if not it < itmax:
            raise RuntimeError('iteration limit reached')
    return it


print(agm(20, 24))
