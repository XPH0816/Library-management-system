from os import stat
from tkinter import Tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from ttkthemes import ThemedTk
from PIL import ImageTk, Image

from ..model.Author import *
from ..model.Book import *
from ..model.Reader import *
from ..model.Publisher import *
from ..sqlTools.BorrowTools import *
from ..sqlTools.ReaderTools import *
from ..sqlTools.AuthorTools import *
from ..sqlTools.BookTools import *
from ..sqlTools.PublisherTools import *

class Login_LibrarianFrame:

    def Logout(self):
        self.CloseFrame()
        self.frame = self.LoginFrame
        self.frame.loginFrame()
    
    def CloseFrame(self):
        self.root.destroy()

    def Open_Reader_RegisterFrame(self):
        self.CloseFrame()
        self.frame = reader_RegisterFrame(self.LoginFrame)

    def Open_Book_RegisterFrame(self):
        self.CloseFrame()
        self.frame = book_RegisterFrame(self.LoginFrame)

    def Open_Reader_ManagementFrame(self):
        self.CloseFrame()
        self.frame = Reader_ManagementFrame(self.LoginFrame)

    def Open_Book_ManagementFrame(self):
        self.CloseFrame()
        self.frame = Book_ManegementFrame(self.LoginFrame)

    def Open_Lending_ManegementFrame(self):
        self.CloseFrame()
        self.frame = Lending_ManagementFrame(self.LoginFrame)

    def __init__(self, LoginFrame):

        self.LoginFrame =  LoginFrame
        
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
        self.text_frame.place(relx=0.1,rely=0.5, relwidth=0.4, relheight=0.5)

        self.title_text = ttk.Label(self.text_frame,text="Library Management System",font=("Cascadia Code SemiBold", 18), style="Title.TLabel")
        self.title_text.place(relx=0.05, rely=0.4)

        self.logout_button = ttk.Button(self.title_frame,text="Logout", style="Logout.TButton", command=self.Logout)
        self.logout_button.place(relx=0.78, rely=0.58, relwidth=0.15)

        self.content_frame = ttk.Frame(self.root, style="Content.TFrame")
        self.content_frame.place(relx=0.3, rely=0.2, relwidth=1, relheight=0.8)

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

        self.nav_button1 = ttk.Button(self.nav_frame, text="User Register",
                                      style="Nav.TButton", command=self.Open_Reader_RegisterFrame)
        self.nav_button1.place(relx=0.25, rely=0.05, relwidth=0.5)
        self.nav_button2 = ttk.Button(
            self.nav_frame, text="Book Regsiter", style="Nav.TButton", command=self.Open_Book_RegisterFrame)
        self.nav_button2.place(relx=0.25, rely=0.25, relwidth=0.5)
        self.nav_button3 = ttk.Button(self.nav_frame, text="User Manage",
                                      style="Nav.TButton", command=self.Open_Reader_ManagementFrame)
        self.nav_button3.place(relx=0.25, rely=0.45, relwidth=0.5)
        self.nav_button4 = ttk.Button(
            self.nav_frame, text="Book Manage", style="Nav.TButton", command=self.Open_Book_ManagementFrame)
        self.nav_button4.place(relx=0.25, rely=0.65, relwidth=0.5)
        self.nav_button5 = ttk.Button(self.nav_frame, text="Lending Manage",
                                      style="Nav.TButton", command=self.Open_Lending_ManegementFrame)
        self.nav_button5.place(relx=0.25, rely=0.85, relwidth=0.5)

        self.root.mainloop()

