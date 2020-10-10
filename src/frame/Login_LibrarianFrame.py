from tkinter import Tk
from tkinter import ttk
from tkinter import *
from ttkthemes import ThemedTk
from PIL import ImageTk, Image

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
        self,frame = Lending_ManagementFrame(self.LoginFrame)

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

        self.style = ttk.Style()
        self.style.configure("Title.TLabel", foreground="snow")
        self.style.configure("Logout.TButton", font=(
            "Cascadia Code SemiBold", 14))
        self.style.configure("Nav.TButton", font=(
            "Cascadia Code SemiBold", 12))
        self.style.configure(
            "Content.TFrame", foreground="black", background="LightSkyBlue2")
        self.style.configure(
            "Nav.TFrame", foreground="black", background="SeaGreen1")

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
        self.Nav_image = self.Nav_image.resize(
            (self.x_nav, self.y_nav), Image.ANTIALIAS)
        self.Nav_image = ImageTk.PhotoImage(self.Nav_image)

        # (highlightthickness = 0) is for remove the border for the Canvas
        self.Nav_label = Canvas(
            self.nav_frame, width=self.x_nav, height=self.y_nav, highlightthickness=0)
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

        self.root.geometry("%dx%d+%d+%d" %
                           (self.x1, self.y1, self.x2, self.y2))
        self.root.resizable(False, False)

        #Easy for configure within attribute
        self.x1 = int(self.x1)
        self.y1 = int(self.y1)

        self.x_nav = int(self.x1*0.3)
        self.y_nav = int(self.y1*0.8)

        self.style = ttk.Style()
        self.style.configure("Title.TLabel", foreground="snow")
        self.style.configure("Logout.TButton", font=(
            "Cascadia Code SemiBold", 14))
        self.style.configure("Nav.TButton", font=(
            "Cascadia Code SemiBold", 12))
        self.style.configure(
            "Content.TFrame", foreground="black", background="LightSkyBlue2")
        self.style.configure(
            "Nav.TFrame", foreground="black", background="SeaGreen1")

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
        self.Nav_image = self.Nav_image.resize(
            (self.x_nav, self.y_nav), Image.ANTIALIAS)
        self.Nav_image = ImageTk.PhotoImage(self.Nav_image)

        # (highlightthickness = 0) is for remove the border for the Canvas
        self.Nav_label = Canvas(
            self.nav_frame, width=self.x_nav, height=self.y_nav, highlightthickness=0)
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

        self.style = ttk.Style()
        self.style.configure("Title.TLabel", foreground="snow")
        self.style.configure("Logout.TButton", font=(
            "Cascadia Code SemiBold", 14))
        self.style.configure("Nav.TButton", font=(
            "Cascadia Code SemiBold", 12))
        self.style.configure(
            "Content.TFrame", foreground="black", background="LightSkyBlue2")
        self.style.configure(
            "Nav.TFrame", foreground="black", background="SeaGreen1")

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
        self.Nav_image = self.Nav_image.resize(
            (self.x_nav, self.y_nav), Image.ANTIALIAS)
        self.Nav_image = ImageTk.PhotoImage(self.Nav_image)

        # (highlightthickness = 0) is for remove the border for the Canvas
        self.Nav_label = Canvas(
            self.nav_frame, width=self.x_nav, height=self.y_nav, highlightthickness=0)
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

        self.style = ttk.Style()
        self.style.configure("Title.TLabel", foreground="snow")
        self.style.configure("Logout.TButton", font=(
            "Cascadia Code SemiBold", 14))
        self.style.configure("Nav.TButton", font=(
            "Cascadia Code SemiBold", 12))
        self.style.configure(
            "Content.TFrame", foreground="black", background="LightSkyBlue2")
        self.style.configure(
            "Nav.TFrame", foreground="black", background="SeaGreen1")

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
        self.Nav_image = self.Nav_image.resize(
            (self.x_nav, self.y_nav), Image.ANTIALIAS)
        self.Nav_image = ImageTk.PhotoImage(self.Nav_image)

        # (highlightthickness = 0) is for remove the border for the Canvas
        self.Nav_label = Canvas(
            self.nav_frame, width=self.x_nav, height=self.y_nav, highlightthickness=0)
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

if __name__ == "__main__":
    frame = Login_LibrarianFrame()
