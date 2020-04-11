import pandas as pd 
import pymysql

cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test') 

helga_dict = {'firstname': 'helga', 'lastname':'Julhborg', 'startdate': '2003-01-07', 'enddate': '204-04-11', 'salery': '11400'}
def persist_data(connector, dictionary, table_name):
    columns = ', '.join(dictionary.key())
    vals = tuple(dictionary.values())
    insert_str = 'INSERT into {table} ({cals}) values{vals}'.format(table=table_name, cols=columns, vals=vals)
    cursor = connector.cursor()
    cursor.execute(insert_str)
    id = cursor.lastrowid
    connector.commit()
    cursor.close()
    return id

persist_data(cnx, helga_dict, 'pythondemo')