import numpy as np

scalar_type = np.dtype('float64')

array_type = np.dtype([
    ('position', [
        ('x', scalar_type),
        ('y', scalar_type)
    ]),
    ('color', [
        ('r', scalar_type),
        ('g', scalar_type),
        ('b', scalar_type)
    ])
])
Z = np.zeros(2,  array_type)
print('Исходный трехмерный нулевой массив заданного типа: \n', Z)

Z[0] = ((10., 100.), (255., 255., 255.))
print('Массив с инициализированной точкой в Z[0]:\n', Z)

# изменяем координату нулевой точки по х на 20 и яркость зеленого цвета на ноль
Z['position']['x'][0]=20
Z['color']['g'][0]=0
print('Массив в котором изменили значение координаты x и яркость зеленого цвета в точке Z[0]:\n', Z)
print(Z['color'])