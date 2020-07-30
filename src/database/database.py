import traceback
import mysql.connector

class DatabaseTools:
    def getConn(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost", # IP Address for your SQL server
                user="root",
                password="",
                database="library"  # your SQL server Database
            )
            return mydb
        except Exception as e:
            traceback.print_exc()
