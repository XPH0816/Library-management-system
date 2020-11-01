from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from ttkthemes import ThemedTk

from ..model.Author import *
from ..model.Book import *
from ..model.Publisher import *

from ..sqlTools.AuthorTools import *
from ..sqlTools.BookTools import *
from ..sqlTools.PublisherTools import *

class UpdateBook_Frame :

    def do_updateBook(self):

        bookTools = BookTools()
        book = Book()

        author = Author()
        authorTools = AuthorTools()

        publisher = Publisher()
        publisherTools = PublisherTools()

        if (self.idBookEntry['text'] != None and self.idBookEntry['text'] != "" 
            and self.nameBookEntry.get() != None and self.nameBookEntry.get() != "" 
            and self.priceEntry.get() != None and self.priceEntry.get() != "" 
            and self.typeEntry.get() != None and self.typeEntry.get() != ""
            and self.authorEntry.get() != None and self.authorEntry.get() != ""
            and self.publisherEntry.get() != None and self.publisherEntry.get() != ""
            and self.workplaceEntry.get() != None and self.workplaceEntry.get() != ""
            and self.addressEntry.get() != None and self.addressEntry.get() != "" ):

            book.setIdBook(self.idBookEntry['text'])
            book.setNameBook(self.nameBookEntry.get())
            book.setPrice(self.priceEntry.get())
            book.setType(self.typeEntry.get())
            book.setAuthor(self.authorEntry.get())
            book.setPublisher(self.publisherEntry.get())

            author.setName(self.authorEntry.get())
            author.setWorkplace(self.workplaceEntry.get())

            publisher.setName(self.publisherEntry.get())
            publisher.setAddress(self.addressEntry.get())

            publisherTools.UpdatePublisher(publisher)
            publisherTools.addPublisher(publisher)
            
            authorTools.UpdateAuthor(author)
            authorTools.addAuthor(author)

            i = bookTools.UpdateBook(book)
            if i == 1 :
                messagebox.showinfo("Sucessfully Update", "Sucessfully Update The Book Infomation")
                MsgBox = messagebox.askquestion('Continue','Are you sure you want to Continue',icon = 'info')
                if MsgBox == 'yes' :
                    self.root.destroy()
                return
            else :
                messagebox.showinfo("Failed to Update", "Failed to Update The Book Infomation")
                MsgBox = messagebox.askquestion('Continue', 'Are you sure you want to Continue', icon='info')
                if MsgBox == 'yes':
                    self.root.destroy()
                return
        else :
            messagebox.showinfo("Please Enter the Infomation","Please Enter the Infomation")
            

    def __init__(self, Book_ManegementFrame):

        self.root = ThemedTk(theme="equilux")

        #Setting the Title
        self.root.title("Library Management System")

        #Setting the icon
        self.root.iconbitmap('src\\picture\\library.ico')

        #Get the screen resolution
        self.x = self.root.winfo_screenwidth()
        self.y = self.root.winfo_screenheight()

        #Get the value for windows size
        self.x1 = self.x * (4/9)
        self.y1 = self.y * (5/11)

        #Get the value for Starting point for windows
        self.x2 = self.x * (3/11)
        self.y2 = self.y * (2/9)

        self.root.geometry("%dx%d+%d+%d" % (self.x1, self.y1, self.x2, self.y2))
        self.root.resizable(False, False)

        #Easy for configure within attribute
        self.x1 = int(self.x1)
        self.y1 = int(self.y1)

        #Setting Entry variable
        self.nameBook = StringVar()
        self.price = StringVar()
        self.type = StringVar()
        self.author = StringVar()
        self.workplace = StringVar()
        self.publisher = StringVar()
        self.address = StringVar()

        self.style = ttk.Style()
        self.style.configure("Title.TLabel", foreground="snow")
        self.style.configure("Nav.TButton", font=("Cascadia Code SemiBold", 12))
        self.style.configure("Content.TFrame", foreground="black", background="LightSkyBlue2")
        self.style.configure("Content.TLabel", foreground="black", background="LightSkyBlue2")
        self.style.configure("Nav.TFrame", foreground="black", background="SeaGreen1")

        self.content_frame = ttk.Frame(self.root, style="Content.TFrame")
        self.content_frame.place(relwidth=1, relheight=1)

        self.idBookLabel = ttk.Label(self.content_frame, text="Book ID :", font=("Cascadia Code SemiBold", 12), style="Content.TLabel")
        self.idBookLabel.place(relx=0.3, rely=0.05)

        self.idBookEntry = ttk.Label(self.content_frame, text="%s" % Book_ManegementFrame.idbook, font=("Cascadia Code", 12), style="Content.TLabel")
        self.idBookEntry.place(relx=0.43, rely=0.05)

        self.nameBookLabel = ttk.Label(self.content_frame, text="Name :", font=("Cascadia Code SemiBold", 12), style="Content.TLabel")
        self.nameBookLabel.place(relx=0.34, rely=0.15)

        self.nameBookEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12), textvariable=self.nameBook)
        self.nameBookEntry.place(relx=0.43, rely=0.15)

        self.priceLabel = ttk.Label(self.content_frame, text="Price :", font=("Cascadia Code SemiBold", 12), style="Content.TLabel")
        self.priceLabel.place(relx=0.327, rely=0.25)

        self.priceEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12), textvariable=self.price)
        self.priceEntry.place(relx=0.43, rely=0.25)

        self.typeLabel = ttk.Label(self.content_frame, text="Type :", font=("Cascadia Code SemiBold", 12), style="Content.TLabel")
        self.typeLabel.place(relx=0.34, rely=0.35)

        self.typeEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12), textvariable=self.type)
        self.typeEntry.place(relx=0.43, rely=0.35)

        self.authorLabel = ttk.Label(self.content_frame, text="Author :", font=("Cascadia Code SemiBold", 12), style="Content.TLabel")
        self.authorLabel.place(relx=0.15, rely=0.45)

        self.authorEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12), textvariable=self.author)
        self.authorEntry.place(relx=0.26, rely=0.45, relwidth=0.2)

        self.workplaceLabel = ttk.Label(self.content_frame, text="Workplace :", font=("Cascadia Code SemiBold", 12), style="Content.TLabel")
        self.workplaceLabel.place(relx=0.5, rely=0.45)

        self.workplaceEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12), textvariable=self.workplace)
        self.workplaceEntry.place(relx=0.65, rely=0.45, relwidth=0.2)

        self.publisherLabel = ttk.Label(self.content_frame, text="Publisher :", font=("Cascadia Code SemiBold", 12), style="Content.TLabel")
        self.publisherLabel.place(relx=0.11, rely=0.55)

        self.publisherEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12), textvariable=self.publisher)
        self.publisherEntry.place(relx=0.26, rely=0.55, relwidth=0.2)

        self.addressLabel = ttk.Label(self.content_frame, text="Address :", font=("Cascadia Code SemiBold", 12), style="Content.TLabel")
        self.addressLabel.place(relx=0.528, rely=0.55)

        self.addressEntry = ttk.Entry(self.content_frame, font=("Cascadia Code SemiBold", 12), textvariable=self.address)
        self.addressEntry.place(relx=0.65, rely=0.55, relwidth=0.2)

        self.updateButton = ttk.Button(self.content_frame, text="Update", style="Nav.TButton")
        self.updateButton.place(relx=0.45, rely=0.7)

        self.root.mainloop()
