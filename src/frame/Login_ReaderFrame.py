from tkinter import Tk
from tkinter import ttk
from tkinter import *
from ttkthemes import ThemedTk
from PIL import ImageTk, Image

from importlib import reload

from ..model.Book import *
from ..sqlTools.BookTools import *
from ..sqlTools.BorrowTools import *

import sys
reload(sys.modules["src.frame.loginFrame"]) #Cancel the Circular Import and get back to last module
from ..frame.loginFrame import LoginFrame

class Login_ReaderFrame:
    def __init__(self):

        def Open_Search_BookFrame():
            CloseFrame()
            frame = Search_BookFrame()

        def Open_Return_BookFrame():
            CloseFrame()
            frame = Return_BookFrame()

        def Logout():
            CloseFrame()
            frame = LoginFrame()
            frame.loginFrame()

        def CloseFrame():
            root.destroy()
            
        root = ThemedTk(theme="equilux")

        #Setting the Title
        root.title("Library Management System")

        #Setting the icon
        root.iconbitmap('src\\picture\\library.ico')

        #Get the screen resolution
        x = root.winfo_screenwidth()
        y = root.winfo_screenheight()

        #Get the value for windows size
        x1 = x * (13/20)
        y1 = y * (0.81)

        #Get the value for Starting point for windows
        x2 = x * (1.1/6)
        y2 = y * (1/12)

        root.geometry("%dx%d+%d+%d" % (x1, y1, x2, y2))
        root.resizable(False, False)

        #Easy for configure within attribute
        x1 = int(x1)
        y1 = int(y1)

        x_content = int(x1*0.7)
        y_content = int(y1*0.8)

        x_nav = int(x1*0.3)
        y_nav = int(y1*0.8)

        style = ttk.Style()
        style.configure("Title.TLabel", foreground="snow")
        style.configure("Logout.TButton", font=("Cascadia Code SemiBold", 14))
        style.configure("Nav.TButton", font=("Cascadia Code SemiBold", 12))
        style.configure("Content.TFrame", foreground="black", background="LightSkyBlue2")
        style.configure("Nav.TFrame",foreground="black", background="SeaGreen1")
        
        title_frame = ttk.Frame(root)
        title_frame.place(relwidth=1, relheight=0.2)

        text_frame = ttk.Frame(title_frame)
        text_frame.place(relx=0.1,rely=0.5, relwidth=0.4, relheight=0.5)

        title_text = ttk.Label(text_frame,text="Library Management System",font=("Cascadia Code SemiBold", 18), style="Title.TLabel")
        title_text.place(relx=0.05,rely=0.4)

        logout_button = ttk.Button(title_frame,text="Logout", style="Logout.TButton", command=Logout)
        logout_button.place(relx=0.78,rely=0.58,relwidth=0.15)

        content_frame = ttk.Frame(root, style="Content.TFrame")
        content_frame.place(relx=0.3,rely=0.2,relwidth=0.7,relheight=0.8)

        nav_frame = ttk.Frame(root, style="Nav.TFrame")
        nav_frame.place(rely=0.2,relwidth=0.3,relheight=0.8)
        
        #Resize the Image
        Nav_image = Image.open("src\\picture\\Nav.jpg")
        Nav_image = Nav_image.resize((x_nav, y_nav), Image.ANTIALIAS)
        Nav_image = ImageTk.PhotoImage(Nav_image)

        # (highlightthickness = 0) is for remove the border for the Canvas 
        Nav_label = Canvas(nav_frame, width=x_nav, height=y_nav, highlightthickness=0)
        Nav_label.pack()
        Nav_label.create_image(0, 0, anchor=NW, image=Nav_image)

        nav_button1 = ttk.Button(nav_frame, text="Check Out", style="Nav.TButton", command=Open_Search_BookFrame)
        nav_button1.place(relx=0.275,rely=0.2,relwidth=0.45)
        nav_button2 = ttk.Button(nav_frame, text="Check In", style="Nav.TButton", command=Open_Return_BookFrame)
        nav_button2.place(relx=0.275, rely=0.6, relwidth=0.45)

        root.mainloop()


