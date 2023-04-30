import numpy as np


def end(x, y, start, stop, rad):
    return (x - rad * np.cos(start + 180) + rad * np.cos(stop), y - rad * np.sin(start + 180) + rad * np.sin(stop))


print(end(-1, 0, 40, 155, 3))
