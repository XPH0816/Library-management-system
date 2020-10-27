import traceback
import mysql.connector
from ..model.Author import *
from ..database.database import DatabaseTools

class AuthorTools:
    def AuthorDataName(self, name):
        db = DatabaseTools()
        conn = db.getConn()
        result_set = None
        ls = []
        try:
            sql = "select name,workplace from author where name= %s"
            answer = (str(name),)

            mycursor = conn.cursor()

            mycursor.execute(sql,answer)

            result_set = mycursor.fetchall()

            for row in result_set :
                author = Author()
                author.setName(row[0])
                author.setWorkplace(row[1])
                ls.append(author.list_return())

            mycursor.close()
            conn.close()
        except Exception as e:
            traceback.print_exc()
        return ls
    
    def AuthorData(self):
        db = DatabaseTools()
        conn = db.getConn()
        result_set = None
        ls = []
        try :
            sql = "select name,workplace from author"

            mycursor = conn.cursor()

            mycursor.execute(sql)

            result_set = mycursor.fetchall()

            for row in result_set:
                author = Author()
                author.setName(row[0])
                author.setWorkplace(row[1])
                ls.append(author.list_return())

            mycursor.close()
            conn.close()
        except Exception as e:
            traceback.print_exc()
        return ls

    def addAuthor(self, Author):
        i = 0
        db = DatabaseTools()
        conn = db.getConn()
        try : 
            sql = "insert into author (name,workplace)values(%s,%s)"
            answer = (str(Author.name),str(Author.workplace))

            mycursor = conn.cursor()

            mycursor.execute(sql,answer)

            i = mycursor.rowcount

            mycursor.close()

            conn.commit()
            conn.close()
        except Exception as e:
            traceback.print_exc()
        return i

    def UpdateAuthor(self, Author):
        i = 0
        db = DatabaseTools()
        conn = db.getConn()
        try :
            sql = "update author set name=%s ,workplace=%s where name=%s"
            answer = (str(Author.name),str(Author.workplace),str(Author.name))

            mycursor = conn.cursor()

            mycursor.execute(sql,answer)

            i = mycursor.rowcount

            mycursor.close()
            conn.commit()
            conn.close()
        except Exception as e:
            traceback.print_exc()
        return i

    

