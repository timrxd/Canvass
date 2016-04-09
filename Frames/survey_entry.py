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
        self.b = Button(self, text="Test")
        self.b.pack()

    def open_survey(self, name):
        self.b.config(text=name)

# end class
