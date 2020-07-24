from src.frame.MainFrame import *
#from src.sqlTools.LibrarianTools import *
from src.model.Reader import *
from src.model.Librarian import *
from src.sqlTools.PublisherTools import *
    
#main = MainFrame()

#login = LibrarianTools()
#print(login.LibrarianLogin("root","root"))

#person1 = Reader()
#person1.idReader = "011"
#person1.nameReader = "baba"
#person1.level = "教师"
#person1.sex = "男"
#person1.password = "root"

#print(person1.equals("",person1.idReader))

get_data = PublisherTools()

print(get_data.PublisherData())
#print(get_data.ReaderData())
