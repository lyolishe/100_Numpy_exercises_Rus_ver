import numpy as np

z = np.arange(15)

z.setflags(write=False)

try:
    z[0] = 1
except Exception:
    print("task failed successfully")