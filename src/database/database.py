import traceback
import mysql.connector

class DatabaseTools:
    conn = None
    def getConn(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="library"
            )
        except Exception as e:
            traceback.print_exc()