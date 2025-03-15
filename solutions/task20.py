import numpy as np

N = 100  # номер индекса (предполагаем, что счет элемментов начинается с 1 (единицы))
print(np.unravel_index(indices=N-1,shape=(6,7,8)))