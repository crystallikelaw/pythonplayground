def golomb(n: int) -> list:
    '''
    golomb sequence
    '''
    assert type(n) is int, 'input must be int'
    assert n >= 0, 'input must be >= 0'
    seq = [1]
    i = 0
    while len(seq) < n:
        i += 1  # reads terms of sequence
        next = seq[-1] + 1  # iterates to next integer
        seq.append(next)  # adds one term, otherwise index might not exist
        for j in range(seq[i] - 1):  # adds appropriate terms
            if len(seq) == n:  # in case length reached
                break
            seq.append(next)
    return seq


def counter(seq: list) -> list:
    '''
    returns a list comprised of runs of the original list
    '''
    assert type(seq) is list, 'input must be a list'
    assert len(seq) > 0, 'list must be nonempty'
    runs = []
    count = 1
    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            count += 1
        else:
            runs.append(count)
            count = 1
    runs.append(count)
    return runs


if __name__ == '__main__':
    # print values such that golomb(i) is done
    for i in range(1, 101):
        gol = golomb(i)
        c = counter(gol)
        if c == gol[:len(c)]:
            print(i)
    print(golomb(22))
    print(counter(golomb(22)))
