import numpy as np

V = np.genfromtxt('./file54.txt', filling_values=0, delimiter=',', comments='#', dtype=np.int32)
print(V)