class Return_BookFrame:
    def __init__(self):

        def Open_Search_BookFrame():
            CloseFrame()
            frame = Search_BookFrame()

        def Open_Return_BookFrame():
            CloseFrame()
            frame = Return_BookFrame()

        def Logout():
            CloseFrame()
            frame = LoginFrame()
            frame.loginFrame()

        def CloseFrame():
            root.destroy()

        root = ThemedTk(theme="equilux")

        #Setting the Title
        root.title("Library Management System")

        #Setting the icon
        root.iconbitmap('src\\picture\\library.ico')

        #Get the screen resolution
        x = root.winfo_screenwidth()
        y = root.winfo_screenheight()

        #Get the value for windows size
        x1 = x * (13/20)
        y1 = y * (0.81)

        #Get the value for Starting point for windows
        x2 = x * (1.1/6)
        y2 = y * (1/12)

        root.geometry("%dx%d+%d+%d" % (x1, y1, x2, y2))
        root.resizable(False, False)

        #Easy for configure within attribute
        x1 = int(x1)
        y1 = int(y1)

        x_content = int(x1*0.7)
        y_content = int(y1*0.8)

        x_nav = int(x1*0.3)
        y_nav = int(y1*0.8)

        style = ttk.Style()
        style.configure("Title.TLabel", foreground="snow")
        style.configure("Logout.TButton", font=("Cascadia Code SemiBold", 14))
        style.configure("Nav.TButton", font=("Cascadia Code SemiBold", 12))
        style.configure("Content.TFrame", foreground="black",
                        background="LightSkyBlue2")
        style.configure("Nav.TFrame", foreground="black", background="SeaGreen1")

        title_frame = ttk.Frame(root)
        title_frame.place(relwidth=1, relheight=0.2)

        text_frame = ttk.Frame(title_frame)
        text_frame.place(relx=0.1, rely=0.5, relwidth=0.4, relheight=0.5)

        title_text = ttk.Label(text_frame, text="Library Management System", font=("Cascadia Code SemiBold", 18), style="Title.TLabel")
        title_text.place(relx=0.05, rely=0.4)

        logout_button = ttk.Button(title_frame, text="Logout", style="Logout.TButton", command=Logout)
        logout_button.place(relx=0.78, rely=0.58, relwidth=0.15)

        content_frame = ttk.Frame(root, style="Content.TFrame")
        content_frame.place(relx=0.3, rely=0.2, relwidth=0.7, relheight=0.8)

        nav_frame = ttk.Frame(root, style="Nav.TFrame")
        nav_frame.place(rely=0.2, relwidth=0.3, relheight=0.8)

        #Resize the Image
        Nav_image = Image.open("src\\picture\\Nav.jpg")
        Nav_image = Nav_image.resize((x_nav, y_nav), Image.ANTIALIAS)
        Nav_image = ImageTk.PhotoImage(Nav_image)

        # (highlightthickness = 0) is for remove the border for the Canvas
        Nav_label = Canvas(nav_frame, width=x_nav,
                           height=y_nav, highlightthickness=0)
        Nav_label.pack()
        Nav_label.create_image(0, 0, anchor=NW, image=Nav_image)

        nav_button1 = ttk.Button(
            nav_frame, text="Check Out", style="Nav.TButton", command=Open_Search_BookFrame)
        nav_button1.place(relx=0.275, rely=0.2, relwidth=0.45)
        nav_button2 = ttk.Button(
            nav_frame, text="Check In", style="Nav.TButton", command=Open_Return_BookFrame)
        nav_button2.place(relx=0.275, rely=0.6, relwidth=0.45)

        root.mainloop()


