import pandas as pd
import numpy as np
def logistic_regression(data, labels, weights, num_epochs, learning_rate): # do not change the heading of the function
    x = np.insert(data,0,values=1,axis = 1)
    y = labels.reshape(len(labels),1)
    counter = 0
    while(counter < num_epochs):
        p = 1/(1+np.exp(-(np.dot(x,weights.reshape(len(weights),1)))))
        error =  p - y
        weights = weights - learning_rate * np.multiply(error,x).sum(axis=0)
        counter+=1
    return weights
