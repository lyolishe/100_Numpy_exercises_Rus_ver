import numpy as np

vec = np.ones([9, 6])

# запятая разделяется по шейпу. vec имеет форму 9х6, соответственно
# сперва слайс по строкам,  а потом - по столбцам
vec[1:-1, 1:-1] = 0

print(vec)