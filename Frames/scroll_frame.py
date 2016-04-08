__author__ = 'Tim'

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
import math


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

        self.frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    # TODO: Make this a dynamic configure, take in array of ints to set minsize, remove extra cols? from init?
    def on_frame_configure(self, event):
        # Reset the scroll region to encompass the inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.frame.grid_columnconfigure(0, minsize=self.canvas.winfo_width()*0.35)
        self.frame.grid_columnconfigure(1, minsize=self.canvas.winfo_width()*0.1)
        self.frame.grid_columnconfigure(2, minsize=self.canvas.winfo_width()*0.1)
        self.frame.grid_columnconfigure(3, minsize=self.canvas.winfo_width()*0.35)
        self.frame.grid_columnconfigure(4, minsize=self.canvas.winfo_width()*0.1)

    # Test on linux w/ mouse
    # TODO: On mac, remove 'divide by 120'
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(math.floor(-1*(event.delta/120)), "units")