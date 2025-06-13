import numpy as np

Z = np.random.randint(-1, 2, 20).reshape(10, 2).astype(np.float64)

X = Z[:,0]
Y = Z[:,1]

print("исходный", Z)

R = np.sqrt(X**2+ Y**2)
T = np.arctan2(X, Y)

Z[:,0] = R
Z[:,1] = T

print("конечный", Z)