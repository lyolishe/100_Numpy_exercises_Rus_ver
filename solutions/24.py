import numpy as np

A = np.ones([2,3])
B = np.ones([3, 5])

z = np.dot(A, B)
Z = A@B

print(z, Z)