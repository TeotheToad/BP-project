import numpy as np

a , b = map(int, input().split())
random_number = np.random.uniform(a , b)

print("random_number:", random_number)