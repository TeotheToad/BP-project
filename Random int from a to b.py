class LCG:
    def __init__(self, seed, x=1, y=2, z=2**10):
        self.x = x
        self.y = y
        self.z = z
        self.state = seed

    def random_number(self):
        self.state = ((self.y + self.x * self.state) % self.z)
        return (self.state / int(self.z))

def random_number_a_to_b(a:int, b:int):
    value = abs(hash(str(a + b)))
    lcg = LCG(seed=value)
    return (lcg.random_number()*(b - a) + a)

print(int(random_number_a_to_b('a','b')))
