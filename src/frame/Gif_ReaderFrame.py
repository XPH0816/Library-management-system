from tkinter import Tk
from tkinter import ttk
from tkinter import *

class Gif_ReaderFrame:
    def Gif_ReaderFrame(self):
        class AnimatedGif(object):
            """ Animated GIF Image Container. """

            def __init__(self, image_file_path):
                # Read in all the frames of a multi-frame gif image.
                self._frames = []

                frame_num = 0  # Number of next frame to read.
                while True:
                    try:
                        frame = PhotoImage(file=image_file_path,format="gif -index {}".format(frame_num))
                    except TclError:
                        break
                    self._frames.append(frame)
                    frame_num += 1
            
            def __len__(self):
                return len(self._frames)

            def __getitem__(self, frame_num):
                return self._frames[frame_num]
        
        def update_label_image(label, ani_img, ms_delay, frame_num):
            global cancel_id
            label.configure(image=ani_img[frame_num])
            frame_num = (frame_num+1) % len(ani_img)
            cancel_id = root.after(ms_delay, update_label_image, label, ani_img, ms_delay, frame_num)
        
        def enable_animation():
            global cancel_id
            if cancel_id is None:  # Animation not started?
                ms_delay = 1000 // len(ani_img)  # Show all frames in 1000 ms.
                cancel_id = root.after(ms_delay, update_label_image, Label, ani_img, ms_delay, 0)

        root = Tk()

        #Setting the Title
        root.title("Library Management System")

        #Setting the icon
        root.iconbitmap('src\\picture\\library.ico')

        #Get the screen resolution
        x = root.winfo_screenwidth()
        y = root.winfo_screenheight()

        #Get the value for Starting point for windows
        x2 = x * (2/5)
        y2 = y * (1/7)

        root.geometry("%dx%d+%d+%d" % (529, 527, x2, y2))
        root.resizable(False, False)

        ani_img = AnimatedGif("src\\picture\\goodReader.gif")
        global cancel_id
        cancel_id = None

        Label = ttk.Label(image=ani_img[0])
        Label.place(relx=0.2,rely=0.1)
        enable_animation()

        root.mainloop()


