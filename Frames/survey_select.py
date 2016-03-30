__author__ = 'Tim'

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *


class SelectSurvey(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        for x in range(0, 10):
            self.grid_columnconfigure(x, weight=1)

        # Row 1: new survey button
        self.new_survey_button = Button(self, text=" + New Survey", bg="yellow")
        self.new_survey_button.grid(row=1, column=5, sticky="nswe", pady=10, ipady=10)

        # Row 2: Search bar
        self.search_bar = Entry(self)
        self.search_bar.grid(row=2, column=0, columnspan=11, sticky="nswe", pady=10, padx=75)

        # Row 3 Headers
        h_row = 3
        self.doc_name_label = Label(self, text="Survey Name", bg="grey", relief=RAISED)
        self.doc_name_label.grid(row=h_row, column=0, sticky="nswe")
        self.grid_columnconfigure(0, weight=3)

        self.last_mod = Label(self, text="Last Modified", bg="grey", relief=RAISED)
        self.last_mod.grid(row=h_row, column=1, sticky="nswe")
        self.grid_columnconfigure(1, weight=1)

        self.responses = Label(self, text="Responses", bg="grey", relief=RAISED)
        self.responses.grid(row=h_row, column=2, sticky="nswe")
        self.grid_columnconfigure(2, weight=1)

        self.responses = Label(self, text="Responses", bg="grey", relief=RAISED)
        self.responses.grid(row=h_row, column=2, sticky="nswe")
        self.grid_columnconfigure(2, weight=1)

# end
