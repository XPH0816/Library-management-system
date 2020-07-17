from tkinter import Tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk,Image

def loginFrame():
    root = Tk()

    #Setting the Title
    root.title("Library Management System")

    #Setting the icon
    root.iconbitmap('src\picture\library.ico')
    
    #Get the screen resolution
    x = root.winfo_screenwidth()
    y = root.winfo_screenheight()

    #Get the value for windows size 
    x1 = x * (2/9)
    y1 = y * (7/11)

    #Get the value for Starting point for windows
    x2 = x * (2/5)
    y2 = y * (1/7)

    root.geometry("%dx%d+%d+%d" % (x1,y1,x2,y2))
    root.resizable(False,False)

    #easy for configure within attribute
    x1 = int(x1)
    y1 = int(y1)

    #Setting Style for ttk
    style = ttk.Style()
    style.configure("BW.TLabel", foreground="black", background="DarkOrchid1")
    style.configure("BL.Label", foreground="black", background="DarkOrchid2")
    

    background_image = Image.open("src\picture\Mac.jpeg")
    background_image = background_image.resize((x1, y1), Image.ANTIALIAS)
    background_image = ImageTk.PhotoImage(background_image)
    background_label = Canvas(root, width=x, height=y)
    background_label.pack()
    background_label.create_image(0, 0, anchor=NW, image=background_image)

    frame_top = ttk.Frame(root,style = "BW.TLabel")
    frame_top.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.15)
    title = ttk.Label(frame_top, text="Library Management System", padding = "2 5 2 10", font=("Cascadia Code SemiBold", 14),style = "BW.TLabel")
    title2 = ttk.Label(frame_top, text="Login to access your account", padding = "0 0 0 0", font=("Cascadia Code", 13),style = "BL.Label")
    title.pack()
    title2.pack()

    login_frame = ttk.Frame(root, relief = GROOVE)
    login_frame.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.35)

    Name_label = ttk.Label(login_frame, text = "Name :",font=("Cascadia Code" , 12))
    Username = ttk.Entry(login_frame)
    Name_label.place(relx=0.145, rely=0.125)
    Username.place(relx=0.36, rely=0.140, relwidth=0.55)

    Password_label = ttk.Label(login_frame,text = "Password :",font=("Cascadia Code" , 11))
    Password = ttk.Entry(login_frame,show="*")

    button_image = Image.open("src\picture\lock.png")
    button_image = button_image.resize((16, 16), Image.ANTIALIAS)
    button_image = ImageTk.PhotoImage(button_image)
    Show_Button = ttk.Button(login_frame, image = button_image)

    Password_label.place(relx=0.03, rely=0.375)
    Password.place(relx=0.36, rely=0.385, relwidth=0.43)
    Show_Button.place(relx=0.81, rely=0.375, relwidth=0.1)

    button_frame = ttk.Frame(login_frame, relief = GROOVE)
    button_frame.place(relx=0.1,rely=0.63, relwidth=0.8, relheight=0.25)
    button_login = ttk.Button(button_frame, text = "Login")
    button_clear = ttk.Button(button_frame, text = "Clear")
    button_login.place(relx=0.55, rely=0.25, relwidth=0.4)
    button_clear.place(relx=0.05, rely=0.25, relwidth=0.4)
    

    root.mainloop()

loginFrame()