class reader_RegisterFrame :

    def Logout(self):
        self.CloseFrame()
        self.frame = self.LoginFrame
        self.frame.loginFrame()

    def CloseFrame(self):
        self.root.destroy()

    def Open_Reader_RegisterFrame(self):
        self.CloseFrame()
        self.frame = reader_RegisterFrame(self.LoginFrame)

    def Open_Book_RegisterFrame(self):
        self.CloseFrame()
        self.frame = book_RegisterFrame(self.LoginFrame)

    def Open_Reader_ManagementFrame(self):
        self.CloseFrame()
        self.frame = Reader_ManagementFrame(self.LoginFrame)

    def Open_Book_ManagementFrame(self):
        self.CloseFrame()
        self.frame = Book_ManegementFrame(self.LoginFrame)

    def Open_Lending_ManegementFrame(self):
        self.CloseFrame()
        self.frame = Lending_ManagementFrame(self.LoginFrame)

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
        self.content_frame.place(relx=0.3, rely=0.2, relwidth=1, relheight=0.8)

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

        self.nav_button1 = ttk.Button(self.nav_frame, text="User Register",
                                      style="Nav.TButton", command=self.Open_Reader_RegisterFrame)
        self.nav_button1.place(relx=0.25, rely=0.05, relwidth=0.5)
        self.nav_button2 = ttk.Button(
            self.nav_frame, text="Book Regsiter", style="Nav.TButton", command=self.Open_Book_RegisterFrame)
        self.nav_button2.place(relx=0.25, rely=0.25, relwidth=0.5)
        self.nav_button3 = ttk.Button(self.nav_frame, text="User Manage",
                                      style="Nav.TButton", command=self.Open_Reader_ManagementFrame)
        self.nav_button3.place(relx=0.25, rely=0.45, relwidth=0.5)
        self.nav_button4 = ttk.Button(
            self.nav_frame, text="Book Manage", style="Nav.TButton", command=self.Open_Book_ManagementFrame)
        self.nav_button4.place(relx=0.25, rely=0.65, relwidth=0.5)
        self.nav_button5 = ttk.Button(self.nav_frame, text="Lending Manage",
                                      style="Nav.TButton", command=self.Open_Lending_ManegementFrame)
        self.nav_button5.place(relx=0.25, rely=0.85, relwidth=0.5)

        self.idReaderLabel = ttk.Label(self.content_frame, text="ID Reader :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.idReaderLabel.place(relx=0.2, rely=0.15)

        self.idReaderEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12))
        self.idReaderEntry.place(relx=0.37, rely=0.16)

        self.nameReaderLabel = ttk.Label(self.content_frame, text="Name :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.nameReaderLabel.place(relx=0.272, rely=0.25)

        self.nameReaderEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12))
        self.nameReaderEntry.place(relx=0.37, rely=0.26)

        self.positionLabel = ttk.Label(self.content_frame, text="Position :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.positionLabel.place(relx=0.215, rely=0.35)

        self.positionEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12))
        self.positionEntry.place(relx=0.37, rely=0.36)

        self.sexLabel = ttk.Label(self.content_frame, text="Sex :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.sexLabel.place(relx=0.285, rely=0.45)

        self.sexEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12))
        self.sexEntry.place(relx=0.37, rely=0.46)

        self.passwordLabel = ttk.Label(self.content_frame, text="Password :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.passwordLabel.place(relx=0.215, rely=0.55)

        self.passwordEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12))
        self.passwordEntry.place(relx=0.37, rely=0.56)

        self.registerButton = ttk.Button(self.content_frame, text="Register", style="Nav.TButton")
        self.registerButton.place(relx=0.3, rely=0.7)

        self.root.mainloop()

