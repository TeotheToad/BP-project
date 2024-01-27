import numpy as np
import math

n = int(input())


p = math.pi
e = math.e
def normal_distributionـfunction(x):
    y =((2*p)**(-1/2))*(e**((-1/2)*(x**2)))
    return y


def normal(n):
    y = []
    i = n
    while i > 0 :
        x = np.random.rand()
        y.append(normal_distributionـfunction(x))
        i = i - 1

    sum = 0
    j = 0
    while j < len(y):
        sum += y[j]
        j = j + 1
    m = sum/n
    
    s = 0
    k = 0
    while k < len(y):
        s = s + ((((y[k]-m)**2)/n)**1/2)
        k = k + 1
    
    return m, s, y

print(normal(n))