from tkinter import Tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from ttkthemes import ThemedTk
from PIL import ImageTk, Image

from importlib import reload

from ..model.Book import *
from ..sqlTools.BookTools import *
from ..sqlTools.BorrowTools import *

class Login_ReaderFrame:

    def Open_Search_BookFrame(self):
        self.CloseFrame()
        self.frame = Search_BookFrame(self.LoginFrame)

    def Open_Return_BookFrame(self):
        self.CloseFrame()
        self.frame = Return_BookFrame(self.LoginFrame)

    def Logout(self):
        self.CloseFrame()
        self.frame = self.LoginFrame
        self.frame.loginFrame()

    def CloseFrame(self):
        self.root.destroy()


    def __init__(self, LoginFrame):

        self.LoginFrame = LoginFrame
            
        self.root = ThemedTk(theme="equilux")

        #Setting the Title
        self.root.title("Library Management System")

        #Setting the icon
        self.root.iconbitmap('src\\picture\\library.ico')

        #Get the screen resolution
        self.x = self.root.winfo_screenwidth()
        self.y = self.root.winfo_screenheight()

        #Get the value for windows size
        self.x1 = self.x * (13/20)
        self.y1 = self.y * (0.81)

        #Get the value for Starting point for windows
        self.x2 = self.x * (1.1/6)
        self.y2 = self.y * (1/12)

        self.root.geometry("%dx%d+%d+%d" % (self.x1, self.y1, self.x2, self.y2))
        self.root.resizable(False, False)

        #Easy for configure within attribute
        self.x1 = int(self.x1)
        self.y1 = int(self.y1)

        self.x_content = int(self.x1*0.7)
        self.y_content = int(self.y1*0.8)

        self.x_nav = int(self.x1*0.3)
        self.y_nav = int(self.y1*0.8)

        self.style = ttk.Style()
        self.style.configure("Title.TLabel", foreground="snow")
        self.style.configure("Logout.TButton", font=("Cascadia Code SemiBold", 14))
        self.style.configure("Nav.TButton", font=("Cascadia Code SemiBold", 12))
        self.style.configure("Content.TFrame", foreground="black", background="LightSkyBlue2")
        self.style.configure("Nav.TFrame",foreground="black", background="SeaGreen1")
        
        self.title_frame = ttk.Frame(self.root)
        self.title_frame.place(relwidth=1, relheight=0.2)

        self.text_frame = ttk.Frame(self.title_frame)
        self.text_frame.place(relx=0.1, rely=0.5, relwidth=0.4, relheight=0.5)

        self.title_text = ttk.Label(self.text_frame,text="Library Management System",font=("Cascadia Code SemiBold", 18), style="Title.TLabel")
        self.title_text.place(relx=0.05, rely=0.4)

        self.logout_button = ttk.Button(self.title_frame,text="Logout", style="Logout.TButton", command=self.Logout)
        self.logout_button.place(relx=0.78,rely=0.58,relwidth=0.15)

        self.content_frame = ttk.Frame(self.root, style="Content.TFrame")
        self.content_frame.place(relx=0.3,rely=0.2,relwidth=0.7,relheight=0.8)

        self.nav_frame = ttk.Frame(self.root, style="Nav.TFrame")
        self.nav_frame.place(rely=0.2, relwidth=0.3, relheight=0.8)
        
        #Resize the Image
        self.Nav_image = Image.open("src\\picture\\Nav.jpg")
        self.Nav_image = self.Nav_image.resize((self.x_nav, self.y_nav), Image.ANTIALIAS)
        self.Nav_image = ImageTk.PhotoImage(self.Nav_image)

        # (highlightthickness = 0) is for remove the border for the Canvas 
        self.Nav_label = Canvas(self.nav_frame, width=self.x_nav, height=self.y_nav, highlightthickness=0)
        self.Nav_label.pack()
        self.Nav_label.create_image(0, 0, anchor=NW, image=self.Nav_image)

        self.nav_button1 = ttk.Button(self.nav_frame, text="Check Out", style="Nav.TButton", command=self.Open_Search_BookFrame)
        self.nav_button1.place(relx=0.275,rely=0.2,relwidth=0.45)
        self.nav_button2 = ttk.Button(self.nav_frame, text="Check In", style="Nav.TButton", command=self.Open_Return_BookFrame)
        self.nav_button2.place(relx=0.275, rely=0.6, relwidth=0.45)

        self.root.mainloop()


