import numpy as np

Z = np.arange(20)
print(Z)
a = np.random.uniform(0, 20)

print('случайное число: ',a)
index = np.argmin(np.abs(Z-a))
print(Z[index])