class Search_BookFrame:

    def __init__(self):

        def show_data():
            heading = ttk.Treeview(content)

            #Creating Columns
            heading['columns'] = ("Column 2", "Column 3","Column 4", "Column 5", "Column 6", "Column 7")
            heading.column("#0", width=5, minwidth=5, anchor=CENTER)
            heading.column("Column 2", width=60, minwidth=60, anchor=CENTER)
            heading.column("Column 3", width=2, minwidth=2, anchor=CENTER)
            heading.column("Column 4", width=2, minwidth=2, anchor=CENTER)
            heading.column("Column 5", width=10, minwidth=10, anchor=CENTER)
            heading.column("Column 6", width=50, minwidth=50, anchor=CENTER)
            heading.column("Column 7", width=80, minwidth=80, anchor=CENTER)

            heading.heading("#0", text="IdBook", anchor=CENTER)
            heading.heading("Column 2", text="Book Name", anchor=CENTER)
            heading.heading("Column 3", text="Price", anchor=CENTER)
            heading.heading("Column 4", text="Type", anchor=CENTER)
            heading.heading("Column 5", text="Author", anchor=CENTER)
            heading.heading("Column 6", text="Publisher", anchor=CENTER)
            heading.heading("Column 7", text="Whether In Stock", anchor=CENTER)

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
                else :
                    whetherInStock = "No"
                heading.insert("",row_index, text="%s" % temp.getIdBook(), values=("%s" % temp.getNameBook(),"%d" % temp.getPrice(),"%s" % temp.getType(),"%s" % temp.getAuthor(),"%s" % temp.getPublisher(),"%s" % whetherInStock), tags=('Data',))
            
            heading.tag_configure('Data', font=("Cascadia Code SemiBold", 9))

            heading.pack(side=TOP,fill=X)


        def Open_Search_BookFrame():
            CloseFrame()
            frame = Search_BookFrame()

        def Open_Return_BookFrame():
            CloseFrame()
            frame = Return_BookFrame()

        def Logout():
            CloseFrame()
            frame = LoginFrame()
            frame.loginFrame()

        def CloseFrame():
            root.destroy()

        root = ThemedTk(theme="equilux")

        #Setting the Title
        root.title("Library Management System")

        #Setting the icon
        root.iconbitmap('src\\picture\\library.ico')

        #Get the screen resolution
        x = root.winfo_screenwidth()
        y = root.winfo_screenheight()

        #Get the value for windows size
        x1 = x * (13/20)
        y1 = y * (0.81)

        #Get the value for Starting point for windows
        x2 = x * (1.1/6)
        y2 = y * (1/12)

        root.geometry("%dx%d+%d+%d" % (x1, y1, x2, y2))
        root.resizable(False, False)

        #Easy for configure within attribute
        x1 = int(x1)
        y1 = int(y1)

        x_content = int(x1*0.7)
        y_content = int(y1*0.8)

        x_nav = int(x1*0.3)
        y_nav = int(y1*0.8)

        style = ttk.Style()
        style.configure("Title.TLabel", foreground="snow")
        style.configure("Logout.TButton", font=("Cascadia Code SemiBold", 14))
        style.configure("Nav.TButton", font=("Cascadia Code SemiBold", 12))
        style.configure("Content.TFrame", foreground="black", background="LightSkyBlue2")
        style.configure("Content.TLabel", foreground="black", background="LightSkyBlue2")
        style.configure("Nav.TFrame", foreground="black", background="SeaGreen1")
        style.configure("Treeview.Heading", font=("Cascadia Code SemiBold", 9))

        title_frame = ttk.Frame(root)
        title_frame.place(relwidth=1, relheight=0.2)

        text_frame = ttk.Frame(title_frame)
        text_frame.place(relx=0.1, rely=0.5, relwidth=0.4, relheight=0.5)

        title_text = ttk.Label(text_frame, text="Library Management System", font=("Cascadia Code SemiBold", 18), style="Title.TLabel")
        title_text.place(relx=0.05, rely=0.4)

        logout_button = ttk.Button(title_frame, text="Logout", style="Logout.TButton", command=Logout)
        logout_button.place(relx=0.78, rely=0.58, relwidth=0.15)

        content_frame = ttk.Frame(root, style="Content.TFrame")
        content_frame.place(relx=0.3, rely=0.2, relwidth=0.7, relheight=0.8)

        search_label = ttk.Label(content_frame, text="Book Name Searching",font=("Cascadia Code SemiBold", 18), style="Content.TLabel")
        search_label.place(relx=0.3)

        search_bar = ttk.Entry(content_frame, font=("Cascadia Code", 16))
        search_bar.place(relx=0.1, rely=0.15, relwidth=0.6)

        search_button = ttk.Button(content_frame, text="Search", style="Nav.TButton")
        search_button.place(relx=0.75 , rely=0.15, relwidth=0.149)

        content = ttk.Frame(content_frame)
        content.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

        show_data()

        borrow_button = ttk.Button(content_frame, text="Borrow", style="Nav.TButton")
        borrow_button.place(relx=0.65, rely = 0.85)

        nav_frame = ttk.Frame(root, style="Nav.TFrame")
        nav_frame.place(rely=0.2, relwidth=0.3, relheight=0.8)

        #Resize the Image
        Nav_image = Image.open("src\\picture\\Nav.jpg")
        Nav_image = Nav_image.resize((x_nav, y_nav), Image.ANTIALIAS)
        Nav_image = ImageTk.PhotoImage(Nav_image)

        # (highlightthickness = 0) is for remove the border for the Canvas
        Nav_label = Canvas(nav_frame, width=x_nav, height=y_nav, highlightthickness=0)
        Nav_label.pack()
        Nav_label.create_image(0, 0, anchor=NW, image=Nav_image)

        nav_button1 = ttk.Button(nav_frame, text="Check Out", style="Nav.TButton", command=Open_Search_BookFrame)
        nav_button1.place(relx=0.275, rely=0.2, relwidth=0.45)
        nav_button2 = ttk.Button(nav_frame, text="Check In", style="Nav.TButton", command=Open_Return_BookFrame)
        nav_button2.place(relx=0.275, rely=0.6, relwidth=0.45)

        root.mainloop()

if __name__ == "__main__":
    frame = Login_ReaderFrame()
