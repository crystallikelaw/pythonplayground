import itertools
# # import numpy as np

end = 10
for end in [6, 8, 10]:
    nos = list(range(0, end))
    perms = list(itertools.permutations(nos))
    fail_cont = 0

    for item in perms:
        num_cont = []
        for num in item:
            success = False
            if num in num_cont:
                continue
            num_cont = []
            while not success:
                if item[num] in num_cont:
                    success = True
                num_cont.append(num)
                num = item[num]
            if len(num_cont) > len(nos)/2:
                fail_cont = fail_cont + 1
                break
            # if len(num_cont) > len(nos)/2:
            #     break
    print(end, ':', 1 - fail_cont/len(perms))
