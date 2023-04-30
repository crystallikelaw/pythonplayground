import numpy as np

d = 6  # side of dice
exp = (1 + d) / 2
reps = 10000


for n in [10, 20, 50, 100, 200, 1000, 5000, 10000]:  # different number of rolls
    _dev = 0
    for i in range(reps):
        total = np.random.randint(1, d + 1, n).sum()
        est = int(np.round(total / exp))
        _temp = np.abs(est / n - 1)
        if _temp > _dev:
            _dev = _temp

    print("for ", n, " rolls, highest observed (of ", reps, " reps) absolute deviation is ", np.round(_dev * 100, decimals=2), "%", sep="")
