from src.frame.MainFrame import *
#from src.sqlTools.LibrarianTools import *
from src.model.Reader import *
from src.model.Librarian import *
from src.sqlTools.ReaderTools import *
    
main = MainFrame()

#login = LibrarianTools()
#print(login.LibrarianLogin("root","root"))

person1 = Reader()
person1.idReader = "011"
person1.nameReader = "baba"
person1.level = "教师"
person1.sex = "男"
person1.password = "root"

print(person1.toString())

#get_data = ReaderTools()

#print(get_data.DeleteReader(person1.idReader))
#print(get_data.ReaderData())
