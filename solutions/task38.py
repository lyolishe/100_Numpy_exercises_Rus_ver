import numpy as np

def generate():
    for x in range(10):
        # аналогично js - паузит функцию, возвращая значение под yield
        yield x

Z = np.fromiter(generate(), dtype=float)
print(Z)