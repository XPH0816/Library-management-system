from tkinter import Tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from ttkthemes import ThemedTk
from PIL import ImageTk,Image

from ..model.Librarian import *
from ..model.Reader import *
from ..model.Book import *

from ..sqlTools.BookTools import *
from ..sqlTools.BorrowTools import *
from ..sqlTools.LibrarianTools import *
from ..sqlTools.ReaderTools import *

class LoginFrame:

    #Function for button to Unshow/Show Password
    def show_password(self):
        if self.Show_Button.cget('image') == (str(self.button_image),):
            self.Show_Button.config(image=self.unlock)
            self.Password.config(show="")
        else:
            self.Show_Button.config(image=self.button_image)
            self.Password.config(show="*")

    def Clear_Input(self):
        self.Username.delete(0, END)
        self.Password.delete(0, END)

    def CloseFrame(self):
        self.root.destroy()

    #Function to check login to next Frame
    def check_login(self):
        if (self.var.get() == 1):
            rTools = ReaderTools()
            reader = Reader()
            reader.setIdReader(self.Username.get())
            reader.setPassword(self.Password.get())

            if ((self.Username.get() != None) and (not(reader.equals("", self.Username.get()))) and (self.Password.get() != None) and (not(reader.equals("", self.Password.get())))):
                whether_login = rTools.ReaderLogin(reader.getIdReader(), reader.getPassword())
                if(whether_login == True):
                    self.idReader = reader.getIdReader()
                    self.nameReader = (rTools.ReaderDataId(reader.getIdReader())[0][1])

                    self.CloseFrame()
                    self.frame = Login_ReaderFrame()
                else:
                    messagebox.showinfo("用户名或密码错误", "用户名或密码错误")
            else:
                messagebox.showinfo("请填写用户名和密码", "请填写用户名和密码")
        elif (self.var.get() == 2):
            libTools = LibrarianTools()
            lib = Librarian()
            lib.setNameUser(self.Username.get())
            lib.setPassword(self.Password.get())

            if ((self.Username.get() != None) and (not(lib.equals("", self.Username.get()))) and (self.Password.get() != None) and (not(lib.equals("", self.Password.get())))):
                whether_login = libTools.LibrarianLogin(lib.getNameUser(), lib.getPassword())
                if (whether_login == True):
                    self.nameUser = lib.getNameUser()

                    self.CloseFrame()
                    self.frame = Login_LibrarianFrame()
                else:
                    messagebox.showinfo("用户名或密码错误", "用户名或密码错误")
            else:
                messagebox.showinfo("请填写用户名和密码", "请填写用户名和密码")
            return None

    def loginFrame(self):

        self.root = Tk()

        #Setting the Title
        self.root.title("Library Management System")

        #Setting the icon
        self.root.iconbitmap('src\\picture\\library.ico')

        #Get the screen resolution
        self.x = self.root.winfo_screenwidth()
        self.y = self.root.winfo_screenheight()

        #Get the value for windows size
        self.x1 = self.x * (2/9)
        self.y1 = self.y * (7/11)

        #Get the value for Starting point for windows
        self.x2 = self.x * (2/5)
        self.y2 = self.y * (1/7)

        self.root.geometry("%dx%d+%d+%d" % (self.x1, self.y1, self.x2, self.y2))
        self.root.resizable(False, False)

        #Easy for configure within attribute
        self.x1 = int(self.x1)
        self.y1 = int(self.y1)

        #Setting Radio Button Variable
        self.var = IntVar() # 1 for Reader , 2 for Librarian

        #Setting Style for ttk
        self.style = ttk.Style()
        self.style.configure("BW.TLabel", foreground="black", background="MediumPurple1")
        self.style.configure("BL.Label", foreground="black", background="MediumPurple2")

        self.background_image = Image.open("src\\picture\\Mac.jpeg")
        self.background_image = self.background_image.resize((self.x1, self.y1), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(self.background_image)
        self.background_label = Canvas(self.root, width=self.x, height=self.y)
        self.background_label.pack()
        self.background_label.create_image(0, 0, anchor=NW, image=self.background_image)

        self.frame_top = ttk.Frame(self.root, style="BW.TLabel")
        self.frame_top.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.15)
        self.title = ttk.Label(self.frame_top, text="Library Management System", padding="2 5 2 10", font=("Cascadia Code SemiBold", 14), style="BW.TLabel")
        self.title2 = ttk.Label(self.frame_top, text="Login to access your account", padding="0 0 0 0", font=("Cascadia Code", 13), style="BL.Label")
        self.title.pack()
        self.title2.pack()

        self.login_frame = ttk.Frame(self.root, relief=GROOVE)
        self.login_frame.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.45)

        self.Name_label = ttk.Label(self.login_frame, text="Name/ID :", font=("Cascadia Code", 12))
        self.Username = ttk.Entry(self.login_frame, font=("Cascadia Code", 10))
        self.Name_label.place(relx=0.03, rely=0.125)
        self.Username.place(relx=0.36, rely=0.140, relwidth=0.55)

        self.Password_label = ttk.Label(self.login_frame, text="Password :", font=("Cascadia Code", 11))
        self.Password = ttk.Entry(self.login_frame, font=("Cascadia Code", 10), show="*")

        #Setting Lock Button Image
        self.button_image = Image.open("src\\picture\\lock.png")
        self.button_image = self.button_image.resize((16, 16), Image.ANTIALIAS)
        self.button_image = ImageTk.PhotoImage(self.button_image)

        #Setting Unlock Button Image
        self.unlock = Image.open("src\\picture\\unlock.png")
        self.unlock = self.unlock.resize((16, 16), Image.ANTIALIAS)
        self.unlock = ImageTk.PhotoImage(self.unlock)

        self.Show_Button = ttk.Button(self.login_frame, image=self.button_image, command=self.show_password)

        self.Password_label.place(relx=0.03, rely=0.375)
        self.Password.place(relx=0.36, rely=0.385, relwidth=0.43)
        self.Show_Button.place(relx=0.81, rely=0.375, relwidth=0.1)

        self.type_Frame = ttk.Frame(self.login_frame, relief=GROOVE)
        self.type_Frame.place(relx=0.1, rely=0.57, relwidth=0.8, relheight=0.1)
        self.readerRadioButton = Radiobutton(self.type_Frame, text = "Reader", variable = self.var, value = 1, font=("Cascadia Code", 9))
        self.librarianRadioButton = Radiobutton(self.type_Frame, text = "Librarian", variable = self.var, value = 2, font=("Cascadia Code", 9))
        self.librarianRadioButton.select()
        self.readerRadioButton.place(relx=0.58, rely=0.15, relheight=0.6)
        self.librarianRadioButton.place(relx=0.08, rely=0.15, relheight=0.6)


        self.button_frame = ttk.Frame(self.login_frame, relief=GROOVE)
        self.button_frame.place(relx=0.1, rely=0.73, relwidth=0.8, relheight=0.2)
        self.button_login = ttk.Button(self.button_frame, text="Login", command=self.check_login)
        self.button_clear = ttk.Button(self.button_frame, text="Clear", command=self.Clear_Input)
        self.button_login.place(relx=0.55, rely=0.25, relwidth=0.4)
        self.button_clear.place(relx=0.05, rely=0.25, relwidth=0.4)

        self.root.mainloop()

