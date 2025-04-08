from math import floor

import numpy as np


z = np.random.uniform(0, 10, 10)
print(z)

# базово округляем вниз через np
print(np.floor(z))
print(np.trunc(z))
# базово округляем вверх через np
print(np.ceil(z))
# делим нацело на 1
print(z // 1)
# вычитаем остаток от деления на 1
print(z - z%1)
# каст к инту
print(z.astype(int))