class book_RegisterFrame :

    def Logout(self):
        self.CloseFrame()
        self.frame = self.LoginFrame
        self.frame.loginFrame()

    def CloseFrame(self):
        self.root.destroy()

    def Open_Reader_RegisterFrame(self):
        self.CloseFrame()
        self.frame = reader_RegisterFrame(self.LoginFrame)

    def Open_Book_RegisterFrame(self):
        self.CloseFrame()
        self.frame = book_RegisterFrame(self.LoginFrame)

    def Open_Reader_ManagementFrame(self):
        self.CloseFrame()
        self.frame = Reader_ManagementFrame(self.LoginFrame)

    def Open_Book_ManagementFrame(self):
        self.CloseFrame()
        self.frame = Book_ManegementFrame(self.LoginFrame)

    def Open_Lending_ManegementFrame(self):
        self.CloseFrame()
        self.frame = Lending_ManagementFrame(self.LoginFrame)

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

        self.root.geometry("%dx%d+%d+%d" %
                           (self.x1, self.y1, self.x2, self.y2))
        self.root.resizable(False, False)

        #Easy for configure within attribute
        self.x1 = int(self.x1)
        self.y1 = int(self.y1)

        self.x_nav = int(self.x1*0.3)
        self.y_nav = int(self.y1*0.8)
        
        #Setting the ttk Style
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

        self.title_text = ttk.Label(self.text_frame, text="Library Management System", font=(
            "Cascadia Code SemiBold", 18), style="Title.TLabel")
        self.title_text.place(relx=0.05, rely=0.4)

        self.logout_button = ttk.Button(
            self.title_frame, text="Logout", style="Logout.TButton", command=self.Logout)
        self.logout_button.place(relx=0.78, rely=0.58, relwidth=0.15)

        self.content_frame = ttk.Frame(self.root, style="Content.TFrame")
        self.content_frame.place(relx=0.3, rely=0.2, relwidth=1, relheight=0.8)

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

        self.nav_button1 = ttk.Button(self.nav_frame, text="User Register", style="Nav.TButton", command=self.Open_Reader_RegisterFrame)
        self.nav_button1.place(relx=0.25, rely=0.05, relwidth=0.5)
        self.nav_button2 = ttk.Button(self.nav_frame, text="Book Regsiter", style="Nav.TButton", command=self.Open_Book_RegisterFrame)
        self.nav_button2.place(relx=0.25, rely=0.25, relwidth=0.5)
        self.nav_button3 = ttk.Button(self.nav_frame, text="User Manage", style="Nav.TButton", command=self.Open_Reader_ManagementFrame)
        self.nav_button3.place(relx=0.25, rely=0.45, relwidth=0.5)
        self.nav_button4 = ttk.Button(self.nav_frame, text="Book Manage", style="Nav.TButton", command=self.Open_Book_ManagementFrame)
        self.nav_button4.place(relx=0.25, rely=0.65, relwidth=0.5)
        self.nav_button5 = ttk.Button(self.nav_frame, text="Lending Manage", style="Nav.TButton", command=self.Open_Lending_ManegementFrame)
        self.nav_button5.place(relx=0.25, rely=0.85, relwidth=0.5)

        self.idBookLabel = ttk.Label(self.content_frame, text="Book ID :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.idBookLabel.place(relx=0.23, rely=0.05)

        self.idBookEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12))
        self.idBookEntry.place(relx=0.37, rely=0.06)

        self.nameBookLabel = ttk.Label(self.content_frame, text="Name :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.nameBookLabel.place(relx=0.273, rely=0.15)

        self.nameBookEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12))
        self.nameBookEntry.place(relx=0.37, rely=0.16)

        self.priceLabel = ttk.Label(self.content_frame, text="Price :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.priceLabel.place(relx=0.26, rely=0.25)

        self.priceEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12))
        self.priceEntry.place(relx=0.37, rely=0.26)

        self.typeLabel = ttk.Label(self.content_frame, text="Type :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.typeLabel.place(relx=0.274, rely=0.35)

        self.typeEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12))
        self.typeEntry.place(relx=0.37, rely=0.36)

        self.authorLabel = ttk.Label(self.content_frame, text="Author :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.authorLabel.place(relx=0.092, rely=0.5)

        self.authorEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12))
        self.authorEntry.place(relx=0.21, rely=0.51, relwidth=0.15)

        self.workplaceLabel = ttk.Label(self.content_frame, text="Workplace :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.workplaceLabel.place(relx=0.38, rely=0.5)

        self.workplaceEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12))
        self.workplaceEntry.place(relx=0.54, rely=0.51, relwidth=0.15)

        self.publisherLabel = ttk.Label(self.content_frame, text="Publisher :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.publisherLabel.place(relx=0.05, rely=0.65)

        self.publisherEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12))
        self.publisherEntry.place(relx=0.21 , rely=0.66, relwidth=0.15)

        self.addressLabel = ttk.Label(self.content_frame, text="Address :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.addressLabel.place(relx=0.408, rely=0.65)

        self.addressEntry = ttk.Entry(self.content_frame, font=("Cascadia Code SemiBold", 12))
        self.addressEntry.place(relx=0.54, rely=0.66, relwidth=0.15)

        self.registerButton = ttk.Button(self.content_frame, text="Register", style="Nav.TButton")
        self.registerButton.place(relx=0.35, rely=0.8)

        self.root.mainloop()

class Reader_ManagementFrame:

    def Logout(self):
        self.CloseFrame()
        self.frame = self.LoginFrame
        self.frame.loginFrame()

    def CloseFrame(self):
        self.root.destroy()

    def Open_Reader_RegisterFrame(self):
        self.CloseFrame()
        self.frame = reader_RegisterFrame(self.LoginFrame)
    
    def Open_Book_RegisterFrame(self):
        self.CloseFrame()
        self.frame = book_RegisterFrame(self.LoginFrame)

    def Open_Reader_ManagementFrame(self):
        self.CloseFrame()
        self.frame = Reader_ManagementFrame(self.LoginFrame)

    def Open_Book_ManagementFrame(self):
        self.CloseFrame()
        self.frame = Book_ManegementFrame(self.LoginFrame)

    def Open_Lending_ManegementFrame(self):
        self.CloseFrame()
        self.frame = Lending_ManagementFrame(self.LoginFrame)

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
        self.content_frame.place(relx=0.3, rely=0.2, relwidth=1, relheight=0.8)

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

        self.nav_button1 = ttk.Button(self.nav_frame, text="User Register", style="Nav.TButton", command=self.Open_Reader_RegisterFrame)
        self.nav_button1.place(relx=0.25, rely=0.05, relwidth=0.5)
        self.nav_button2 = ttk.Button(self.nav_frame, text="Book Regsiter", style="Nav.TButton", command=self.Open_Book_RegisterFrame)
        self.nav_button2.place(relx=0.25, rely=0.25, relwidth=0.5)
        self.nav_button3 = ttk.Button(self.nav_frame, text="User Manage", style="Nav.TButton", command=self.Open_Reader_ManagementFrame)
        self.nav_button3.place(relx=0.25, rely=0.45, relwidth=0.5)
        self.nav_button4 = ttk.Button(self.nav_frame, text="Book Manage", style="Nav.TButton", command=self.Open_Book_ManagementFrame)
        self.nav_button4.place(relx=0.25, rely=0.65, relwidth=0.5)
        self.nav_button5 = ttk.Button(self.nav_frame, text="Lending Manage", style="Nav.TButton", command=self.Open_Lending_ManegementFrame)
        self.nav_button5.place(relx=0.25, rely=0.85, relwidth=0.5)

        self.content = ttk.Frame(self.content_frame)
        self.content.place(relx=0.05, rely=0.1, relwidth=0.6, relheight=0.65)

        self.updateButton = ttk.Button(self.content_frame, text="Update", style="Nav.TButton")
        self.updateButton.place(relx=0.15, rely=0.8)

        self.deleteButton = ttk.Button(self.content_frame, text="Delete", style="Nav.TButton")
        self.deleteButton.place(relx=0.45, rely=0.8)
        
        self.root.mainloop()

class Book_ManegementFrame:

    def Logout(self):
        self.CloseFrame()
        self.frame = self.LoginFrame
        self.frame.loginFrame()

    def CloseFrame(self):
        self.root.destroy()

    def Open_Reader_RegisterFrame(self):
        self.CloseFrame()
        self.frame = reader_RegisterFrame(self.LoginFrame)

    def Open_Book_RegisterFrame(self):
        self.CloseFrame()
        self.frame = book_RegisterFrame(self.LoginFrame)

    def Open_Reader_ManagementFrame(self):
        self.CloseFrame()
        self.frame = Reader_ManagementFrame(self.LoginFrame)

    def Open_Book_ManagementFrame(self):
        self.CloseFrame()
        self.frame = Book_ManegementFrame(self.LoginFrame)

    def Open_Lending_ManegementFrame(self):
        self.CloseFrame()
        self.frame = Lending_ManagementFrame(self.LoginFrame)

    def show_data(self):
        self.heading = ttk.Treeview(self.content)

        #Creating Columns
        self.heading['columns'] = (
            "Column 2", "Column 3", "Column 4", "Column 5", "Column 6", "Column 7", "Column 8", "Column 9")
        self.heading.column("#0", width=5, minwidth=5, anchor=CENTER)
        self.heading.column("Column 2", width=60, minwidth=60, anchor=CENTER)
        self.heading.column("Column 3", width=2, minwidth=2, anchor=CENTER)
        self.heading.column("Column 4", width=2, minwidth=2, anchor=CENTER)
        self.heading.column("Column 5", width=10, minwidth=10, anchor=CENTER)
        self.heading.column("Column 6", width=50, minwidth=50, anchor=CENTER)
        self.heading.column("Column 7", width=50, minwidth=50, anchor=CENTER)
        self.heading.column("Column 8", width=50, minwidth=50, anchor=CENTER)
        self.heading.column("Column 9", width=80, minwidth=80, anchor=CENTER)

        self.heading.heading("#0", text="IdBook", anchor=CENTER)
        self.heading.heading("Column 2", text="Book Name", anchor=CENTER)
        self.heading.heading("Column 3", text="Price", anchor=CENTER)
        self.heading.heading("Column 4", text="Type", anchor=CENTER)
        self.heading.heading("Column 5", text="Author", anchor=CENTER)
        self.heading.heading("Column 6", text="Publisher", anchor=CENTER)
        self.heading.heading("Column 7", text="Workplace", anchor=CENTER)
        self.heading.heading("Column 8", text="Address", anchor=CENTER)
        self.heading.heading("Column 9", text="Whether In Stock", anchor=CENTER)

        bookTools = BookTools()
        authorTools = AuthorTools()
        publisherTools = PublisherTools()

        booklist = bookTools.BookData()
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
            authorlist = authorTools.AuthorDataName(temp.getAuthor())
            publisher = publisherTools.PublisherDataName(temp.getPublisher())
            self.heading.insert("", row_index, text="%s" % temp.getIdBook(), values=("%s" % temp.getNameBook(), "%d" % temp.getPrice(), "%s" % temp.getType(), "%s" % temp.getAuthor(), "%s" % temp.getPublisher(),"%s" % authorlist[0][1], "%s" % publisher[1],  "%s" % whetherInStock), tags=('Data',))
            self.heading.tag_configure('Data', font=("Cascadia Code SemiBold", 12))
        
        self.vsb = ttk.Scrollbar(self.content_frame,orient="vertical", command=self.heading.yview)
        self.vsb.place(relx=0.65, rely=0.2, relheight=0.6)

        self.heading.pack(side=TOP, fill=X)

        self.heading.configure(yscrollcommand=self.vsb.set)

        del bookTools,authorTools,borrowTools,booklist,publisherTools

    def do_search_book(self):

        # For Book Name
        if self.var.get() == 2 :
            self.heading.destroy()
            self.vsb.destroy()

            self.heading = ttk.Treeview(self.content)

            #Creating Columns
            self.heading['columns'] = ("Column 2", "Column 3", "Column 4", "Column 5", "Column 6", "Column 7", "Column 8", "Column 9")
            self.heading.column("#0", width=5, minwidth=5, anchor=CENTER)
            self.heading.column("Column 2", width=60, minwidth=60, anchor=CENTER)
            self.heading.column("Column 3", width=2, minwidth=2, anchor=CENTER)
            self.heading.column("Column 4", width=2, minwidth=2, anchor=CENTER)
            self.heading.column("Column 5", width=10, minwidth=10, anchor=CENTER)
            self.heading.column("Column 6", width=50, minwidth=50, anchor=CENTER)
            self.heading.column("Column 7", width=50, minwidth=50, anchor=CENTER)
            self.heading.column("Column 8", width=50, minwidth=50, anchor=CENTER)
            self.heading.column("Column 9", width=80, minwidth=80, anchor=CENTER)

            self.heading.heading("#0", text="IdBook", anchor=CENTER)
            self.heading.heading("Column 2", text="Book Name", anchor=CENTER)
            self.heading.heading("Column 3", text="Price", anchor=CENTER)
            self.heading.heading("Column 4", text="Type", anchor=CENTER)
            self.heading.heading("Column 5", text="Author", anchor=CENTER)
            self.heading.heading("Column 6", text="Publisher", anchor=CENTER)
            self.heading.heading("Column 7", text="Workplace", anchor=CENTER)
            self.heading.heading("Column 8", text="Address", anchor=CENTER)
            self.heading.heading("Column 9", text="Whether In Stock", anchor=CENTER)

            bookTools = BookTools()
            authorTools = AuthorTools()
            publisherTools = PublisherTools()

            borrowTools = BorrowTools()

            keyword = None
            if self.searchbar.get() != None and self.searchbar.get() != "" :
                keyword = self.searchbar.get()
            else :
                self.show_data()
                messagebox.showinfo("Please Enter the Book Name","Please Enter the Book Name")
                return
            
            booklist = bookTools.BookDataName(keyword)

            if len(booklist) == 0 :
                messagebox.showinfo("Cant Find the Book","Cant Find the Book Based on the Book Name Given")
            else :
                for row in booklist:
                    row_index = booklist.index(row) + 1
                    temp = Book()
                    temp.setAll(row)
                    whetherInStock = None
                    if(borrowTools.whetherInStock(temp.getIdBook())):
                        whetherInStock = "Yes"
                    else:
                        whetherInStock = "No"
                    authorlist = authorTools.AuthorDataName(temp.getAuthor())
                    publisher = publisherTools.PublisherDataName(temp.getPublisher())
                    self.heading.insert("", row_index, text="%s" % temp.getIdBook(), values=("%s" % temp.getNameBook(), "%d" % temp.getPrice(), "%s" % temp.getType(), "%s" % temp.getAuthor(), "%s" % temp.getPublisher(),"%s" % authorlist[0][1], "%s" % publisher[1],  "%s" % whetherInStock), tags=('Data',))
                    self.heading.tag_configure('Data', font=("Cascadia Code SemiBold", 12))

            self.vsb = ttk.Scrollbar(self.content_frame,orient="vertical", command=self.heading.yview)
            self.vsb.place(relx=0.9, rely=0.3, relheight=0.6)

            self.heading.pack(side=TOP, fill=X)

            self.heading.configure(yscrollcommand=self.vsb.set)

            del bookTools,authorTools,borrowTools,booklist,publisherTools
        
        #For Book ID
        if self.var.get() == 1 :
            self.heading.destroy()
            self.vsb.destroy()

            self.heading = ttk.Treeview(self.content)

            #Creating Columns
            self.heading['columns'] = ("Column 2", "Column 3", "Column 4", "Column 5", "Column 6", "Column 7", "Column 8", "Column 9")
            self.heading.column("#0", width=5, minwidth=5, anchor=CENTER)
            self.heading.column("Column 2", width=60, minwidth=60, anchor=CENTER)
            self.heading.column("Column 3", width=2, minwidth=2, anchor=CENTER)
            self.heading.column("Column 4", width=2, minwidth=2, anchor=CENTER)
            self.heading.column("Column 5", width=10, minwidth=10, anchor=CENTER)
            self.heading.column("Column 6", width=50, minwidth=50, anchor=CENTER)
            self.heading.column("Column 7", width=50, minwidth=50, anchor=CENTER)
            self.heading.column("Column 8", width=50, minwidth=50, anchor=CENTER)
            self.heading.column("Column 9", width=80, minwidth=80, anchor=CENTER)

            self.heading.heading("#0", text="IdBook", anchor=CENTER)
            self.heading.heading("Column 2", text="Book Name", anchor=CENTER)
            self.heading.heading("Column 3", text="Price", anchor=CENTER)
            self.heading.heading("Column 4", text="Type", anchor=CENTER)
            self.heading.heading("Column 5", text="Author", anchor=CENTER)
            self.heading.heading("Column 6", text="Publisher", anchor=CENTER)
            self.heading.heading("Column 7", text="Workplace", anchor=CENTER)
            self.heading.heading("Column 8", text="Address", anchor=CENTER)
            self.heading.heading("Column 9", text="Whether In Stock", anchor=CENTER)

            bookTools = BookTools()
            authorTools = AuthorTools()
            publisherTools = PublisherTools()

            borrowTools = BorrowTools()

            keyword = None
            if self.searchbar.get() != None and self.searchbar.get() != "" :
                keyword = self.searchbar.get()
            else :
                self.show_data()
                messagebox.showinfo("Please Enter the Book ID","Please Enter the Book ID")
                return
            
            booklist = bookTools.Search_Book(keyword)

            if len(booklist) == 0 :
                messagebox.showinfo("Cant Find the Book","Cant Find the Book Based on the Book ID Given")
            else :
                for row in booklist:
                    row_index = booklist.index(row) + 1
                    temp = Book()
                    temp.setAll(row)
                    whetherInStock = None
                    if(borrowTools.whetherInStock(temp.getIdBook())):
                        whetherInStock = "Yes"
                    else:
                        whetherInStock = "No"
                    authorlist = authorTools.AuthorDataName(temp.getAuthor())
                    publisher = publisherTools.PublisherDataName(temp.getPublisher())
                    self.heading.insert("", row_index, text="%s" % temp.getIdBook(), values=("%s" % temp.getNameBook(), "%d" % temp.getPrice(), "%s" % temp.getType(), "%s" % temp.getAuthor(), "%s" % temp.getPublisher(),"%s" % authorlist[0][1], "%s" % publisher[1],  "%s" % whetherInStock), tags=('Data',))
                    self.heading.tag_configure('Data', font=("Cascadia Code SemiBold", 12))

            self.vsb = ttk.Scrollbar(self.content_frame,orient="vertical", command=self.heading.yview)
            self.vsb.place(relx=0.9, rely=0.3, relheight=0.6)

            self.heading.pack(side=TOP, fill=X)

            self.heading.configure(yscrollcommand=self.vsb.set)

            del bookTools, authorTools, borrowTools, booklist, publisherTools

    def updateBook(self):
        item = None
        for item in self.heading.selection():
            self.idbook = self.heading.item(item, "text")
            self.namebook = self.heading.item(item, "values")[0]
            self.price = self.heading.item(item, "values")[1]
            self.type = self.heading.item(item, "values")[2]
            self.author = self.heading.item(item, "values")[3]
            self.publisher = self.heading.item(item, "values")[4]
            self.workplace = self.heading.item(item, "values")[5]
            self.address = self.heading.item(item, "values")[6]
        
        if item == None:
            messagebox.showwarning("Please Choose A Book", "Please Choose A Book")
            return

        self.updateBook_Frame = UpdateBook_Frame(self)

    def delete_Book(self):
        item = None
        for item in self.heading.selection():
            self.idbook = self.heading.item(item, "text")

        if item == None:
            messagebox.showwarning("Please Choose A Book", "Please Choose A Book")
            return
        
        bookTools = BookTools()
        i = bookTools.DeteleBook(self.idbook)
        if i == 1 :
            messagebox.showinfo("Successfully deleted", "Successfully deleted")
            self.heading.destroy()
            self.show_data()
            return
        else :
            messagebox.showinfo("Failed To Delete", "Failed To Delete")
            return


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
        self.x1 = self.x * (17/20)
        self.y1 = self.y * (0.85)

        #Get the value for Starting point for windows
        self.x2 = self.x * (1.1/15)
        self.y2 = self.y * (1/15)

        self.root.geometry("%dx%d+%d+%d" %
                           (self.x1, self.y1, self.x2, self.y2))
        self.root.resizable(False, False)

        #Easy for configure within attribute
        self.x1 = int(self.x1)
        self.y1 = int(self.y1)

        self.x_nav = int(self.x1*0.3)
        self.y_nav = int(self.y1*0.8)

        #Setting Radio Button Variable
        self.var = IntVar() # 1 for Book ID, 2 for Book Name

        self.style = ttk.Style()
        self.style.configure("Title.TLabel", foreground="snow")
        self.style.configure("Logout.TButton", font=("Cascadia Code SemiBold", 14))
        self.style.configure("Nav.TButton", font=("Cascadia Code SemiBold", 12))
        self.style.configure("Content.TButton", font=("Cascadia Code SemiBold", 14))
        self.style.configure("Content.TButton", font=("Cascadia Code SemiBold", 14))
        self.style.configure("Content.TFrame", foreground="black", background="LightSkyBlue2")
        self.style.configure("Content.TRadiobutton", font=("Cascadia Code", 14))
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
        self.content_frame.place(relx=0.3, rely=0.2, relwidth=1, relheight=0.8)

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

        self.nav_button1 = ttk.Button(self.nav_frame, text="User Register", style="Nav.TButton", command=self.Open_Reader_RegisterFrame)
        self.nav_button1.place(relx=0.25, rely=0.05, relwidth=0.5)
        self.nav_button2 = ttk.Button(self.nav_frame, text="Book Regsiter", style="Nav.TButton", command=self.Open_Book_RegisterFrame)
        self.nav_button2.place(relx=0.25, rely=0.25, relwidth=0.5)
        self.nav_button3 = ttk.Button(self.nav_frame, text="User Manage", style="Nav.TButton", command=self.Open_Reader_ManagementFrame)
        self.nav_button3.place(relx=0.25, rely=0.45, relwidth=0.5)
        self.nav_button4 = ttk.Button(self.nav_frame, text="Book Manage", style="Nav.TButton", command=self.Open_Book_ManagementFrame)
        self.nav_button4.place(relx=0.25, rely=0.65, relwidth=0.5)
        self.nav_button5 = ttk.Button(self.nav_frame, text="Lending Manage", style="Nav.TButton", command=self.Open_Lending_ManegementFrame)
        self.nav_button5.place(relx=0.25, rely=0.85, relwidth=0.5)

        self.searchbar = ttk.Entry(self.content_frame, font=("Cascadia Code SemiBold", 18))
        self.searchbar.place(relx=0.1, rely=0.05, relwidth=0.4)

        self.searchButton = ttk.Button(self.content_frame, text="Search", style="Content.TButton", command=self.do_search_book)
        self.searchButton.place(relx=0.53, rely=0.05)

        self.bookID_radiobutton = ttk.Radiobutton(self.content_frame, text = "Book ID", variable = self.var, value = 1, style="Content.TRadiobutton")
        self.bookID_radiobutton.place(relx=0.15, rely=0.13)

        self.var.set(1)

        self.bookName_radiobutton = ttk.Radiobutton(self.content_frame, text = "Book Name", variable = self.var, value = 2, style="Content.TRadiobutton")
        self.bookName_radiobutton.place(relx=0.35, rely=0.13)

        self.content = ttk.Frame(self.content_frame)
        self.content.place(relx=0.05, rely=0.2, relwidth=0.6, relheight=0.6)

        self.updateButton = ttk.Button(self.content_frame, text="Update", style="Content.TButton", command=self.updateBook)
        self.updateButton.place(relx=0.1, rely=0.85, relwidth=0.15)

        self.deleteButton = ttk.Button(self.content_frame, text="Delete", style="Content.TButton")
        self.deleteButton.place(relx=0.45, rely=0.85, relwidth=0.15)

        self.show_data()

        self.root.mainloop()

class Lending_ManagementFrame:

    def Logout(self):
        self.CloseFrame()
        self.frame = self.LoginFrame
        self.frame.loginFrame()

    def CloseFrame(self):
        self.root.destroy()

    def Open_Reader_RegisterFrame(self):
        self.CloseFrame()
        self.frame = reader_RegisterFrame(self.LoginFrame)

    def Open_Book_RegisterFrame(self):
        self.CloseFrame()
        self.frame = book_RegisterFrame(self.LoginFrame)

    def Open_Reader_ManagementFrame(self):
        self.CloseFrame()
        self.frame = Reader_ManagementFrame(self.LoginFrame)

    def Open_Book_ManagementFrame(self):
        self.CloseFrame()
        self.frame = Book_ManegementFrame(self.LoginFrame)

    def Open_Lending_ManegementFrame(self):
        self.CloseFrame()
        self.frame = Lending_ManagementFrame(self.LoginFrame)

    def show_data(self):
        self.heading = ttk.Treeview(self.content)

        #Creating Columns
        self.heading['columns'] = (
            "Column 2", "Column 3", "Column 4", "Column 5", "Column 6")
        self.heading.column("#0", width=5, minwidth=5, anchor=CENTER)
        self.heading.column("Column 2", width=60, minwidth=60, anchor=CENTER)
        self.heading.column("Column 3", width=2, minwidth=2, anchor=CENTER)
        self.heading.column("Column 4", width=2, minwidth=2, anchor=CENTER)
        self.heading.column("Column 5", width=10, minwidth=10, anchor=CENTER)
        self.heading.column("Column 6", width=50, minwidth=50, anchor=CENTER)

        self.heading.heading("#0", text="IdBook", anchor=CENTER)
        self.heading.heading("Column 2", text="Book Name", anchor=CENTER)
        self.heading.heading("Column 3", text="Price", anchor=CENTER)
        self.heading.heading("Column 4", text="Type", anchor=CENTER)
        self.heading.heading("Column 5", text="Author", anchor=CENTER)
        self.heading.heading("Column 6", text="Publisher", anchor=CENTER)

        readerTools = ReaderTools()
        reader = Reader()
        borrowTools = BorrowTools()

        if (self.idReaderEntry.get() != None and self.idReaderEntry.get() != ""):
            reader.setIdReader(self.idReaderEntry.get())
        else :
            messagebox.showinfo("Please Enter the ID Reader ","Please Enter the ID Reader")
            return
        
        readerlist = readerTools.ReaderDataId(reader.getIdReader())
        booklist = borrowTools.BookData(reader.getIdReader())

        # Check the ID Reader
        if (len(readerlist) == 0):
            messagebox.showinfo("Error in ID Reader","Please Enter the Correct ID Reader")
            return

        else:
        
            for row in readerlist:
                self.nameReader['text'] = row[1]
                self.position['text'] = row[2]
                self.gender['text'] = row[3]
                self.password['text'] = row[4]

            for row in booklist:
                row_index = booklist.index(row) + 1
                temp = Book()
                temp.setAll(row)
                self.heading.insert("", row_index, text="%s" % temp.getIdBook(), values=("%s" % temp.getNameBook(), "%d" % temp.getPrice(), "%s" % temp.getType(), "%s" % temp.getAuthor(), "%s" % temp.getPublisher()), tags=('Data',))
                self.heading.tag_configure('Data', font=("Cascadia Code SemiBold", 9))

        self.vsb = ttk.Scrollbar(self.content_frame,orient="vertical", command=self.heading.yview)
        self.vsb.place(relx=0.65, rely=0.35, relheight=0.45)

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
        self.content_frame.place(relx=0.3, rely=0.2, relwidth=1, relheight=0.8)

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

        self.nav_button1 = ttk.Button(self.nav_frame, text="User Register", style="Nav.TButton", command=self.Open_Reader_RegisterFrame)
        self.nav_button1.place(relx=0.25, rely=0.05, relwidth=0.5)
        self.nav_button2 = ttk.Button(self.nav_frame, text="Book Regsiter", style="Nav.TButton", command=self.Open_Book_RegisterFrame)
        self.nav_button2.place(relx=0.25, rely=0.25, relwidth=0.5)
        self.nav_button3 = ttk.Button(self.nav_frame, text="User Manage", style="Nav.TButton", command=self.Open_Reader_ManagementFrame)
        self.nav_button3.place(relx=0.25, rely=0.45, relwidth=0.5)
        self.nav_button4 = ttk.Button(self.nav_frame, text="Book Manage", style="Nav.TButton", command=self.Open_Book_ManagementFrame)
        self.nav_button4.place(relx=0.25, rely=0.65, relwidth=0.5)
        self.nav_button5 = ttk.Button(self.nav_frame, text="Lending Manage", style="Nav.TButton", command=self.Open_Lending_ManegementFrame)
        self.nav_button5.place(relx=0.25, rely=0.85, relwidth=0.5)

        self.idReaderLabel = ttk.Label(self.content_frame, text="ID Reader :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.idReaderLabel.place(relx=0.2, rely=0.01)

        self.idReaderEntry = ttk.Entry(self.content_frame, font=("Cascadia Code SemiBold", 14))
        self.idReaderEntry.place(relx=0.36, rely=0.02, relwidth=0.15)

        self.nameReaderLabel = ttk.Label(self.content_frame, text="Name :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.nameReaderLabel.place(relx=0.1, rely=0.11)

        self.nameReader = ttk.Label(self.content_frame, text="", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.nameReader.place(relx=0.2, rely=0.11)

        self.positionLabel = ttk.Label(self.content_frame, text="Position :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.positionLabel.place(relx=0.35, rely=0.11)

        self.position = ttk.Label(self.content_frame, text="", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.position.place(relx=0.5,rely=0.11)

        self.genderLabel = ttk.Label(self.content_frame, text="Gender :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.genderLabel.place(relx=0.072, rely=0.21)

        self.gender = ttk.Label(self.content_frame, text="", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.gender.place(relx=0.2, rely=0.21)

        self.passwordLabel = ttk.Label(self.content_frame, text="Password :", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.passwordLabel.place(relx=0.35, rely=0.21)

        self.password = ttk.Label(self.content_frame, text="", font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        self.password.place(relx=0.5, rely=0.21)

        self.content = ttk.Frame(self.content_frame)
        self.content.place(relx=0.05, rely=0.35, relwidth=0.6, relheight=0.45)

        self.inquireButton = ttk.Button(self.content_frame, text="Inquire", style="Nav.TButton", command=self.show_data)
        self.inquireButton.place(relx=0.45, rely=0.85)

        self.root.mainloop()

#Needed to Modify
class UpdateBook_Frame :

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

        self.idBookLabel = ttk.Label(self.content_frame, text="Book ID :", font=("Cascadia Code SemiBold", 9), style="Content.TLabel")
        self.idBookLabel.place(relx=0.23, rely=0.05)

        self.idBookEntry = ttk.Label(self.content_frame, text="%s" % Book_ManegementFrame.idbook, font=("Cascadia Code", 9), style="Content.TLabel")
        self.idBookEntry.place(relx=0.37, rely=0.06)

        self.nameBookLabel = ttk.Label(self.content_frame, text="Name :", font=("Cascadia Code SemiBold", 9), style="Content.TLabel")
        self.nameBookLabel.place(relx=0.273, rely=0.15)

        self.nameBookEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 9), textvariable=self.nameBook)
        self.nameBookEntry.place(relx=0.37, rely=0.16)
        self.nameBook.set(Book_ManegementFrame.namebook)

        self.priceLabel = ttk.Label(self.content_frame, text="Price :", font=("Cascadia Code SemiBold", 9), style="Content.TLabel")
        self.priceLabel.place(relx=0.26, rely=0.25)

        self.priceEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 9), textvariable=self.price)
        self.priceEntry.place(relx=0.37, rely=0.26)
        self.price.set(Book_ManegementFrame.price)

        self.typeLabel = ttk.Label(self.content_frame, text="Type :", font=("Cascadia Code SemiBold", 9), style="Content.TLabel")
        self.typeLabel.place(relx=0.274, rely=0.35)

        self.typeEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 9), textvariable=self.type)
        self.typeEntry.place(relx=0.37, rely=0.36)
        self.type.set(Book_ManegementFrame.type)

        self.authorLabel = ttk.Label(self.content_frame, text="Author :", font=("Cascadia Code SemiBold", 9), style="Content.TLabel")
        self.authorLabel.place(relx=0.092, rely=0.5)

        self.authorEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 9), textvariable=self.author)
        self.authorEntry.place(relx=0.21, rely=0.51, relwidth=0.15)
        self.author.set(Book_ManegementFrame.author)

        self.workplaceLabel = ttk.Label(self.content_frame, text="Workplace :", font=("Cascadia Code SemiBold", 9), style="Content.TLabel")
        self.workplaceLabel.place(relx=0.38, rely=0.5)

        self.workplaceEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 9), textvariable=self.workplace)
        self.workplaceEntry.place(relx=0.54, rely=0.51, relwidth=0.15)
        self.workplace.set(Book_ManegementFrame.workplace)

        self.publisherLabel = ttk.Label(self.content_frame, text="Publisher :", font=("Cascadia Code SemiBold", 9), style="Content.TLabel")
        self.publisherLabel.place(relx=0.05, rely=0.65)

        self.publisherEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 9), textvariable=self.publisher)
        self.publisherEntry.place(relx=0.21 , rely=0.66, relwidth=0.15)
        self.publisher.set(Book_ManegementFrame.publisher)

        self.addressLabel = ttk.Label(self.content_frame, text="Address :", font=("Cascadia Code SemiBold", 9), style="Content.TLabel")
        self.addressLabel.place(relx=0.408, rely=0.65)

        self.addressEntry = ttk.Entry(self.content_frame, font=("Cascadia Code SemiBold", 9), textvariable=self.address)
        self.addressEntry.place(relx=0.54, rely=0.66, relwidth=0.15)
        self.address.set(Book_ManegementFrame.address)

        self.updateButton = ttk.Button(self.content_frame, text="Update", style="Nav.TButton")
        self.updateButton.place(relx=0.35, rely=0.8)

        self.root.mainloop()





if __name__ == "__main__":

    class LoginFrame:
        def __init__(self):
            self.nameUser = "root"

    frame = Login_LibrarianFrame(LoginFrame())
