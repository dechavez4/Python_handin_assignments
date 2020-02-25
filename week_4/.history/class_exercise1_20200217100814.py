import numpy as np

a = np.arange(10,30).reshape(4,5)
#exercise 1 table
yellow = a[0,0]
green = a[:3, 2]
teal = a[:, (1,3)] 
blue = a[::2, 4] 
red = a[0, 1:4]

#print('yellow= ', yellow, 'green= ', green, 'blue= ', blue, 'teal=', teal, 'red=', red)


#exercise 2 cube:
c = np.arange(0, 27).reshape((3, 3, 3)) # = (z, y, x)
slice1 = c[1, 1, :]
slice2 = c[:, 1 , 0 ]
slice3 = c[0, :, 1]

print('slice1 = ', slice1, 'slice2 = ', slice2, 'slice3 = ', slice3)