"""Generators
This class creates a generator than can be used in simulations.

Generators are set set using parameters, or can be set 
by reading actual histories and calculating those
parameters.

"""

import numpy as np

class Generator:

    def __init__(self, distribution='normal'):
        """ Initializes the Generator instance

        Parameters
        ----------
        distribution: str
            Which distribution you would like used to generate the demand
            (default: normal)
            (options: normal, lognormal, range)
            note: range changes the functions from mu/sigma to low/high
        
        """

        self.distribution = distribution
        print(f'Generator initialized as a {self.distribution} distribution ')

    def generate(self, mu, sigma, periods=1):
        """ Generates a random array of values matching the parameters fed

        Parameters
        ----------
        mu : float
            the mean of the demand you would like generated
            note: for lognormal, this is the is mean of the log observations
            note: if choosing range, this is the low inclusive of the range, not the mean
        sigma : float
            The standard deviation of the demand you would like generated
            note: for lognormal, this is the standard deviation of the log observations
            note: if choosing range, this is the high inclusive of the range, not the standard deviation
        periods : integer, optional
            How many random points you would like generated
            (default: 1)

        Returns
        -------
        array
            an array of randomly generated numbers using the parameters fed
        """

        if self.distribution == 'range':
            return np.random.random_integers(mu, sigma+1, periods)
        elif self.distribution == 'lognormal':
            return np.random.lognormal(mu, sigma, periods)
        elif self.distribution == 'normal':
            return np.random.normal(mu, sigma, periods)
        else: return 'No Distribution Specified'


    def mimic(self, X, periods=1):
        """ Copies parameters from a fed array and mimics them as a simulation

        Parameters
        ----------
        X : array
            An array of data to extract parameters from
        periods : integer, optional
            How many random points you would like generated
            (default: 1)

        Returns
        -------
        array
            an array of randomly generated numbers using the parameters fed

        Notes
        -----
        Currently only works for 'range' and 'normal' distributions
        """
        if self.distribution == 'range':
            mu = np.max(X),
            sigma = np.min(X),
            return self.generate(mu, sigma, periods)
        elif self.distribution == 'normal':
            mu = np.mean(X),
            sigma = np.std(X),
            return self.generate(mu, sigma, periods)
        else: return 'Distribution not calculated'

