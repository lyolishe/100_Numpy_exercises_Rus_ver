import numpy as np

V = (np.random.rand(10)*100).astype(np.float32)
print(V)
y = V.view(np.int32)
y[:] = V
print(y)