class Return_BookFrame:

    def Open_Search_BookFrame(self):
        self.CloseFrame()
        self.frame = Search_BookFrame(self.LoginFrame)

    def Open_Return_BookFrame(self):
        self.CloseFrame()
        self.frame = Return_BookFrame(self.LoginFrame)

    def Logout(self):
        self.CloseFrame()
        self.frame = self.LoginFrame
        self.frame.loginFrame()

    def CloseFrame(self):
        self.root.destroy()

    def __init__(self, LoginFrame):

        self.LoginFrame = LoginFrame

        self.root = ThemedTk(theme="equilux")

        #Setting the Title
        self.root.title("Library Management System")

        #Setting the icon
        self.root.iconbitmap('src\\picture\\library.ico')

        #Get the screen resolution
        self.x = self.root.winfo_screenwidth()
        self.y = self.root.winfo_screenheight()

        #Get the value for windows size
        self.x1 = self.x * (13/20)
        self.y1 = self.y * (0.81)

        #Get the value for Starting point for windows
        self.x2 = self.x * (1.1/6)
        self.y2 = self.y * (1/12)

        self.root.geometry("%dx%d+%d+%d" % (self.x1, self.y1, self.x2, self.y2))
        self.root.resizable(False, False)

        #Easy for configure within attribute
        self.x1 = int(self.x1)
        self.y1 = int(self.y1)

        self.x_content = int(self.x1*0.7)
        self.y_content = int(self.y1*0.8)

        self.x_nav = int(self.x1*0.3)
        self.y_nav = int(self.y1*0.8)

        self.style = ttk.Style()
        self.style.configure("Title.TLabel", foreground="snow")
        self.style.configure("Logout.TButton", font=("Cascadia Code SemiBold", 14))
        self.style.configure("Nav.TButton", font=("Cascadia Code SemiBold", 12))
        self.style.configure("Content.TFrame", foreground="black", background="LightSkyBlue2")
        self.style.configure("Content.TLabel", foreground="black", background="LightSkyBlue2")
        self.style.configure("Nav.TFrame", foreground="black", background="SeaGreen1")

        self.title_frame = ttk.Frame(self.root)
        self.title_frame.place(relwidth=1, relheight=0.2)

        self.text_frame = ttk.Frame(self.title_frame)
        self.text_frame.place(relx=0.1, rely=0.5, relwidth=0.4, relheight=0.5)

        self.title_text = ttk.Label(self.text_frame, text="Library Management System", font=("Cascadia Code SemiBold", 18), style="Title.TLabel")
        self.title_text.place(relx=0.05, rely=0.4)

        self.logout_button = ttk.Button(self.title_frame, text="Logout", style="Logout.TButton", command=self.Logout)
        self.logout_button.place(relx=0.78, rely=0.58, relwidth=0.15)

        self.content_frame = ttk.Frame(self.root, style="Content.TFrame")
        self.content_frame.place(relx=0.3, rely=0.2, relwidth=0.7, relheight=0.8)

        self.idReaderLabel = ttk.Label(self.content_frame, text="IdReader:", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.idReaderLabel.place(relx=0.28)
        
        self.nameReaderLabel = ttk.Label(self.content_frame, text="NameReader:", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.nameReaderLabel.place(relx=0.08, rely=0.08)

        self.typeLabel = ttk.Label(self.content_frame, text="Post :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.typeLabel.place(relx=0.58, rely=0.08)

        self.sexLabel = ttk.Label(self.content_frame, text="Sex :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.sexLabel.place(relx=0.08, rely=0.16)

        self.passwordLabel = ttk.Label(self.content_frame, text="Password :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.passwordLabel.place(relx=0.58, rely=0.16)

        self.showidReaderLabel = ttk.Label(self.content_frame, text=self.LoginFrame.idReader, font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.showidReaderLabel.place(relx=0.47)

        self.showNameReaderLabel = ttk.Label(self.content_frame, text="", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.showNameReaderLabel.place(relx=0.3, rely=0.08)

        self.showtypeLabel = ttk.Label(self.content_frame, text="", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.showtypeLabel.place(relx=0.71, rely=0.08)

        self.showSexLabel = ttk.Label(self.content_frame, text="", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.showSexLabel.place(relx=0.19, rely=0.16)

        self.showPasswordLabel = ttk.Label(self.content_frame, text="", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.showPasswordLabel.place(relx=0.79, rely=0.16)

        self.content = ttk.Frame(self.content_frame)
        self.content.place(relx=0.1, rely=0.28, relwidth=0.8, relheight=0.45)

        self.nav_frame = ttk.Frame(self.root, style="Nav.TFrame")
        self.nav_frame.place(rely=0.2, relwidth=0.3, relheight=0.8)

        #Resize the Image
        self.Nav_image = Image.open("src\\picture\\Nav.jpg")
        self.Nav_image = self.Nav_image.resize((self.x_nav, self.y_nav), Image.ANTIALIAS)
        self.Nav_image = ImageTk.PhotoImage(self.Nav_image)

        # (highlightthickness = 0) is for remove the border for the Canvas
        self.Nav_label = Canvas(self.nav_frame, width=self.x_nav, height=self.y_nav, highlightthickness=0)
        self.Nav_label.pack()
        self.Nav_label.create_image(0, 0, anchor=NW, image=self.Nav_image)

        self.nav_button1 = ttk.Button(self.nav_frame, text="Check Out", style="Nav.TButton", command=self.Open_Search_BookFrame)
        self.nav_button1.place(relx=0.275, rely=0.2, relwidth=0.45)
        self.nav_button2 = ttk.Button(self.nav_frame, text="Check In", style="Nav.TButton", command=self.Open_Return_BookFrame)
        self.nav_button2.place(relx=0.275, rely=0.6, relwidth=0.45)

        self.root.mainloop()


class Search_BookFrame:

    def CloseFrame(self):
        self.root.destroy()

    def Logout(self):
        self.CloseFrame()
        self.frame = self.LoginFrame
        self.frame.loginFrame()


    def Open_Return_BookFrame(self):
        self.CloseFrame()
        self.frame = Return_BookFrame(self.LoginFrame)

    def do_search_book(self):
        booktools = BookTools()
        borrowtools = BorrowTools()

        keyword = ""
        
        if ( (self.search_bar.get() != None) and (self.search_bar.get() != "") ):
            keyword = self.search_bar.get()
        else :
            messagebox.showwarning("Enter Book Name","Please Enter The Book Name")
            return 
        
        booklist = booktools.BookDataName(keyword)

        if ( len(booklist) == 0 ):
            messagebox.showwarning("Cannot Find Book","Cannot Find The Book")
            return
        else :

            for row in self.heading.get_children():
                self.heading.delete(row)

            for new_row in booklist :
                row_index = booklist.index(new_row) + 1
                temp = Book()
                temp.setAll(new_row)
                whetherInStock = None
                if(borrowtools.whetherInStock(temp.getIdBook())):
                    whetherInStock = "Yes"
                else:
                    whetherInStock = "No"
                self.heading.insert("", row_index, text="%s" % temp.getIdBook(), values=("%s" % temp.getNameBook(), "%d" % temp.getPrice(), "%s" % temp.getType(), "%s" % temp.getAuthor(), "%s" % temp.getPublisher(), "%s" % whetherInStock), tags=('Data',))
                self.heading.tag_configure('Data', font=("Cascadia Code SemiBold", 9))



    def do_borrow_book(self):
        item = None
        for item in self.heading.selection():
            self.check_value = self.heading.item(item, "values")[5]
            self.idbook = self.heading.item(item, "text")

        if item == None:
            messagebox.showwarning("Please Choose A Book", "Please Choose A Book")
        if self.check_value == "No":
            messagebox.showwarning("Book Has been Borrowed", "The Choosen Book Has been Borrowed")
        else:
            borrowtools = BorrowTools()
            self.idReader = self.LoginFrame.idReader
            i = borrowtools.BorrowBook(self.idReader, self.idbook)
            if i == 1:
                messagebox.showinfo("Successfully borrowed", "Successfully borrowed")
            else:
                messagebox.showinfo("Failed To Borrow", "Failed To Borrow")

        self.heading.destroy()
        self.show_data()

    def Open_Search_BookFrame(self):
        self.CloseFrame()
        self.frame = Search_BookFrame(self.LoginFrame)

    def show_data(self):
        self.heading = ttk.Treeview(self.content)

        #Creating Columns
        self.heading['columns'] = ("Column 2", "Column 3", "Column 4", "Column 5", "Column 6", "Column 7")
        self.heading.column("#0", width=5, minwidth=5, anchor=CENTER)
        self.heading.column("Column 2", width=60, minwidth=60, anchor=CENTER)
        self.heading.column("Column 3", width=2, minwidth=2, anchor=CENTER)
        self.heading.column("Column 4", width=2, minwidth=2, anchor=CENTER)
        self.heading.column("Column 5", width=10, minwidth=10, anchor=CENTER)
        self.heading.column("Column 6", width=50, minwidth=50, anchor=CENTER)
        self.heading.column("Column 7", width=80, minwidth=80, anchor=CENTER)

        self.heading.heading("#0", text="IdBook", anchor=CENTER)
        self.heading.heading("Column 2", text="Book Name", anchor=CENTER)
        self.heading.heading("Column 3", text="Price", anchor=CENTER)
        self.heading.heading("Column 4", text="Type", anchor=CENTER)
        self.heading.heading("Column 5", text="Author", anchor=CENTER)
        self.heading.heading("Column 6", text="Publisher", anchor=CENTER)
        self.heading.heading("Column 7", text="Whether In Stock", anchor=CENTER)

        bookTools = BookTools()
        booklist = BookTools().BookData()

        borrowTools = BorrowTools()

        for row in booklist:
            row_index = booklist.index(row) + 1
            temp = Book()
            temp.setAll(row)
            whetherInStock = None
            if(borrowTools.whetherInStock(temp.getIdBook())):
                whetherInStock = "Yes"
            else:
                whetherInStock = "No"
            self.heading.insert("", row_index, text="%s" % temp.getIdBook(), values=("%s" % temp.getNameBook(), "%d" % temp.getPrice(), "%s" % temp.getType(), "%s" % temp.getAuthor(), "%s" % temp.getPublisher(), "%s" % whetherInStock), tags=('Data',))
            self.heading.tag_configure('Data', font=("Cascadia Code SemiBold", 9))
        
        self.vsb = ttk.Scrollbar(self.content_frame,orient="vertical", command=self.heading.yview)
        self.vsb.place(relx=0.9, rely=0.3, relheight=0.45)

        self.heading.pack(side=TOP, fill=X)

        self.heading.configure(yscrollcommand=self.vsb.set)

    def __init__(self, LoginFrame):

        self.LoginFrame = LoginFrame

        self.root = ThemedTk(theme="equilux")

        #Setting the Title
        self.root.title("Library Management System")

        #Setting the icon
        self.root.iconbitmap('src\\picture\\library.ico')

        #Get the screen resolution
        self.x = self.root.winfo_screenwidth()
        self.y = self.root.winfo_screenheight()

        #Get the value for windows size
        self.x1 = self.x * (13/20)
        self.y1 = self.y * (0.81)

        #Get the value for Starting point for windows
        self.x2 = self.x * (1.1/6)
        self.y2 = self.y * (1/12)

        self.root.geometry("%dx%d+%d+%d" % (self.x1, self.y1, self.x2, self.y2))
        self.root.resizable(False, False)

        #Easy for configure within attribute
        self.x1 = int(self.x1)
        self.y1 = int(self.y1)

        self.x_content = int(self.x1*0.7)
        self.y_content = int(self.y1*0.8)

        self.x_nav = int(self.x1*0.3)
        self.y_nav = int(self.y1*0.8)

        self.style = ttk.Style()
        self.style.configure("Title.TLabel", foreground="snow")
        self.style.configure("Logout.TButton", font=("Cascadia Code SemiBold", 14))
        self.style.configure("Nav.TButton", font=("Cascadia Code SemiBold", 12))
        self.style.configure("Content.TFrame", foreground="black", background="LightSkyBlue2")
        self.style.configure("Content.TLabel", foreground="black", background="LightSkyBlue2")
        self.style.configure("Nav.TFrame", foreground="black", background="SeaGreen1")
        self.style.configure("Treeview.Heading", font=("Cascadia Code SemiBold", 9))

        self.title_frame = ttk.Frame(self.root)
        self.title_frame.place(relwidth=1, relheight=0.2)

        self.text_frame = ttk.Frame(self.title_frame)
        self.text_frame.place(relx=0.1, rely=0.5, relwidth=0.4, relheight=0.5)

        self.title_text = ttk.Label(self.text_frame, text="Library Management System", font=("Cascadia Code SemiBold", 18), style="Title.TLabel")
        self.title_text.place(relx=0.05, rely=0.4)

        self.logout_button = ttk.Button(self.title_frame, text="Logout", style="Logout.TButton", command=self.Logout)
        self.logout_button.place(relx=0.78, rely=0.58, relwidth=0.15)

        self.content_frame = ttk.Frame(self.root, style="Content.TFrame")
        self.content_frame.place(relx=0.3, rely=0.2, relwidth=0.7, relheight=0.8)

        self.search_label = ttk.Label(self.content_frame, text="Book Name Searching",font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.search_label.place(relx=0.3)

        self.search_bar = ttk.Entry(self.content_frame, font=("Cascadia Code", 16))
        self.search_bar.place(relx=0.1, rely=0.15, relwidth=0.6)

        self.search_button = ttk.Button(self.content_frame, text="Search", style="Nav.TButton", command=self.do_search_book)
        self.search_button.place(relx=0.75, rely=0.15, relwidth=0.149)

        self.content = ttk.Frame(self.content_frame)
        self.content.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.45)

        self.show_data()

        self.borrow_button = ttk.Button(self.content_frame, text="Borrow", style="Nav.TButton", command=self.do_borrow_book)
        self.borrow_button.place(relx=0.65, rely=0.85)

        self.nav_frame = ttk.Frame(self.root, style="Nav.TFrame")
        self.nav_frame.place(rely=0.2, relwidth=0.3, relheight=0.8)

        #Resize the Image
        self.Nav_image = Image.open("src\\picture\\Nav.jpg")
        self.Nav_image = self.Nav_image.resize((self.x_nav, self.y_nav), Image.ANTIALIAS)
        self.Nav_image = ImageTk.PhotoImage(self.Nav_image)

        # (highlightthickness = 0) is for remove the border for the Canvas
        self.Nav_label = Canvas(self.nav_frame, width=self.x_nav, height=self.y_nav, highlightthickness=0)
        self.Nav_label.pack()
        self.Nav_label.create_image(0, 0, anchor=NW, image=self.Nav_image)

        self.nav_button1 = ttk.Button(self.nav_frame, text="Check Out", style="Nav.TButton", command=self.Open_Search_BookFrame)
        self.nav_button1.place(relx=0.275, rely=0.2, relwidth=0.45)
        self.nav_button2 = ttk.Button(self.nav_frame, text="Check In", style="Nav.TButton", command=self.Open_Return_BookFrame)
        self.nav_button2.place(relx=0.275, rely=0.6, relwidth=0.45)

        self.root.mainloop()

if __name__ == "__main__":
    frame = Login_ReaderFrame()
