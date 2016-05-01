__author__ = 'Tim'

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *


class MainPage(Frame):
    def __init__(self, parent, top, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        self.parent = top

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)

        for x in range(0, 10):
            self.grid_rowconfigure(x, weight=1)

        self.survey_button = Button(self, text="Make Survey", font=("Times", 18), bg="steelblue")
        self.survey_button.grid(row=3, column=1, sticky="nswe")
        self.data_button = Button(self, text="Analyze Data", font=("Times", 18), bg="steelblue")
        self.data_button.grid(row=5, column=1, sticky="nswe")

        self.survey_button.bind("<Button-1>", lambda e: self.parent.to_survey_select())
        self.data_button.bind("<Button-1>", lambda e: self.parent.to_analysis_selector())

# end
