import numpy as np

N = 11 # пусть будет 10 точек

# инициализируем пустую сетку
X = np.zeros((N, N), [('x', float), ('y', float)])

X['x'], X['y'] = np.meshgrid(np.linspace(0, 1, num=N),np.linspace(0, 1, num=N))

print(X)
