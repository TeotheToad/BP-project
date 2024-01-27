import math
n = int(input())

class LCG:
    def __init__(self, seed, x=16467, y=201467, z=2**10):
        self.x = x
        self.y = y
        self.z = z
        self.state = seed

    def random_number(self):
        self.state = (self.x * self.state + self.y) % self.z
        return self.state / float(self.z)

value = abs(hash(str('random number')))
lcg = LCG(seed=value)

p = math.pi
e = math.e
def normal_distributionـfunction(x):
    y =((2*p)**(-1/2))*(e**((-1/2)*(x**2)))
    return y


def normal(n):
    y = []
    i = n
    while i > 0 :
        value = abs(hash(str(i)))
        random_number = LCG(seed=value)
        x = random_number.random_number()
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