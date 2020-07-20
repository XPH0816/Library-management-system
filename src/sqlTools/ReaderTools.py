import traceback
import mysql.connector
from ..model.Reader import Reader
from ..database.database import DatabaseTools

class ReaderTools:
    def ReaderData(self,idReader):
        sql = "select idReader,nameReader,kind,sex,password from Reader where idReader = %s"
        answer = str(idReader)
        db = DatabaseTools()
        conn = db.getConn()
        result_set = None
        ls = []
        try :
            mycursor = conn.cursor()

            mycursor.execute(sql,answer)

            result_set = (mycursor.fetchall())

            for row in result_set:
                reader = Reader()
                reader.setIdReader(row[0])
                reader.setNameReader(row[1])
                reader.setLevel(row[2])
                reader.setSex(row[3])
                reader.setPassword(row[4])
                ls.append(reader)
            
            mycursor.close()
            conn.close()
        except Exception as e :
            traceback.print_exc()
        return ls


