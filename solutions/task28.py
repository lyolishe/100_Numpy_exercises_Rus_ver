import numpy as np

np.array(0) / np.array(0) # ошибка invalid value encountered in divide - деление на 0
np.array(0) // np.array(0) # ошибка divide by zero encountered in floor_divide - деление на 0
np.array([np.nan]).astype(int).astype(float) # ошибка invalid value encountered in cast - не может конвертнуть нан в инт