from random import random
# from random import randint


# def fairCoin(numflips: int) -> float:
#     '''
#     Tosses a fair coin several times, and gives you the estimated probability of heads
#     '''
#     assert type(numflips) is int, 'input must be int'
#     assert numflips >= 0, 'input must be >= 0'
#     flips = [randint(0, 1) for r in range(numflips)]  # random draw from (0,1) for each r in range input
#     return sum(flips) / numflips


def coinFlip(n: int, p: float = .5) -> float:
    '''
    given probability of heads p and number of flips n,
    returns estimated probability of heads
    '''
    assert type(n) is int, 'input must be int'
    assert n >= 0, 'input must be >= 0'
    assert 1 >= p >= 0, 'probability not in [0, 1]'

    heads = sum([1 if random() <= p else 0 for i in range(n)])

    return heads / n


if __name__ == '__main__':
    number_toss = 1000
    prob_heads = 0.56
    average_prob_heads = coinFlip(number_toss, prob_heads)
    average_prob_tails = 1 - average_prob_heads

    # We print the results...
    print("- Number of tosses = " + str(number_toss))
    print("- Defined probability of Heads = " + str(prob_heads))
    print("- Proportion of Heads for " + str(number_toss) + " tosses = ", coinFlip(number_toss, prob_heads))
    print("- Proportion of Tails for " + str(number_toss) + " tosses = ", 1 - coinFlip(number_toss, prob_heads))
