import traceback
import mysql.connector
from ..database.database import *


class LibrarianTools:
    def LibrarianLogin(self, nameUser, password):
        db = DatabaseTools()
        conn = db.getConn()
        try:
            sql = "select nameUser,password from librarian where nameUser= %s and password= %s "
            answer = (str(nameUser),str(password))

            mycursor = conn.cursor()

            mycursor.execute(sql,answer)

            result = mycursor.fetchone()

            if(result != None):
                return True
            mycursor.close()
            conn.close()
        except Exception as e:
            traceback.print_exc()
        return False
