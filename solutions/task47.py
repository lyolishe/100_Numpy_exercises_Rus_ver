import numpy as np

X = np.random.randint(0, 10, 4)
Y = X + 0.5

C = 1/(np.subtract.outer(X, Y))

print(X, Y, C)
print( np.linalg.det(C))