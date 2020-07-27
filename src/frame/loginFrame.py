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
        
    def loginFrame(self):

        def CloseFrame():
            root.destroy()
        
        #Function for button to Unshow/Show Password
        def show_password():
            if Show_Button.cget('image') == ('pyimage2',):
                Show_Button.config(image=unlock)
                Password.config(show="")
            else :
                Show_Button.config(image=button_image)
                Password.config(show="*")

        #Function to check login to next Frame
        def check_login():
            if (var.get() == 1):
                rTools = ReaderTools()
                reader = Reader()
                reader.setIdReader(Username.get())
                reader.setPassword(Password.get())

                if ((Username.get() != None) and (not(reader.equals("",Username.get()))) and (Password.get() != None) and (not(reader.equals("",Password.get())))):
                    whether_login = rTools.ReaderLogin(reader.getIdReader(), reader.getPassword())
                    nameReader = (rTools.ReaderDataId(reader.getIdReader())[0][1])
                    if(whether_login == True):
                        idReader = reader.getIdReader()
                        
                        frame = Login_ReaderFrame()
                        CloseFrame()
                    else :
                        messagebox.showinfo("用户名或密码错误", "用户名或密码错误")
                else :
                    messagebox.showinfo("请填写用户名和密码", "请填写用户名和密码")
            elif (var.get() == 2):
                libTools = LibrarianTools()
                lib = Librarian()
                lib.setNameUser(Username.get())
                lib.setPassword(Password.get())

                if ((Username.get() != None) and (not(lib.equals("", Username.get()))) and (Password.get() != None) and (not(lib.equals("", Password.get())))):
                    whether_login = libTools.LibrarianLogin(lib.getNameUser(),lib.getPassword())
                    if (whether_login == True):
                        nameUser = lib.getNameUser()

                        frame = Login_LibrarianFrame()
                        CloseFrame()
                    else:
                        messagebox.showinfo("用户名或密码错误", "用户名或密码错误")
                else:
                    messagebox.showinfo("请填写用户名和密码", "请填写用户名和密码")
            return None

        root = Tk()

        #Setting the Title
        root.title("Library Management System")

        #Setting the icon
        root.iconbitmap('src\\picture\\library.ico')

        #Get the screen resolution
        x = root.winfo_screenwidth()
        y = root.winfo_screenheight()

        #Get the value for windows size
        x1 = x * (2/9)
        y1 = y * (7/11)

        #Get the value for Starting point for windows
        x2 = x * (2/5)
        y2 = y * (1/7)

        root.geometry("%dx%d+%d+%d" % (x1, y1, x2, y2))
        root.resizable(False, False)

        #Easy for configure within attribute
        x1 = int(x1)
        y1 = int(y1)

        #Setting Radio Button Variable
        var = IntVar() # 1 for Reader , 2 for Librarian

        #Setting Style for ttk
        style = ttk.Style()
        style.configure("BW.TLabel", foreground="black", background="MediumPurple1")
        style.configure("BL.Label", foreground="black", background="MediumPurple2")

        background_image = Image.open("src\\picture\\Mac.jpeg")
        background_image = background_image.resize((x1, y1), Image.ANTIALIAS)
        background_image = ImageTk.PhotoImage(background_image)
        background_label = Canvas(root, width=x, height=y)
        background_label.pack()
        background_label.create_image(0, 0, anchor=NW, image=background_image)

        frame_top = ttk.Frame(root, style="BW.TLabel")
        frame_top.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.15)
        title = ttk.Label(frame_top, text="Library Management System", padding="2 5 2 10", font=("Cascadia Code SemiBold", 14), style="BW.TLabel")
        title2 = ttk.Label(frame_top, text="Login to access your account", padding="0 0 0 0", font=("Cascadia Code", 13), style="BL.Label")
        title.pack()
        title2.pack()

        login_frame = ttk.Frame(root, relief=GROOVE)
        login_frame.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.45)

        Name_label = ttk.Label(login_frame, text="Name :", font=("Cascadia Code", 12))
        Username = ttk.Entry(login_frame, font=("Cascadia Code", 10))
        Name_label.place(relx=0.03, rely=0.125)
        Username.place(relx=0.36, rely=0.140, relwidth=0.55)

        Password_label = ttk.Label(
        login_frame, text="Password :", font=("Cascadia Code", 11))
        Password = ttk.Entry(login_frame, font=("Cascadia Code", 10), show="*")

        #Setting Lock Button Image
        button_image = Image.open("src\\picture\\lock.png")
        button_image = button_image.resize((16, 16), Image.ANTIALIAS)
        button_image = ImageTk.PhotoImage(button_image)

        #Setting Unlock Button Image
        unlock = Image.open("src\\picture\\unlock.png")
        unlock = unlock.resize((16, 16), Image.ANTIALIAS)
        unlock = ImageTk.PhotoImage(unlock)

        Show_Button = ttk.Button(login_frame, image=button_image, command=show_password)

        Password_label.place(relx=0.03, rely=0.375)
        Password.place(relx=0.36, rely=0.385, relwidth=0.43)
        Show_Button.place(relx=0.81, rely=0.375, relwidth=0.1)

        type_Frame = ttk.Frame(login_frame, relief=GROOVE)
        type_Frame.place(relx=0.1, rely=0.57, relwidth=0.8, relheight=0.1)
        readerRadioButton = Radiobutton(type_Frame, text = "Reader", variable = var, value = 1, font=("Cascadia Code", 9))
        librarianRadioButton = Radiobutton(type_Frame, text = "Librarian", variable = var, value = 2, font=("Cascadia Code", 9))
        librarianRadioButton.select()
        readerRadioButton.place(relx=0.58, rely=0.15, relheight=0.6)
        librarianRadioButton.place(relx=0.08, rely=0.15, relheight=0.6)


        button_frame = ttk.Frame(login_frame, relief=GROOVE)
        button_frame.place(relx=0.1, rely=0.73, relwidth=0.8, relheight=0.2)
        button_login = ttk.Button(button_frame, text="Login", command=check_login)
        button_clear = ttk.Button(button_frame, text="Clear")
        button_login.place(relx=0.55, rely=0.25, relwidth=0.4)
        button_clear.place(relx=0.05, rely=0.25, relwidth=0.4)

        root.mainloop()
