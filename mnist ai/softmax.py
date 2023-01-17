
import numpy as np
from math import exp
v=[1.3,5.1,2.2,0.7,1.1]
def softmax(X):
    z=np.exp(X)/sum(np.exp(X))
    return z
def deriv_softmax(X):
    z=np.exp(X)/sum(np.exp(X))
    return z
print(softmax(v))