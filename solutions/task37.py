import numpy as np

a = np.arange(0, 5)
b = a.repeat(5).reshape((5, 5)).transpose()
print(b)

## решение из источника
z = np.zeros((5, 5))
z += np.arange(0, 5)
print(z)