class Login_ReaderFrame:

    def Open_Search_BookFrame(self):
        self.CloseFrame()
        self.frame = Search_BookFrame()

    def Open_Return_BookFrame(self):
        self.CloseFrame()
        self.frame = Return_BookFrame()

    def Logout(self):
        self.CloseFrame()
        self.frame = self.LoginFrame()
        self.frame.loginFrame()

    def CloseFrame(self):
        self.root.destroy()


    def __init__(self):
            
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

        self.nav_button1 = ttk.Button(self.nav_frame, text="Check In", style="Nav.TButton", command=self.Open_Search_BookFrame)
        self.nav_button1.place(relx=0.275,rely=0.2,relwidth=0.45)
        self.nav_button2 = ttk.Button(self.nav_frame, text="Check Out", style="Nav.TButton", command=self.Open_Return_BookFrame)
        self.nav_button2.place(relx=0.275, rely=0.6, relwidth=0.45)

        self.root.mainloop()


class Return_BookFrame:

    def Open_Search_BookFrame(self):
        self.CloseFrame()
        self.frame = Search_BookFrame()

    def Open_Return_BookFrame(self):
        self.CloseFrame()
        self.frame = Return_BookFrame()

    def Logout(self):
        self.CloseFrame()
        self.frame = LoginFrame()
        self.frame.loginFrame()

    def CloseFrame(self):
        self.root.destroy()

    def __init__(self):

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

        self.nav_frame = ttk.Frame(root, style="Nav.TFrame")
        self.nav_frame.place(rely=0.2, relwidth=0.3, relheight=0.8)

        #Resize the Image
        self.Nav_image = Image.open("src\\picture\\Nav.jpg")
        self.Nav_image = self.Nav_image.resize((self.x_nav, self.y_nav), Image.ANTIALIAS)
        self.Nav_image = ImageTk.PhotoImage(self.Nav_image)

        # (highlightthickness = 0) is for remove the border for the Canvas
        self.Nav_label = Canvas(self.nav_frame, width=self.x_nav, height=self.y_nav, highlightthickness=0)
        self.Nav_label.pack()
        self.Nav_label.create_image(0, 0, anchor=NW, image=self.Nav_image)

        self.nav_button1 = ttk.Button(self.nav_frame, text="Check In", style="Nav.TButton", command=self.Open_Search_BookFrame)
        self.nav_button1.place(relx=0.275, rely=0.2, relwidth=0.45)
        self.nav_button2 = ttk.Button(self.nav_frame, text="Check Out", style="Nav.TButton", command=self.Open_Return_BookFrame)
        self.nav_button2.place(relx=0.275, rely=0.6, relwidth=0.45)

        self.root.mainloop()


