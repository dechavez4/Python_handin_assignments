import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from itertools import cycle

iris_data = pd.read_excel('iris_data.xlsx')
print(iris_data.head())

iris_data = pd.get_dummies(iris_data,columns=['Species'])
print(iris_data.head())
if(iris_data['Species_I. virginica'][1:]==1):
    iris_data.plot.scatter(x=0,y=1, c='r')
plt.show()