import pandas as pd
import pymysql
from sqlalchemy import create_engine

con_str = 'mysql+pymysql://dev:ax2@localhost:3307/test'
engine = create_engine(con_str)

df = pd.DataFrame ({
    'make' : ['2018'],
    'model' : ['audi a6'],
    'year' : ['2019'],
    'price' : ['123000']
})

df.to_sql('cars', con=engine, if_exists='append', index= False)
print(df.dtypes)

/*
cvs= """
make,model,year,price
vw,up,2018,123000
audi,a6,2011,85000
citroen,c3,2019,143000
"""
data = pd.read_clipboard(sep='')
data
*/