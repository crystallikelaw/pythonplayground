'''
prime check
'''
import sys
import numpy as np
from Prime_Check import primetest
from random import randint


# dumb version 1
def dumber_prime(n):
    '''
    check if the number is 2,3,4,5,7, or 11.
    (because avehi thinks 4 is prime)
    if not, say it is not prime.
    '''
    check = [2,3,4,5,7,11]
    # for i in check:
    # if n in check:
    if i in check:
        print("TRUE")
    else:
        print("FALSE")


for i in range(100):
    if i%2 != 0:
        print(i)


def dumber(n):
    '''
    iterate numbers from 2 to n-1 and check whether n is divisible by these numbers. If n is not divisible by any of these numbers it is prime.
    '''
    assert n > 2
    for i in range(2,n):
        if i >= n / 2:
            print('True')
            return True
        if n / i == np.floor(n / i):
            print('False')
            return False
    print("True")
    return True

def frog_times(lilypads): #todo: this function is terrible
    '''
    Generate it hurts my soul. This description seems adequate.
    '''
    steps = 0
    count = 0
    while count != lilypads:
        step1 = randint(0, lilypads - count)
        count += step1
        steps += 1
    return steps

means = []
for j in range(50, 200):
    a = 0
    for i in range(100):
        a += frog_times(j)
    means.append(a/100)



print(means)
