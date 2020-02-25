import numpy as np

a = np.arange(10,30).reshape(4,5)

yellow = a[0,0]
green = a[:3, 2]
teal = a[:1, ::2] 
blue = a[::2, 4] 

purple = a[:, 1]

print('yellow= ', yellow, 'green= ', green, 'blue= ', blue, 'teal=', teal)

