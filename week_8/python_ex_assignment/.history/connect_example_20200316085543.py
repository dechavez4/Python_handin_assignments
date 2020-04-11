import pymysql.cursors  
 
# Connect to the database.
connection = pymysql.connect(host='127.0.0.1',
                             user='dev',
                             password='ax2',                             
                             db='startcode',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")
 
try:
  
 
    with connection.cursor() as cursor:
       
        # SQL 
        sql = "SELECT ID, MOVIENAME FROM startcode "
         
        # Execute query.
        cursor.execute(sql)
         
        print ("cursor.description: ", cursor.description)
 
        print()
 
        for row in cursor:
            print(row)
             
finally:
    # Close connection.
    connection.close()