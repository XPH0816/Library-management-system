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
                ls.append(reader.list_return())
            
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
                ls.append(reader.list_return())
            
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
                ls.append(reader.list_return())

            mycursor.close()
            conn.close()
        except Exception as e:
            traceback.print_exc()
        return ls

    def ReaderLogin(self, idReader , password):
        db = DatabaseTools()
        conn = db.getConn()
        try:
            sql = "select idReader,password from reader where idReader= %s and password= %s "
            answer = (str(idReader),str(password))

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

    def addReader(self, Reader):
        i = 0
        db = DatabaseTools()
        conn = db.getConn()
        try :
            sql = "insert into reader (idReader,nameReader,kind,sex,password) values (%s,%s,%s,%s,%s)"
            answer = (str(Reader.idReader),str(Reader.nameReader),str(Reader.level),str(Reader.sex),str(Reader.password))

            mycursor = conn.cursor()

            mycursor.execute(sql,answer)

            i = mycursor.rowcount            

            mycursor.close()
            conn.commit()
            conn.close()
        except Exception as e :
            traceback.print_exc()
        return i

    def UpdateReader(self, Reader):
        i = 0
        db = DatabaseTools()
        conn = db.getConn()
        try :
            sql = "update reader set idReader=%s,nameReader=%s,kind=%s,sex=%s,password=%s where idReader=%s"
            answer = (str(Reader.idReader),str(Reader.nameReader),str(Reader.level),str(Reader.sex),str(Reader.password),str(Reader.idReader))

            mycursor = conn.cursor()

            mycursor.execute(sql,answer)

            i = mycursor.rowcount

            mycursor.close()
            conn.commit()
            conn.close()
        except Exception as e :
            traceback.print_exc()
        return i
    
    def DeleteReader(self, idreader):
        i = 0
        db = DatabaseTools()
        conn = db.getConn()
        try :
            sql = "delete from reader where idReader = %s"
            answer = (str(idreader),)

            mycursor = conn.cursor()

            mycursor.execute(sql,answer)

            i = mycursor.rowcount

            mycursor.close()
            conn.commit()
            conn.close()
        except Exception as e :
            traceback.print_exc()
        return i








