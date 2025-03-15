import numpy as np

deck = np.zeros([8,8])


deck[::2, ::2] = 1
deck[1::2, 1::2] = 1

print(deck)