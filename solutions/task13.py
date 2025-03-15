import numpy as np

vec = np.random.randint(low=-100, high=100, size=[10, 10])

print(vec)

min = np.min(vec)
max = np.max(vec)

print([vec.min(), vec.max()], [min, max])