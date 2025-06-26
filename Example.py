import mysql.connector
conn=mysql.connector.connect(host='localhost', password='Admin', user='root')

if conn.is_connected():
    print("Connection established...")
