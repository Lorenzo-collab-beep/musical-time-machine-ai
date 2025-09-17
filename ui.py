from tkinter import Tk, PhotoImage
import os

_TITLE_ = "musical-time-machine-ai"
_ICON_ = "icon/note.png"
_GEOMETRY_ = "400x400"

class Window:

    def __init__(self):
        self.tk = Tk()
        self.tk.config(padx=20, pady=20)
        self.tk.geometry(_GEOMETRY_)
        self.tk.title(_TITLE_)

        root = self.tk.winfo_toplevel()
        root.resizable(False, False)

        if os.path.exists(_ICON_):
            icon = PhotoImage(file=_ICON_)
            root.iconphoto(True, icon)


    def mainloop(self):
        self.tk.mainloop()

    def root(self):
        return self.tk
