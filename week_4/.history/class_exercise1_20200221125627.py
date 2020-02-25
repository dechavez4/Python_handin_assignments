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
filename = 'befkbhalderstatkode.csv'
bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
dd = bef_stats_df
mask_year_2015 = dd[:, 0] == 2015
mask_german = dd[:,3] == 5180
german_children_mask = (mask_year_2015 & mask_german & (dd[:, 2] <= 0))

german_children = np.sum(dd[(german_children_mask)][:, 4])

#print(german_children)

def showNum(aar=dd[:,0], bydel=dd[:,1], alder=dd[:,2], statkode=dd[:,3]):
    parts = (dd[:,0] == aar) & (dd[:,3] == statkode) & (dd[:,2] <= alder) & (dd[:,1] == bydel) 
#    partsData = dd[parts]
    partsSum = np.sum(dd[parts][:,4])
    print(partsSum)
showNum(aar=2015, alder=2, statkode=5180)

#exercise 5 boolean:
def getPeopleOverSixtyFive():
    mask = (dd[:,0] == 2015) && (dd[:,4] <= 65)
    getOldPeople = np.sum(dd[mask][:,4]) 