class Search_BookFrame:

    def CloseFrame(self):
        self.root.destroy()

    def Logout(self):
        self.CloseFrame()
        self.frame = LoginFrame()
        self.frame.loginFrame()


    def Open_Return_BookFrame(self):
        self.CloseFrame()
        self.frame = Return_BookFrame()

    def do_borrow_book(self):
        item = None
        for item in self.heading.selection():
            self.item_text = self.heading.item(item, "text")
            self.check_value = self.heading.item(item, "values")[5]
            self.idbook = self.heading.item(item, "values")[0]

        if item == None:
            messagebox.showwarning("Please Choose A Book", "Please Choose A Book")
        if self.check_value == "No":
            messagebox.showwarning("Book Has been Borrowed", "The Choosen Book Has been Borrowed")
        else:
            borrowtools = BorrowTools()
            self.idReader = LoginFrame.idReader
            i = borrowtools.BorrowBook(self.idReader, self.idbook)
            if i == 1:
                messagebox.showinfo("Successfully borrowed", "Successfully borrowed")
            else:
                messagebox.showinfo("Failed To Borrow", "Failed To Borrow")

    def Open_Search_BookFrame(self):
        self.CloseFrame()
        self.frame = Search_BookFrame()

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

        self.heading.pack(side=TOP, fill=X)

    def __init__(self):

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

        self.search_button = ttk.Button(self.content_frame, text="Search", style="Nav.TButton")
        self.search_button.place(relx=0.75, rely=0.15, relwidth=0.149)

        self.content = ttk.Frame(self.content_frame)
        self.content.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

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

        self.nav_button1 = ttk.Button(self.nav_frame, text="Check In", style="Nav.TButton", command=self.Open_Search_BookFrame)
        self.nav_button1.place(relx=0.275, rely=0.2, relwidth=0.45)
        self.nav_button2 = ttk.Button(self.nav_frame, text="Check Out", style="Nav.TButton", command=self.Open_Return_BookFrame)
        self.nav_button2.place(relx=0.275, rely=0.6, relwidth=0.45)

        self.root.mainloop()
