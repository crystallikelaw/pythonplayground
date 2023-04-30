
# coding: utf-8

# In[ ]:

"""
Value Iteration for the One Sector Growth Model with Convex Adjutment Costs(deterministic)
"""

# Log utility
# F(k) = k**alpha
# Convex adjustment costs = phi*i(t)/2*k(t) per unit of i(t)
# Budget Constraint: F(k(t)) = c(t) + (1 + phi*i(t)/2*k(t))*i(t)
# Capital accumulation: k(t+1) = (1 - delta)*k(t) + i(t)
# Total supply: f(k(t)) = F(k(t)) + (1-delta)*k(t)

from scipy import linspace, interp  # for grid and linear interpolation
from scipy.optimize import fminbound
import numpy as np
import matplotlib.pyplot as plt

# specify parameters and return (period Utility) function

delta,alpha,beta,phi = 0.3,0.8,0.9,1

# depreciation rate, production exponent, discount factor, coefficient of adjustment costs are above
# the period utility is below, as a function of current capital stock k
# and next period's capital stock y

def U(k,y): 
	return np.log(k**alpha + (1-delta)*k -(phi/(2*k))*(y - (1- delta)*k)**2 - y) 

# specify the steady state capital stock

kstar = ((2 + 2*phi*delta - 2*beta - 2*phi*beta*delta + 2*beta*delta + phi*beta*(delta)**2)/2*beta*alpha)**(1/(alpha-1))

# steady state capital stock has been calculated manually
# at the intersection of q(t+1) - q(t) = k(t+1) - k(t) = 0
# We get qstar = 1 + phi(istar/kstar) = 1 +phi*delta (since at steady state i = delta*k, from k(t+1) = k(t))
#Subsitute qstar and istar into FOC for k(t+1) to get required kstar

# specify grid around steady state capital stock

gridsize=1000
gridmin=1                   # so log of this is a positive capital stock
gridmax=1.2*kstar
grid=linspace(gridmin**1e-1,gridmax**1e-1,gridsize)**10

# specify the Bellman operator

def argmax(h,a,b):
	return fminbound(lambda x:-h(x),a,b)

def maximum(h,a,b):
	return h(fminbound(lambda x:-h(x),a,b))

def bellman(w):
    Tw=[]
    for k in grid:
        rhs = lambda y: U(k,y) + beta*w(y)
        Tw.append(maximum(rhs,gridmin,k))
    return lambda x:interp(x,grid,Tw)

# specify Value Iteration

valfunc=lambda x: x
tol=0.001
while 1:
    plt.plot(grid,valfunc(grid),'r-')
    newvalfunc=bellman(valfunc)
    if max(abs(newvalfunc(grid)-valfunc(grid))) < tol:
        break
    valfunc=newvalfunc
plt.show()

