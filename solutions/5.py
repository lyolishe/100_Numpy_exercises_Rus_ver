import numpy as np

print(np.info(np.add))

vec1 = np.zeros(10)
vec2 = np.zeros((10, 1))
vec1.fill(5)
vec2.fill(2)
sum = np.add(vec1, vec2)
print('vec1: \n', vec1)
print('vec2: \n', vec2)
print('sum: \n', sum, sum.shape)