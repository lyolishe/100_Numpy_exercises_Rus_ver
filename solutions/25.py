import numpy as np

vec = np.arange(11)

vec[(vec > 3) & (vec < 8)] *= -1

print(vec)