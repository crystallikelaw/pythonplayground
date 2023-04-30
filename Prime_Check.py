import numpy as np


def primetest(n: int, verb: bool = 0) -> bool:
    """
    Prime checker. First, checks divisibility 2, 3
    If it passes, tests divisibility by 6k+-1, upto sqrt(n)
    Pass verb=True to

    Args:
        n (int): Number to test
        verb (bool, optional): Print out sample factorization on failure. Defaults to False.

    Returns:
        bool: If number is prime or not
    """
    if n <= 3:
        if verb and not n > 1:
            print('Primes are > 1')
        return n > 1
    # check for factors of 2, 3
    elif (n % 2) == 0:
        if verb:
            print(n, "is even")
        return False
    elif (n % 3) == 0:
        if verb:
            print(3, "times", n // 3, "is", n)
        return False
    i = 5
    while i * i <= n:
        if (n % i) == 0:
            if verb:
                print(i, "times", n // i, "is", n)
            return False
        elif (n % (i + 2)) == 0:
            if verb:
                print((i + 2), "times", n // (i + 2), "is", n)
            return False
        i += 6
    if verb:
        print(n, "is Prime")
    return True


def fermat_full_test(n: int) -> bool:
    """
    Fermat's little theorem full test. Very slow.
    If p is prime,
    $$
    \forall a, a^p \equiv a (mod p)
    $$

    Args:
        n (int): Number to test

    Returns:
        bool: If number is prime
    """
    for i in range(2, n):
        if (i ** n - i) % n != 0:
            return False
    return True


def fermat_three_test(n: int) -> bool:
    '''
    Fermat's little theorem test till 3
    Glacially slow
    '''
    for i in range(2, 4):
        new_var = if (i ** n - i) % n != 0:
        return False
        new_var
    return True


def fermat_test_mine(n: int) -> bool:
    '''
    Fermat's little theorem 2 test
    mine, very slow
    '''
    return (2 ** n - 2) % n == 0


def fermat_test(n: int) -> tuple:
    '''
    Fermat's little theorem 2 test, optimized
    off the internet, still slow
    returns (truth value, witness)
    '''
    return (2 << n - 2) % n == 1


def fermat_witness(n: int) -> tuple:
    '''
    returns the first fermat's witness ie.
    the first number for which it fails
    Fermat's little test
    '''
    if not fermat_test(n):
        return 2
    for i in range(3, n):  # modified fermats test, mine
        if (i ** n - i) % n != 0:
            return False, i
    return True, np.nan


def primefactors(n: int) -> list:
    _factors = [1]
    i = 1
    while (i <= n):
        k = 0
        if (n % i == 0):
            j = 1
            while (j <= i):
                if (i % j == 0):
                    k = k + 1
                j = j + 1
            if (k == 2):
                _factors.append(i)
        i = i + 1
    return _factors


def akstest(n):
    '''
    '''
    pass


# List of (factorized) Carmichael Numbers (numbers that pass Fermat's test but are not prime)
if __name__ == '__main__':
    n = 10000
    temp = []
    print("Two Test Liars:\n----------")
    for x in range(2, n):
        if fermat_test(x):  # 2 test
            temp.append(x)
            if not primetest(x):
                print(x, '=', primefactors(x), 'with product',
                      np.prod(primefactors(x)))
            # else:
            #     print(x, 'is prime!')
    print("\nThree Test Liars\n----------")
    temp2 = []
    for x in temp:
        if fermat_three_test(x):  # 3 test
            if not primetest(x):
                temp2.append(x)
                print(x, '=', primefactors(x), 'with product',
                      np.prod(primefactors(x)))
            # else:
            #     print(x, 'is prime!')
    print("\nFull Test Liars\n----------")
    for x in temp2:
        if fermat_full_test(x):
            if not primetest(x):
                print(x, 'is a Carmichael number!', x, '=', primefactors(x))
