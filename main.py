from src.frame.MainFrame import *
#from src.sqlTools.LibrarianTools import *
#from src.model.Reader import *
from src.model.Librarian import *
from src.sqlTools.ReaderTools import *
    
#main()

#login = LibrarianTools()
#print(login.LibrarianLogin("root","root"))

get_data = ReaderTools()
print(get_data.ReaderData())
