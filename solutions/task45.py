import numpy as np

Z = np.random.randint(0, 10, 10)

print(Z, Z.argmax())

max = np.argmax(Z)
Z[max] = 0

print(Z)
