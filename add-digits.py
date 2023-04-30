def add_dig(n: int) -> int:
    '''
    incident (stroke?) add to total
    '''
    assert type(n) is int, 'input must be int'
    assert n >= 0, 'input must be >= 0'
    steps = 0
    digits = [int(x) for x in str(n)]
    while len(digits) > 1:
        digits = [int(x) for x in str(sum(digits))]
        steps += 1
    return steps


if __name__ == '__main__':
    # finds the number needing the most steps below number
    number = 10000000

    result = 0
    steps = 0
    for x in range(10, number):
        if add_dig(x) > steps:
            steps = add_dig(x)
            result = x
    print(result, steps)
