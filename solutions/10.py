import numpy as np

input = np.array([1,2,0,0,4,0])
# классический вариант
res = []

for index, el in enumerate(input):
    if el != 0:
        res.append(index)

print(res)

# нормальный вариант

print(np.nonzero(input))