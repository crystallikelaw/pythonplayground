'''
Returns all primes upto a certian number using the Sieve of Eratosthenes
'''


def candidate_range(n):
    cur = 5  # >5
    incr = 2  # has to be odd
    while cur < n + 1:
        yield cur
        cur += incr
        incr ^= 6  # or incr = 6-incr, or however


def sieve(end):
    prime_list = [2, 3]  # it's cheating, but easier
    sieve_list = [True] * (end + 1)
    for each_number in candidate_range(end):
        if sieve_list[each_number]:
            prime_list.append(each_number)
            for multiple in range(each_number * each_number, end + 1, each_number):
                sieve_list[multiple] = False
    return prime_list


print(sieve(200))
