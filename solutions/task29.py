import numpy as np

Z = (np.arange(15)-7)/4
print('Исходный вектор Z:\n', Z)

# стандартный метод
print(np.around(Z))

# округление в большую сторону абсолютных значений Z с копированием знака (SIC!)
print(np.copysign(np.ceil(np.abs(Z)), Z))

# пошло функциональное программирование
print(np.where(Z > 0, np.ceil(Z), np.floor(Z)))