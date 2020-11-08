"""Demand Generators
These methods simulate various types of demand used in
modeling and optimizing models.

They can be set using parameters, or can be set 
by reading actual histories and calculating those
parameters.

"""

import numpy as np

def generate_demand(mu, sigma, periods=1, distribution='normal'):
    """ generate_demand

    Parameters
    ----------
    mu : float
        the mean of the demand you would like generated
        note: for lognormal, this is the is mean of the log observations
    sigma : float
        The standard deviation of the demand you would like generated
        note: for lognormal, this is the standard deviation of the log observations
    periods : integer, optional
        How many random points you would like generated
        (default: 1)
    distribution : str
        Which distribution you would like used to generate the demand
        (default: normal)
        (options: normal, lognormal)


    Returns
    -------
    array
        an array of randomly generated demands using the parameters fed
    """
    if distribution == 'normal':
        return np.random.normal(mu, sigma, periods)
    elif distribution == 'lognormal':
        return np.random.lognormal(mu, sigma, periods)
