from math import exp
v=[1.3,5.1,2.2,0.7,1.1]
def softmax(v):
    z=[]
    s=0
    for i in v:
        zi=exp(i)
        z.append(zi)
        s+=zi
    z=[a/s for a in z]
    return z
print(softmax(v))