import random

bign = 0
_t = 0
while bign < 3:
    maxa = 100  # divided out in the end
    testn = 0  # number

    while testn < maxa:
        a = 0  # termination condition
        b = 0  # iterations ^
        while a == 0:
            b += 1
            listofresults = []
            for i in [4, 6, 8, 10, 12, 20, 100]:  # generating dice rolls list
                listofresults.append(random.randint(1, i))
            for i in range(1, 8):
                if i not in listofresults:
                    break
                if i == 7:
                    a = 1
                    # print(listofresults)
                    # print(b)
                    _t += b  # iterations to hit term cond
                    testn += 1  # test number
                    break

    # testreps ~= testn * \bar{b}; result == \bar{b}
    bign += 1

print(_t / (testn * 3))
