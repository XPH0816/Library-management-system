from src.frame.MainFrame import *
from src.frame.Gif_ReaderFrame import *
#from src.sqlTools.LibrarianTools import *
from src.model.Book import *
from src.model.Librarian import *
from src.sqlTools.LibrarianTools import *
    
#main = MainFrame()

frame = Gif_ReaderFrame()
frame.Gif_ReaderFrame()

#login = LibrarianTools()
#print(login.LibrarianLogin("root","root"))

#person1 = Book()
#person1.idBook = "001"
#person1.nameBook = "周易"
#person1.price = 23
#person1.type_ = "文学"
#person1.author = "山彤"
#person1.publisher = "商务印书出版社"

#print(person1.equals("",person1.idReader))

#get_data = BookTools()

#print(get_data.UpdateBook(person1))
#print(get_data.BookData())
