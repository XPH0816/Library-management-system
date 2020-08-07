import traceback
import mysql.connector
from ..database.database import *
from ..model.Book import *

class BorrowTools:
    def BookData(self, idReader):
        db = DatabaseTools()
        conn = db.getConn()
        result_set = None
        ls = []
        try :
            sql = "select book.idBook,nameBook,price,book.kind,author,publisher from reader,borrow,book where book.idBook = borrow.idBook and reader.idReader = borrow.idReader and reader.idReader = %s "
            answer = (str(idReader),)

            mycursor = conn.cursor()

            mycursor.execute(sql,answer)

            result_set = mycursor.fetchall()

            for row in result_set:
                book = Book()
                book.setIdBook(row[0])
                book.setNameBook(row[1])
                book.setPrice(row[2])
                book.setType(row[3])
                book.setAuthor(row[4])
                book.setPublisher(row[5])
                ls.append(book.list_return())

            mycursor.close()
            conn.close()
        except Exception as e:
            traceback.print_exc()
        return ls

    def BookData_Search_idBook(self, idBook):
        db = DatabaseTools()
        conn = db.getConn()
        result_set = None
        ls = []
        try :
            sql = "select book.idBook,nameBook,price,book.kind,author,publisher from book where book.idBook = %s"
            answer = (str(idBook),)

            mycursor = conn.cursor()

            mycursor.execute(sql,answer)

            result_set = mycursor.fetchall()

            for row in result_set:
                book = Book()
                book.setIdBook(row[0])
                book.setNameBook(row[1])
                book.setPrice(row[2])
                book.setType(row[3])
                book.setAuthor(row[4])
                book.setPublisher(row[5])
                ls.append(book.list_return())

            mycursor.close()
            conn.close()
        except Exception as e:
            traceback.print_exc()
        return ls

    def whetherInStock(self, idBook):
        db = DatabaseTools()
        conn = db.getConn()
        try :
            sql = "select * from borrow"

            mycursor = conn.cursor()

            mycursor.execute(sql)

            result_set = mycursor.fetchall()

            for row in result_set :
                if row[1] != None :
                    if row[1] == idBook :
                        return False

            mycursor.close()
            conn.close()
        except Exception as e:
            traceback.print_exc()
        return True

    def BorrowBook(self, idReader, idBook):
        i = 0
        db = DatabaseTools()
        conn = db.getConn()
        try :
            sql = "insert into borrow (idReader,idbook,lendDate,dueDate,overtime) values (%s,%s,CURRENT_DATE(),DATE_ADD(CURRENT_DATE(),INTERVAL 2 MONTH),'否')"
            answer = (str(idReader),str(idBook))

            mycursor = conn.cursor()

            mycursor.execute(sql,answer)

            i = mycursor.rowcount

            mycursor.close()
            conn.commit()
            conn.close()
        except Exception as e:
            traceback.print_exc()
        return i

    def ReturnBook(self, idBook):
        i = 0
        db = DatabaseTools()
        conn = db.getConn()
        try :
            sql = "delete from Borrow where idBook= %s"
            answer = (str(idBook),)

            mycursor = conn.cursor()

            mycursor.execute(sql,answer)

            i = mycursor.rowcount

            mycursor.close()
            conn.commit()
            conn.close()
        except Exception as e:
            traceback.print_exc()
        return i
        



