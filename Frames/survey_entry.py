__author__ = 'Tim'

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

from .scroll_frame import ScrollFrame


class SurveyEntry(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        # Parent container is self.scroll.frame !!!
        self.scroll = ScrollFrame(self, values=[1])
        self.title = Label(self.scroll.frame, text="", font=("Times", 24))
        self.title.grid(column=0, row=0, sticky='nswe')

    def open_survey(self, name):
        self.title.config(text=name)

# end class
