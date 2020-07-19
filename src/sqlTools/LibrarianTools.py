import traceback
import mysql.connector
from ..database import database


class LibrarianTools:
    def LibrarianLogin(self, nameUser, password):
        db = DatabaseTools()
        conn = db.getConn()
        try:
            sql = "select nameUser,password from librarian where nameUser= + %s +  and password= + %s "
            answer = (nameUser,password)
            mycursor = conn.cursor()

            result = mycursor.execute(sql,answer)
            if(result.fetchone()):
                return True
            mycursor.close()
        except Exception as e:
            traceback.print_exc()
        return False
