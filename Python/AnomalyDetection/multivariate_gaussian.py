""" 
This class:
This class is optional
Automatically captures correlations between feautures
Computationally more expensive
Must have m > n or else sumall is non-invertible
Author: mserna

"""
import numpy
import pandas as pd
import math
from scipy.stats import norm
import matplotlib.pyplot as plt

class MultivariateGaussian(object):

    def __init__(self, x_data, mu, sigma2):
        x_data = pd.read_excel(x_data,names=['CPU', 'Memory', 'Disks'])
        x_data.values
        self.__x_data = x_data
        self.__mu = mu
        self.__sigma2 = sigma2

    def compute_density_func(self):
        k = len(self.__mu)
        prob_dens_func = 0
        X = self.__x_data

        if self.__sigma2.shape[0] == 1:
            self.__sigma2 = numpy.diag(self.__sigma2)
        self.__sigma2 = numpy.diag(self.__sigma2)

        X = numpy.array( X - numpy.transpose(self.__mu[:]) )

        # Calculate probablity density function
        # p = (2 * pi) ^ (- k / 2) * det(Sigma2) ^ (-0.5) * exp(-0.5 * sum(bsxfun(@times, X * pinv(Sigma2), X), 2));
        # prob_dens_func = 1 / ( (2*numpy.pi)**(k/2) * (numpy.linalg.det(self.__sigma2)**0.5) ) * numpy.exp(-0.5 * numpy.sum(X * numpy.linalg.pinv(self.__sigma2) * X,axis=1))
        prob_dens_func = norm.pdf(X)
        plt.plot(X,prob_dens_func)
        plt.show()

        print(self.__sigma2)

        return prob_dens_func