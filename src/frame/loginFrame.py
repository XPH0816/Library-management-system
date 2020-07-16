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

    background_image = Image.open("src\picture\Mac.jpeg")
    background_image = background_image.resize((x1, y1), Image.ANTIALIAS)
    background_image = ImageTk.PhotoImage(background_image)
    background_label = Canvas(root, width=x, height=y)
    background_label.pack()
    background_label.create_image(0, 0, anchor=NW, image=background_image)

    frame_top = ttk.Frame(root)
    frame_top.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.15)
    title = ttk.Label(frame_top, text="Library Management System", padding = "2 5 2 0", font=("Cascadia Code SemiBold", 14))
    title2 = ttk.Label(frame_top, text="Login to access your account", padding = "0 10 0 0", font=("Cascadia Code", 13))
    title.pack()
    title2.pack()

    login_frame = ttk.Frame(root, relief = GROOVE)
    login_frame.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.55)

    

    

    root.mainloop()

loginFrame()
