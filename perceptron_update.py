#-----------------------------------

#
#   In this exercise we write a perceptron class
#   which can update its weights
#
#   Your job is to finish the train method so that it implements the perceptron update rule

import numpy as np

class Perceptron:
    
    def activate(self,values):
        '''Takes in @param values, @param weights lists of numbers
        and @param threshold a single number.
        @return the output of a threshold perceptron with
        given weights and threshold, given values as inputs.
        ''' 
               
        #First calculate the strength with which the perceptron fires
        strength = np.dot(values,self.weights)
        
        if strength>self.threshold:
            result = 1
        else:
            result = 0
            
        return result

    def update(self,values,train,eta=.1):
        '''Takes in a 2D array @param values consisting of a LIST of inputs
        and a 1D array @param train, consisting of a corresponding list of 
        expected outputs.
        Updates internal weights according to the perceptron training rule
        using these values and an optional learning rate, @param eta.
        '''
        #YOUR CODE HERE
        #update self.weights based on the training data
        
        
    def __init__(self,weights=None,threshold=None):
        if weights is not None:
            self.weights = weights
        if threshold is not None:
            self.threshold = threshold