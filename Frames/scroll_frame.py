import math
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *


class ScrollFrame(Frame):
    def __init__(self, root, values=[]):

        Frame.__init__(self, root)
        self.canvas = Canvas(root, borderwidth=0, background="white", highlightthickness=0)
        self.frame = Frame(self.canvas, background="white")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True, padx=15)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.col_values = values
        self.frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    # TODO: Make this a dynamic configure, take in array of ints to set minsize, remove extra cols? from init?
    def on_frame_configure(self, event):
        # Reset the scroll region to encompass the inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        # Set column widths
        col = 0
        for val in self.col_values:
            self.frame.grid_columnconfigure(col, minsize=self.canvas.winfo_width()*val)
            col += 1

    # Test on linux w/ mouse
    # TODO: On mac, remove 'divide by 120'
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(math.floor(-1*(event.delta/120)), "units")