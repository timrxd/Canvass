__author__ = 'Tim'

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *


class ScrollFrame(Frame):
    def __init__(self, root, data=""):

        Frame.__init__(self, root)
        self.canvas = Canvas(root, borderwidth=0, background="white")
        self.frame = Frame(self.canvas, background="white")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

    def onFrameConfigure(self, event):
        # Reset the scroll region to encompass the inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.frame.grid_columnconfigure(0, minsize=self.canvas.winfo_width()*0.35)
        self.frame.grid_columnconfigure(1, minsize=self.canvas.winfo_width()*0.1)
        self.frame.grid_columnconfigure(2, minsize=self.canvas.winfo_width()*0.1)
        self.frame.grid_columnconfigure(3, minsize=self.canvas.winfo_width()*0.35)
        self.frame.grid_columnconfigure(4, minsize=self.canvas.winfo_width()*0.1)
