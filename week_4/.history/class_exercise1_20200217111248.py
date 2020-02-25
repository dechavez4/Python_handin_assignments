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
slice3 = c[0, :, 2]

#print('slice1 = ', slice1, 'slice2 = ', slice2, 'slice3 = ', slice3)


#exercise 3 masking:
data = np.arange(1,101).reshape(10,10)
even = data[data % 2 == 0]
sixOnly = np.where(data % 10 == 6)
six = data[sixOnly]

#print('even =', even, 'sixOnly', six)

#exercise 4 numpy and csv:
filename = './python_thomas_kode/befkbdalderstatkode'
bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
print(type(bef_stats_df))