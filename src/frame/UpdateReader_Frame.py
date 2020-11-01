from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from ttkthemes import ThemedTk

from ..model.Reader import Reader

from ..sqlTools.ReaderTools import ReaderTools

class UpdateReader_Frame:

    def do_updateReader(self):
        
        readerTools = ReaderTools()
        reader = Reader()

        if self.idReaderEntry['text'] != None and self.idReaderEntry['text'] != "" and self.nameReaderEntry.get() != None and self.nameReaderEntry.get() != "" and self.positionEntry.get() != None and self.positionEntry.get() != "" and self.sexEntry.get() != None and self.sexEntry.get() != "" and self.passwordEntry.get() != None and self.passwordEntry.get() != "" :
            reader.setIdReader(self.idReaderEntry['text'])
            reader.setNameReader(self.nameReaderEntry.get())
            reader.setLevel(self.positionEntry.get())
            reader.setSex(self.sexEntry.get())
            reader.setPassword(self.passwordEntry.get())

            i = readerTools.UpdateReader(reader)

            if i == 1 :
                messagebox.showinfo("Sucessfully Update", "Sucessfully Update The Reader Infomation")
                MsgBox = messagebox.askquestion('Continue','Are you sure you want to Continue', icon = 'info')
                if MsgBox == 'yes' :
                    self.root.destroy()
                return
            else :
                messagebox.showinfo("Failed to Update", "Failed to Update The Reader Infomation")
                MsgBox = messagebox.askquestion('Continue', 'Are you sure you want to Continue', icon='info')
                if MsgBox == 'yes':
                    self.root.destroy()
                return
        else :
            messagebox.showinfo("Please Enter the Infomation","Please Enter the Infomation") 



    def __init__(self, Reader_ManagementFrame):
        
        self.root = ThemedTk(theme="equilux")

        #Setting the Title
        self.root.title("Library Management System")

        #Setting the icon
        self.root.iconbitmap('src\\picture\\library.ico')

        #Get the screen resolution
        self.x = self.root.winfo_screenwidth()
        self.y = self.root.winfo_screenheight()

        #Get the value for windows size
        self.x1 = self.x * (3/10)
        self.y1 = self.y * (4/11)

        #Get the value for Starting point for windows
        self.x2 = self.x * (4/11)
        self.y2 = self.y * (2/9)

        self.root.geometry("%dx%d+%d+%d" % (self.x1, self.y1, self.x2, self.y2))
        self.root.resizable(False, False)

        #Easy for configure within attribute
        self.x1 = int(self.x1)
        self.y1 = int(self.y1)

        #Setting Entry variable
        self.nameReader = StringVar()
        self.position = StringVar()
        self.sex = StringVar()
        self.password = StringVar()

        self.style = ttk.Style()
        self.style.configure("Title.TLabel", foreground="snow")
        self.style.configure("Nav.TButton", font=("Cascadia Code SemiBold", 12))
        self.style.configure("Content.TFrame", foreground="black", background="LightSkyBlue2")
        self.style.configure("Content.TLabel", foreground="black", background="LightSkyBlue2")
        self.style.configure("Nav.TFrame", foreground="black", background="SeaGreen1")

        self.content_frame = ttk.Frame(self.root, style="Content.TFrame")
        self.content_frame.place(relwidth=1, relheight=1)

        self.idReaderLabel = ttk.Label(self.content_frame, text="ID Reader :", font=("Cascadia Code SemiBold", 12), style="Content.TLabel")
        self.idReaderLabel.place(relx=0.2, rely=0.05)

        self.idReaderEntry = ttk.Label(self.content_frame, text="%s" % Reader_ManagementFrame.idreader, font=("Cascadia Code", 12), style="Content.TLabel")
        self.idReaderEntry.place(relx=0.45, rely=0.05)

        self.nameReaderLabel = ttk.Label(self.content_frame, text="Name :", font=("Cascadia Code SemiBold", 12), style="Content.TLabel")
        self.nameReaderLabel.place(relx=0.298, rely=0.2)

        self.nameReaderEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12), textvariable=self.nameReader)
        self.nameReaderEntry.place(relx=0.45, rely=0.2)

        self.positionLabel = ttk.Label(self.content_frame, text="Position :", font=("Cascadia Code SemiBold", 12), style="Content.TLabel")
        self.positionLabel.place(relx=0.22, rely=0.35)

        self.positionEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12), textvariable=self.position)
        self.positionEntry.place(relx=0.45, rely=0.35)

        self.sexLabel = ttk.Label(self.content_frame, text="Sex :", font=("Cascadia Code SemiBold", 12), style="Content.TLabel")
        self.sexLabel.place(relx=0.318, rely=0.5)

        self.sexEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12), textvariable=self.sex)
        self.sexEntry.place(relx=0.45, rely=0.5)

        self.passwordLabel = ttk.Label(self.content_frame, text="Password :", font=("Cascadia Code SemiBold", 12), style="Content.TLabel")
        self.passwordLabel.place(relx=0.22, rely=0.65)

        self.passwordEntry = ttk.Entry(self.content_frame, font=("Cascadia Code", 12), textvariable=self.password)
        self.passwordEntry.place(relx=0.45, rely=0.65)

        self.updateButton = ttk.Button(self.content_frame, text="Update", style="Nav.TButton", command=self.do_updateReader)
        self.updateButton.place(relx=0.4, rely=0.8)

        self.root.mainloop()