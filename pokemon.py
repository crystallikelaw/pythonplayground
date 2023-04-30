# moves necessary to have a 'super-effective' move against every single-typed pokemon
import numpy as np
from itertools import combinations

off_types = {
    'normal': np.array([1, 1, 1, 1, 1, .5, 1, 0, .5, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
    'fighting': np.array([2, 1, .5, .5, 1, 2, .5, 0, 2, 1, 1, 1, 1, .5, 2, 1, 2, .5]),
    'flying': np.array([1, 2, 1, 1, 1, .5, 2, 1, .5, 1, 1, 2, .5, 1, 1, 1, 1, 1]),
    'poison': np.array([1, 1, 1, .5, .5, .5, 1, .5, 0, 1, 1, 2, 1, 1, 1, 1, 1, 2]),
    'ground': np.array([1, 1, 0, 2, 1, 2, .5, 1, 2, 2, 1, .5, 2, 1, 1, 1, 1, 1]),
    'rock': np.array([1, 1, 0, 2, 1, 2, .5, 1, 2, 2, 1, .5, 2, 1, 1, 1, 1, 1]),
    'bug': np.array([1, .5, 2, 1, .5, 1, 2, 1, .5, 2, 1, 1, 1, 1, 2, 1, 1, 1]),
    'ghost': np.array([0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, .5, 1]),
    'steel': np.array([1, 1, 1, 1, 1, 2, 1, 1, .5, .5, .5, 1, .5, 1, 2, 1, 1, 2]),
    'fire': np.array([1, 1, 1, 1, 1, .5, 2, 1, 2, .5, .5, 2, 1, 1, 2, .5, 1, 1]),
    'water': np.array([1, 1, 1, 1, 2, 2, 1, 1, 1, 2, .5, .5, 1, 1, 1, .5, 1, 1]),
    'grass': np.array([1, 1, .5, .5, 2, 2, .5, 1, .5, .5, 2, .5, 1, 1, 1, .5, 1, 1]),
    'electric': np.array([1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 2, .5, .5, 1, 1, .5, 1, 1]),
    'psychic': np.array([1, 2, 1, 2, 1, 1, 1, 1, .5, 1, 1, 1, 1, .5, 1, 1, 0, 1]),
    'ice': np.array([1, 1, 2, 1, 2, 1, 1, 1, .5, .5, .5, 2, 1, 1, .5, 2, 1, 1]),
    'dragon': np.array([1, 1, 1, 1, 1, 1, 1, 1, .5, 1, 1, 1, 1, 1, 1, 2, 1, 0]),
    'dark': np.array([1, .5, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, .5, .5]),
    'fairy': np.array([1, 2, 1, .5, 1, 1, 1, 1, .5, .5, 1, 1, 1, 1, 1, 2, 2, 1])
}

# # gen def_types from off types
# dt = np.zeros((18, 18))
# ticker = -1
# for d in off_types:
#     d = list(off_types[d])
#     ticker += 1
#     for _ in range(18):
#         # print(type(_), type(ticker), d)
#         dt[_, ticker] = d[_]
# ks = [d for d in off_types]
# def_types = {ks[i]: dt[i] for i in range(18)}

def_types = {
    'normal': np.array([1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
    'fighting': np.array([1, 1, 2, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 2]),
    'flying': np.array([1, 0.5, 1, 1, 0, 0, 2, 1, 1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1]),
    'poison': np.array([1, 0.5, 1, 0.5, 2, 2, 1, 1, 1, 1, 1, 0.5, 1, 2, 1, 1, 1, 0.5]),
    'ground': np.array([1, 1, 1, 0.5, 1, 1, 0.5, 1, 1, 1, 2, 2, 0, 1, 2, 1, 1, 1]),
    'rock': np.array([0.5, 2, 0.5, 0.5, 2, 2, 1, 1, 2, 0.5, 2, 2, 1, 1, 1, 1, 1, 1]),
    'bug': np.array([1, 0.5, 2, 1, 0.5, 0.5, 2, 1, 1, 2, 1, 0.5, 1, 1, 1, 1, 1, 1]),
    'ghost': np.array([0, 0, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1]),
    'steel': np.array([0.5, 2, 0.5, 0, 2, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 1, 0.5]),
    'fire': np.array([1, 1, 1, 1, 2, 2, 2, 1, 0.5, 0.5, 2, 0.5, 1, 1, 0.5, 1, 1, 0.5]),
    'water': np.array([1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 0.5, 2, 2, 1, 0.5, 1, 1, 1]),
    'grass': np.array([1, 1, 2, 2, 0.5, 0.5, 1, 1, 1, 2, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1]),
    'electric': np.array([1, 1, 0.5, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 0.5, 1, 1, 1, 1, 1]),
    'psychic': np.array([1, 0.5, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0.5, 1, 1, 2, 1]),
    'ice': np.array([1, 2, 1, 1, 1, 1, 2, 1, 2, 2, 1, 1, 1, 1, 0.5, 1, 1, 1]),
    'dragon': np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 1, 2, 2, 1, 2]),
    'dark': np.array([1, 2, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 0, 1, 1, 0.5, 2]),
    'fairy': np.array([1, 0.5, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 0, 0.5, 1])
}

# all type combinations, dual and single
tcomb = combinations(def_types, 2)
tcomb = list(tcomb)
for d in def_types:
    a = (d,)
    tcomb.append(a)

tweak = []  # for each tc, weakness chart
for i in tcomb:
    if len(i) > 1:
        tweak.append(np.array([a * b for a, b in zip(def_types[i[0]], def_types[i[1]])]))
    else:
        tweak.append(def_types[i[0]])

# print(tweak)

for i in tweak:
    # print(i)
    # print(max(i))
    # break
    if max(i) <= 1.1:
        p rint(i)
