import numpy as np

Z1 = np.random.randint(0,2, 10)
Z2 = np.random.randint(0,2, 10)

print(Z1, Z2)

print('equal 1', np.array_equal(Z1, Z2))
print('equal 2', np.array_equal(Z1, Z1))
print('allclose 1', np.allclose(Z1, Z2))
print('allclose 2', np.allclose(Z1, Z1))