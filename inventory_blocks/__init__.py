"""Demand Generator

"""

import numpy as np

def generate_demand(mu, sigma, periods, distribution='normal'):
    if distribution == 'normal':
        return np.random.normal(mu, sigma, periods)
    elif distribution == 'lognormal':
        return np.random.lognormal(mu, sigma, periods)
    