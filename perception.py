#-----------------------------------

#
#   In this exercise you will put the finishing touches on a perceptron class
#
#   Finish writing the activate() method by using numpy.dot and adding in the thresholded
#   activation function

import numpy as np

class Perceptron:
    def activate(self,inputs):
        '''Takes in @param inputs, a list of numbers.
        @return the output of a threshold perceptron with
        given weights, threshold, and inputs.
        '''        
        y = np.dot(self.weights, inputs)
        if y >= self.threshold:
            result = 1
        else:
            result = 0
        return result

           
    def __init__(self,weights=None,threshold=None):
        if weights is not None:
            self.weights = weights
        if threshold is not None:
            self.threshold = threshold
            
            