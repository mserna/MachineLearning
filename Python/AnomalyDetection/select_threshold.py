# This class:
# 1. 
# Author: mserna

class SelectThreshold(object):

    def __init__(self, p_val, y_val):
        self.__p_val = p_val
        self.__y_val = y_val
    
    def select_threshes(self):
        bestEpsilon = 0
        bestF1 = 0
        F1 = 0
        cvPredictions = 1
        stepsize = (max(self.__p_val) - min(self.__p_val)) / 1000
        print("StepSize: {}".format(stepsize))