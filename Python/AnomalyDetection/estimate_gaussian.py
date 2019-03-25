# This class:
# 1. Estimates the parameters of the gaussian distribution given x_data
# 2. Estimates multivariate gaussian distribution (if necessary)
# Author: mserna

import numpy
import pandas as pd
import matplotlib.pyplot as plt

class EstimateGuassian(object):

    def __init__(self, x_data):
        x_data = pd.read_excel(x_data,names=['CPU', 'Memory', 'Disks'])
        # Stores excel data as matrix
        x_data.values

        self.__x_data = x_data
    
    def estimate(self):
        [m, n] = self.__x_data.shape
        #pd.DataFrame.plot(self.__x_data[:,1],self.__x_data[:,2], kind='scatter')

        # Create array of nx1 data
        mu = numpy.zeros((n, 1), float)
        sigma2 = numpy.zeros((n, 1), float)

        mu = self.__x_data.mean() # Compute mean
        sigma2 = self.__x_data.var() # Compute variance
        print("mu: \n{}".format(mu))
        print('\n')
        print("Sigma2: \n{}".format(sigma2))

        return [mu, sigma2]

    def plot_data(self):
        cpu_metrics = self.__x_data['CPU']
        mem_metrics = self.__x_data['Memory']
        plt.scatter(cpu_metrics[:], mem_metrics[:])
        plt.show()
