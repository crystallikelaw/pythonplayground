import random
import math

coprime = 0
cofactor = 0

t = 0

while(t < 10000):
    a = random.randint(1, 12300)
    b = random.randint(1, 12300)
    i = 2
    while (True):
        if i == a or i == b:
            coprime = coprime + 1
            break
        elif a % i == 0 and b % i == 0:
            cofactor += 1
        i += 1
    t += 1

print("pi is aprox. " + str(math.sqrt(6 / (coprime / (cofactor + coprime)))) + ", HUMAN!")
exit()
