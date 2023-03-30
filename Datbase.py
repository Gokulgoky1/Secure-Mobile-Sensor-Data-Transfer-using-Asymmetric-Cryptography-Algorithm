# import mysql.connector
# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="Gokul@123",
#     auth_plugin='mysql_native_password')
# my_cursor=mydb.cursor(buffered=True)
# my_cursor.execute("CREATE DATABASE sensor_data")
# my_cursor.execute("SHOW DATABASES")
# my_cursor.execute("CREATE TABLE client_signup(username Varchar(20),email varchar(40) PRIMARY KEY,password varchar(25))")
# for db in my_cursor:
#     print(db)