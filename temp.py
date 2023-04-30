# # import pandas as pd
import numpy as np
# # # import concurrent.futures
# # # import copy

# # # executor = concurrent.futures.ThreadPoolExecutor(5)


# # # def multi(x):  # outer function that runs another function multiple times
# # #     temp = copy.deepcopy(x)  # don't want to work on original input
# # #     def single():  # function to run multiple times
# # #         nonlocal temp
# # #         temp.append(2)
# # #     if __name__ == '__main__':
# # #         futures = [executor.submit(single(), item) for item in range(2)]
# # #         concurrent.futures.wait(futures)
# # #     temp.append(1)
# # #     return temp

# # # a = [21]
# # # multi(a)
# # # print(a, multi(a))  # this returns [21, 2, 2, 1] and not [21]


# # a = [1, 2, 2]
# # a.remove(2)
# # print(a)


# class hand:  # actions are deterministic
#     def __init__(self, card1, card2):
#         # self.card1 = card1
#         # self.card2 = card2
#         self.cards = [np.min([card1, card2]), np.max([card1, card2])]

# a = hand(1, 2)

# print(a.cards)

# # a.card2 = 0
# # a.__init__(a.cards[0], 0)
# # print(a.cards)

# def func(temp):
#     temp.__init__(temp.cards[1], 5)

# func(a)
# print(a.cards)

# print([np.min([6, 2]), np.max([6, 2])][1])
# a = [1, 2]

# b = a.remove(2)
# print(a)
temp = [3np.nonzero(p2.cards)[0][0], 5, 4, 1, 0]
# temp.remove(1)
# owncard = temp
# print(owncard)
print(temp[np.nonzero(temp)[0][0]])
