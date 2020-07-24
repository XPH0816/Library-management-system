import traceback
import mysql.connector
from ..model.Publisher import *
from ..database.database import DatabaseTools

class PublisherTools:
    def PublisherDataName(self, name):
        db = DatabaseTools()
        conn = db.getConn()
        result_set = None
        publisher = Publisher()
        try :
            sql = "select name,address from publisher where name = %s"
            answer = (str(name),)

            mycursor = conn.cursor()

            mycursor.execute(sql,answer)

            result_set = (mycursor.fetchall())

            for row in result_set:
                publisher.setName(row[0])
                publisher.setAddress(row[1])

            mycursor.close()
            conn.close()
        except Exception as e:
            traceback.print_exc()
        return publisher.list_return()

    def PublisherData(self):
        db = DatabaseTools()
        conn = db.getConn()
        result_set = None
        ls = []
        try:
            sql = "select name,address from publisher"

            mycursor = conn.cursor()

            mycursor.execute(sql)

            result_set = (mycursor.fetchall())

            for row in result_set:
                publisher = Publisher()
                publisher.setName(row[0])
                publisher.setAddress(row[1])
                ls.append(publisher.list_return())

            mycursor.close()
            conn.close()
        except Exception as e:
            traceback.print_exc()
        return ls

    def addPublisher(self, Publisher):
        i = 0
        db = DatabaseTools()
        conn = db.getConn()
        try :
            sql = "insert into publisher (name,address)values(%s,%s)"
            answer = (str(Publisher.name),str(Publisher.address))

            mycursor = conn.cursor()

            mycursor.execute(sql,answer)

            i = mycursor.rowcount

            mycursor.close()
            conn.commit()
            conn.close()
        except Exception as e:
            traceback.print_exc()
        return i

    def UpdatePublisher(self, Publisher):
        i = 0
        db = DatabaseTools()
        conn = db.getConn()
        try :
            sql = "update publisher set name=%s,address=%s where name=%s"
            answer = (str(Publisher.name),str(Publisher.address))

            mycursor = conn.cursor()

            mycursor.execute(sql,answer)

            i = mycursor.rowcount

            mycursor.close()
            conn.commit()
            conn.close()
        except Exception as e:
            traceback.print_exc()
        return i
