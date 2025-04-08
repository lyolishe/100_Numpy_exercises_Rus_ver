import numpy as np

# делаем 11 чисел от 0 до 1, не включая конец. отрубаем первое число
z = np.linspace(0, 1, endpoint=False, num=11)[1:]
print(z)