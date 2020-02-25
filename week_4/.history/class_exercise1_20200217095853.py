import numpy as np
%load_ext autoreload
%autoreload 2
# %aimport solutions.numpy_ex
from solutions import numpy_ex as nump
nump.cube_ex()

a = np.arange(10,30).reshape(4,5)
#exercise 1 table
yellow = a[0,0]
green = a[:3, 2]
teal = a[:, (1,3)] 
blue = a[::2, 4] 
red = a[0, 1:4]

print('yellow= ', yellow, 'green= ', green, 'blue= ', blue, 'teal=', teal, 'red=', red)


#exercise 2 cube:


