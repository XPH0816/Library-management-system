import traceback
import mysql.connector
from ..model.Reader import Reader
from ..database.database import DatabaseTools

class ReaderTools:
    #return for Special ID
    def ReaderDataId(self, idReader):
        db = DatabaseTools()
        conn = db.getConn()
        result_set = None
        ls = []
        try :
            sql = "select idReader,nameReader,kind,sex,password from Reader where idReader = %s"
            answer = (str(idReader),)

            mycursor = conn.cursor()

            mycursor.execute(sql,answer)

            result_set = mycursor.fetchall()

            for row in result_set:
                reader = Reader()
                reader.setIdReader(row[0])
                reader.setNameReader(row[1])
                reader.setLevel(row[2])
                reader.setSex(row[3])
                reader.setPassword(row[4])
                ls.append(reader.list_return_reader())
            
            mycursor.close()
            conn.close()
        except Exception as e :
            traceback.print_exc()
        return ls
    
    #return for Special name
    def ReaderDataSearch(self, nameReader):
        db = DatabaseTools()
        conn = db.getConn()
        result_set = None
        ls = []
        try :
            sql = "select idReader,nameReader,kind,sex,password from Reader where nameReader like %s"
            answer = str("'%"+nameReader+"%'")

            mycursor = conn.cursor()

            mycursor.execute(sql%answer)

            result_set =(mycursor.fetchall())

            for row in result_set:
                reader = Reader()
                reader.setIdReader(row[0])
                reader.setNameReader(row[1])
                reader.setLevel(row[2])
                reader.setSex(row[3])
                reader.setPassword(row[4])
                ls.append(reader.list_return_reader())
            
            mycursor.close()
            conn.close()
        except Exception as e :
            traceback.print_exc()
        return ls

    def ReaderData(self):
        db = DatabaseTools()
        conn = db.getConn()
        result_set = None
        ls = []
        try:
            sql = "select idReader,nameReader,kind,sex,password from Reader"

            mycursor = conn.cursor()

            mycursor.execute(sql)

            result_set = mycursor.fetchall()

            for row in result_set:
                reader = Reader()
                reader.setIdReader(row[0])
                reader.setNameReader(row[1])
                reader.setLevel(row[2])
                reader.setSex(row[3])
                reader.setPassword(row[4])
                ls.append(reader.list_return_reader())

            mycursor.close()
            conn.close()
        except Exception as e:
            traceback.print_exc()
        return ls
                



