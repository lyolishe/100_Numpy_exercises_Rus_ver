import numpy as np

vec = np.zeros([5,5])

vec = np.pad(vec, pad_width=2, mode='constant', constant_values=1)
print(
    vec
)

