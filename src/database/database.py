import mysql.connector

def getConn():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
