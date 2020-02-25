import numpy as np

#exercise 2 cube:
c = np.arange(0, 27).reshape((3, 3, 3)) # = (z, y, x)
slice1 = a[1, 1, :]

print('slice1 = ', slice1)