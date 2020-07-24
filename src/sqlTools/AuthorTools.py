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
            answer(str(name),)

            mycursor = conn.cursor()

            mycursor.execute(sql,answer)

            result_set = mycursor.fetchall()

            for row in result_set :
                author = Author()

