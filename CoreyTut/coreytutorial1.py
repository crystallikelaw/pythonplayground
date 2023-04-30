from random import randint


def tossCoin(numflips):  # def name(input):
    num = numflips  # input =
    # list flips = random draw from (0,1) for each r in range input
    flips = [randint(0, 1) for r in range(num)]
    results = []  # empty list results
    for object in flips:  # for each object in results
        if object == 0:  # 0 is tails
            results.append('Heads')  # write 'heads' in the list results
        elif object == 1:
            results.append('Tails')  # else write 'tails'
    print(str(results.count("Heads")))  # count the 'heads'


tossCoin(5000)
