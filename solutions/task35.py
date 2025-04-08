import numpy as np

# вычисляем (А+B)*(-A/2)
A = np.ones(3)*1
B = np.ones(3)*2
print(A, B)

np.add(A, B, out=B)
np.multiply(A, -1/2, out=A)
np.multiply(B, A, out=B)
print(B)
