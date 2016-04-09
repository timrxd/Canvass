__author__ = 'Tim'

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

from .scroll_frame import ScrollFrame


def highlight_row(row, color):
    for label in row:
        label.config(bg=color)


class SelectSurvey(Frame):
    def __init__(self, parent, top, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        self.parent = top

        self.top_bar = Frame(self, bg="white")
        self.top_bar.pack(fill=BOTH, ipady=10)

        # Row 1: new survey button
        self.new_survey_button = Button(self.top_bar, text=" + New Survey", bg="gold")
        self.new_survey_button.grid(row=1, column=2, sticky="nswe", pady=10, ipady=10)

        # Row 2: Search bar
        self.search_bar = Entry(self.top_bar)
        self.search_bar.grid(row=2, column=0, columnspan=5, sticky="nswe", pady=30, padx=75)

        # Row 3 Headers
        self.top_bar.grid_columnconfigure(0, weight=10)
        self.top_bar.grid_columnconfigure(1, weight=1)
        self.top_bar.grid_columnconfigure(2, weight=1)
        self.top_bar.grid_columnconfigure(3, weight=10)
        self.top_bar.grid_columnconfigure(4, weight=1)

        h_row = 3
        self.doc_name_label = Label(self.top_bar, text="Survey Name", bg="lightgray", relief=RAISED, anchor="w")
        self.doc_name_label.grid(row=h_row, column=0, sticky="nswe")

        self.last_mod = Label(self.top_bar, text="Last Modified", bg="lightgray", relief=RAISED, anchor="w")
        self.last_mod.grid(row=h_row, column=1, sticky="nswe")

        self.responses = Label(self.top_bar, text="Responses", bg="lightgray", relief=RAISED, anchor="w")
        self.responses.grid(row=h_row, column=2, sticky="nswe")

        self.location = Label(self.top_bar, text="Location", bg="lightgray", relief=RAISED, anchor="w")
        self.location.grid(row=h_row, column=3, sticky="nswe")

        self.date = Label(self.top_bar, text="Event Date", bg="lightgray", relief=RAISED, anchor="w")
        self.date.grid(row=h_row, column=4, sticky="nswe")

        # Eventually SQL call
        test_data = [["Loyola", "2/21", "100", "Baltimore", "1/1"],
                     ["Central", "1/25", "88", "Flemington", "2/2"],
                     ["North", "3/21", "100", "Baltimore", "1/1"],
                     ["South", "4/25", "88", "Flemington", "2/2"],
                     ["Del Val", "5/21", "100", "Baltimore", "1/1"],
                     ["JP Case", "6/25", "88", "Flemington", "2/2"]
                    ]

        test_data += test_data
        test_data += test_data
        test_data += test_data
        test_data += test_data

        self.scroll = ScrollFrame(self, data=test_data, values=[.35, .1, .1, .35, .1])
        self.scroll.pack(fill=BOTH, expand=True)

        r = 0
        c = 0
        for row in test_data:
            c = 0
            survey_row = [None] * 5
            for col in row:
                l = Label(self.scroll.frame, text=row[c], bg="lightyellow", anchor="w", relief=RAISED)
                l.grid(column=c, row=r, sticky="nswe", pady=2)
                l.bind("<Button-1>", lambda e, link=row[0], main=self.parent: main.to_survey_entry(link))
                survey_row[c] = l
                c += 1

            for label in survey_row:
                label.bind("<Enter>", lambda e, x=survey_row: highlight_row(x, 'yellow'))
                label.bind("<Leave>", lambda e, x=survey_row: highlight_row(x, 'lightyellow'))
            r += 1

# end
