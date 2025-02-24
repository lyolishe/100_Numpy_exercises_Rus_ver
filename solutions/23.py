# нихуя не ясно что такое dtype

import numpy as np

color = np.dtype([('red', np.uint8),
                  ('green', np.uint8),
                  ('blue', np.uint8),
                  ('alpha', np.uint8)])

point = np.array([(0, 0, 0, 0), (255, 255, 228, 50)],dtype=color)
print(point)
print(point[1], point['blue'])