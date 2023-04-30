# broyden's method optimization
import scipy.optimize as sp


def F(x):
    return x**3 + 2 - 2 * x
    # return -(x + 5)**2


y = sp.broyden1(F, .5, f_tol=1e-14)

print(y)
