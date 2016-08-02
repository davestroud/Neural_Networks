#
#   In this exercise, you will create a network of perceptrons which
#   represent the xor function use the same network structure you used
#   in the previous quizzes.
#
#   You will need to do two things:
#   First, create a network of perceptrons with the correct weights
#   Second, define a procedure EvalNet() which takes in a list of 
#   inputs and ouputs the value of this network.

import numpy as np

class Perceptron:

    def evaluate(self,values):
        '''Takes in @param values, @param weights lists of numbers
        and @param threshold a single number.
        @return the output of a threshold perceptron with
        given weights and threshold, given values as inputs.
        ''' 
               
        #First calculate the strength with which the perceptron fires
        strength = np.dot(values[i],self.weights[i])
        
        #Then evaluate the return value of the perceptron
        if strength >= self.threshold:
            result = 1
        else:
            result = 0

        return result

    def __init__(self,weights=None,threshold=None):
        if weights is not None:
            self.weights = weights
        if threshold is not None:
            self.threshold = threshold
            

Network = [
    #input layer, declare perceptrons here
    [ ... ], \
    #output node, declare one perceptron here
    [ ... ]
]


def EvalNetwork(inputValues, Network):
    
    
    # Be sure your output values are single numbers
    return OutputValues