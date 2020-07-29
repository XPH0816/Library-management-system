from tkinter import Tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

class Login_ReaderFrame:
    def __init__(self):
        root = Tk()

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

        root.mainloop()

if __name__ == "__main__":
    frame = Login_ReaderFrame()