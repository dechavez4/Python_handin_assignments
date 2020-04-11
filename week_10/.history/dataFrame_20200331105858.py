import pandas as pd
import numpy as np

p = np.array ({
['Paula':{'Is':4,'Juice':2,'Kakao':3,'Lagkager':2}],
['Peter':{'Is':2,'Juice':5,'Kakao':0, 'Lagkager':4}],
['Pandora':{'Is':5,'Juice':3, 'Kakao':4, 'Lagkager':5}],
['Pietro':{'Is':1,'Juice':8, 'Kakao':9, 'Lagkager':1}]
})

q = np.array ({
    ['Netto': {'Is':10.50,'Juice':2.25,'Kakao':4.50,'Lagkager':33.50}],
    ['Fakta': {'Is':4.00,'Juice':4.50,'Kakao':6.25,'Lagkager':20.00}]
})

price = p.dot(q)
print(price)
