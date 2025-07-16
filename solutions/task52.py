import numpy as np

N = 5 # кол-во точек
Points = np.zeros((N, 2), dtype='int32')
Points[:,0] = np.random.randint(low=0, high=10, size=N)
Points[:,1] = np.random.randint(low=0, high=10, size=N)
print(f'Вектор Points {Points}')

x, y = np.atleast_2d(Points[:,0], Points[:,1])
D = np.sqrt( (x-x.T)**2 + (y-y.T)**2)
print(f'Матрица расстояний между всеми точками Points: {D}')