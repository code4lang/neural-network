import numpy as np
from math import exp
v=[1.3,5.1,2.2,0.7,1.1]
def sigmoid(X):
    z=1/1+np.exp(-X)
    return z
def deriv_sigmoid(X):
    z=np.exp(-X)/2*np.exp(-X)+np.exp(-2*X)+1
    return z