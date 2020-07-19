from src.frame.MainFrame import *
from src.sqlTools.LibrarianTools import *
    
main()

login = LibrarianTools()
print(login.LibrarianLogin("root","root"))
