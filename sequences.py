import matplotlib.pyplot as plt
import seaborn as sns
from math import floor, sqrt
from Prime_Check import primetest

sns.set_style("darkgrid")


# Van Eck Sequence
# https://en.wikipedia.org/wiki/Van_Eck%27s_sequence
# n th term is 0 iff n-1 th term has occured for the first time, else distance to previous occurance


def _ret_last_index(x: object, k: list) -> int:
    '''
    return index of last occurance of x in k
    https://stackoverflow.com/questions/6890170/how-to-find-the-last-occurrence-of-an-item-in-a-python-list
    '''
    return len(k) - max(loc for loc, val in enumerate(k) if val == x)


def vaneck_seq(n: int) -> list:
    '''
    return's vaneck sequence of length n
    '''
    assert type(n) is int, 'input must be int'
    assert n >= 1, 'input must be >= 1'
    a = [0]
    while len(a) < n:
        if a.count(a[-1]) == 1:  # if it's the first time a[-1] appeared
            a.append(0)
        else:
            a.append(_ret_last_index(a[-1], a[0:-1]))  # last index before a[-1]
    return a


def vaneck_term(n: int) -> int:
    '''
    returns n th term of vaneck sequence
    '''
    return vaneck_seq(n)[-1]


# Fibonacci Sequence


def fibonacci(n: int) -> list:
    '''
    Prints out n terms of the fibonacci sequence
    '''
    assert type(n) is int, 'input must be int'
    assert n >= 1, 'input must be >= 1'
    if n == 1:
        return [1]
    else:
        temp = [1, 1]
        while len(temp) < n:
            temp.append(temp[-1] + temp[-2])
        return temp


def fib_term(n):
    '''
    returns n th term of fibonacci sequence
    '''
    return fibonacci(n)[-1]

# Abundant number
# https://www.wikiwand.com/en/Abundant_number
# must be smaller than the sum of it's proper divisors


def _proper_divisors(n: int) -> list:
    '''
    returns all devisors
    '''
    assert type(n) is int, 'input must be int'
    assert n >= 1, 'input must be >= 1'
    _temp = [1]
    root_n = sqrt(n)
    # all factor pairs must have 1 term <=sqrt
    for i in range(2, floor(root_n) + 1):
        if n % i == 0:
            _temp.append(int(i))
            _temp.append(int(n / i))  # counterpart factors
    # duplication of sqrt_n if integral
    if root_n == floor(root_n):
        _temp.remove(root_n)
    _temp.sort()
    return _temp


def abundant_sequence(n: int) -> tuple:
    '''
    returns the first n abundant numbers:
    a number that is smaller than the sum of its proper divisors
    https://www.wikiwand.com/en/Abundant_number
    '''
    seq = []  # container for sequences
    abnd = [] # abundance, ie sum of divisors - number
    j = 1
    while len(seq) < n:
        while True:
            _temp = sum(_proper_divisors(j))
            if _temp > j:
                seq.append(j)
                abnd.append(_temp - j)
                j += 1
                break  # exits while True
            j += 1
    return seq, abnd


def abundant_term(n: int) -> int:
    '''
    returns the nth abundant number
    '''
    return abundant_sequence(n)[0][-1]


if __name__ == '__main__':
    n = 10
    print('Van Eck Sequence is ', vaneck_seq(n))
    # plt.plot(vaneck_seq(n))
    # plt.show()
    print('Fibonacci Sequence is ', fibonacci(n))
    # plt.plot(fibonacci(n))
    # plt.show()
    print('Abundant Sequence is ', abundant_sequence(n)[0])
    print('Divisors of', abundant_term(n), 'are', _proper_divisors(abundant_term(n)), ', which sum to', abundant_term(n), '+', abundant_sequence(n)[1][-1])
    primetest(n, 1)
