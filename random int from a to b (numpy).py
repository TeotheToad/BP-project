import numpy as np

a , b = map(int, input().split())
random_number = int(np.random.uniform(a , b))

print("random_number:", random_number)