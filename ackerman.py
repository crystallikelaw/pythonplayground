import sys

# sys.setrecursionlimit(10**9)

# print(sys.getrecursionlimit())
doot = 0
# def ackermann(m,n):
#     assert m >= 0, 'doot'
#     assert n >= 0, 'doot'
#     if m == 0:
#         return n + 1
#     elif n == 0:
#         return ackermann(m - 1, 1)
#     else:
#         return ackermann(m - 1, ackermann(m, n - 1))


def ackermann(m, n):
    global doot
    try:
        doot += 1
        if m == 0:
            # BASE CASE
            return n + 1
        elif m > 0 and n == 0:
            # RECURSIVE CASE
            return ackermann(m - 1, 1)
        elif m > 0 and n > 0:
            # RECURSIVE CASE
            return ackermann(m - 1, ackermann(m, n - 1))
    except:
        pass
        # print(doot)


print(ackermann(4, 1))
# print(doot)
