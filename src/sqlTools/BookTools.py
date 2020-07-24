import traceback
import mysql.connector
from ..model.Book import *
from ..database.database import DatabaseTools

class BookTools:
    def BookData(self):
        db = DatabaseTools()
        conn = db.getConn()
        result_set = None
        ls = []
        try :
            sql = "select idBook,nameBook,price,kind,author,publisher from Book"
            
            mycursor = conn.cursor()

            mycursor.execute(sql)

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

    def BookDataName(self, nameBook):
        db = DatabaseTools()
        conn = db.getConn()
        result_set = None
        ls = []
        try:
            sql = "select idBook,nameBook,price,kind,author,publisher from Book where nameBook like %s"
            answer= ("%"+str(nameBook)+"%",)

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

    def Search_Book(self, idBook):
        db = DatabaseTools()
        conn = db.getConn()
        result_set = None
        book = None
        try:
            sql = "select idBook,nameBook,price,kind,author,publisher from Book where idBook= %s "
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

            mycursor.close()
            conn.close()
        except Exception as e:
            traceback.print_exc()
        return book.list_return()

    def AddBook(self, Book):
        i = 0
        db = DatabaseTools()
        conn = db.getConn()
        try :
            sql = "insert into book (idBook,nameBook,price,kind,author,publisher)values(%s,%s,%s,%s,%s,%s)"
            answer = (str(Book.idBook), str(Book.nameBook), str(Book.price), str(Book.type_), str(Book.author), str(Book.publisher))

            mycursor = conn.cursor()

            mycursor.execute(sql,answer)

            i = mycursor.rowcount

            mycursor.close()
            conn.commit()
            conn.close()
        except Exception as e:
            traceback.print_exc()
        return i

