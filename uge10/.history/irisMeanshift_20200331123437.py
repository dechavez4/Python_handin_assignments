import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from itertools import cycle

iris_data = pd.read_excel('iris_data.xlsx')
print(iris_data.head())

iris_data = pd.get_dummies(iris_data,columns=['Species'])
print(iris_data.head())

colors = cycle('bgrcmy')
for data, idx in iris_data:
    if(data['Species_I. virginica']=1)
    iris_data[idx].plot.scatter(x = 0, y=1, colors["red"])


plt.show()