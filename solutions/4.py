import numpy as np

vec = np.zeros((10, 10))

print('vec: \n', vec);
print('vec`s size: ',
  vec.size,
  '\nsize of every item is %d byte' % vec.itemsize,
  '\ntotal size in memory %d byte.' % (vec.size*vec.itemsize)
)