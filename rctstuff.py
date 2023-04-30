'''
evolution of sample mean of a lognormal with an initial 'unlucky' draws
'''

import numpy as np
import scipy.stats as sp

# Underlying distribution parameters
mu = 0
std = .5
max_samp = 10000


def lnormmean():
    '''returns mean of a lognormal,
    for global mu and sigma of generating
    distribution'''
    return(print('True Mean is', np.exp(mu + (std ** 2) / 2)))


def mean_seq(draw, no_bad_draws):
    '''returns evolution of the sample mean starting
    with no_bad_draws of draw, upto max_sam
    number of draws. returns every 20th observation'''
    x = [draw] * no_bad_draws  # unlucky initial draw
    _results = []
    _results.append(draw)  # initial sample mean
    while len(x) < max_samp:
        x.extend(sp.lognorm.rvs(
            scale=np.exp(mu),
            s=std,
            size=int(np.floor(max_samp / 20))
        ))
        _results.append(sum(x) / len(x))
    return(np.array(_results))


lnormmean()
print('Evolution of difference:\n', mean_seq(8, 50) - mean_seq(0, 50))
