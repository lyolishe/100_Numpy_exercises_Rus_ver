import numpy as np

for dtype in [np.int8, np.int32, np.int64]:
   print(f'Тип: {dtype.__name__}, минимум: {np.iinfo(dtype).min}, максимум: {np.iinfo(dtype).max}')
for dtype in [np.float32, np.float64]:
   print(f'Тип: {dtype.__name__}, минимум: {np.finfo(dtype).min}, максимум: {np.finfo(dtype).max}, и дельта: {np.finfo(dtype).eps}')