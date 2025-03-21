import numpy as np

Z1 = np.random.randint(0, 10, 10)
Z2 = np.random.randint(0, 10, 10)

intersect = np.intersect1d(Z1, Z2)
print(f'Z1: {Z1}, Z2: {Z2}, \nintersect: {intersect}')