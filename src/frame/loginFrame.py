from tkinter import Tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

from ..frame.Login_ReaderFrame import *
from ..frame.Login_LibrarianFrame import *

from ..model.Librarian import *
from ..model.Reader import *
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
