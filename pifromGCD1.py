# pi from gcd(m,n)
import math as m
import random as rand

max = 120  # maximum random numbers
n = 10 ** 6  # number of tries
count = 0

for i in range(n):
    if m.gcd(rand.randint(1, max), rand.randint(1, max)) == 1:
        count = count + 1

pi = (6 / (count / n)) ** (1 / 2)

error = (pi - m.pi) / m.pi * 100

print('my PI = ' + str(pi))
print('error = ' + str(error) + '%')

exit()
