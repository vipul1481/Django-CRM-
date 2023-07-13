import mysql.connector

database =mysql.connector.connect(
    host ='localhost',
    user='root',
    passwd='vipulgoyal@1481'


)

#prepare a cursor oobject
cursorObject = database.cursor();

#Create database
cursorObject.execute("CREATE DATABASE projectdb ")
print("All DONE!")