import numpy as np

a = np.arange(10,30).reshape(4,5)

yellow = a[0,0]
green = a[:3, 2]
teal = a[:, (1,3)] 
blue = a[::2, 4] 
red = a[0:, (1,3)]

print('yellow= ', yellow, 'green= ', green, 'blue= ', blue, 'teal=', teal, 'red=', red)

