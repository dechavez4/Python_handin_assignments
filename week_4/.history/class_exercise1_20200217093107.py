
import numpy as np
a = np.arrange(10, 30).reshape(4,5)

yellow = a[0,0]

red    = a[0, 1:4]  
blue   = a[1:4, 0]  
green  = a[::2,::2] 
purple = a[:, 1]

print('yellow', yellow)

