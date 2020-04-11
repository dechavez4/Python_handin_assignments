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

df.to_sql('cars', con=engine, if_exists='append', index= false)
print(df.dtypes)
