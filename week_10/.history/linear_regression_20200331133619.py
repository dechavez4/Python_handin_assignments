import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model



data = pd.read_csv("car_sales.csv")
data.plot.scatter(x = 1, y= 2)
plt.show()
