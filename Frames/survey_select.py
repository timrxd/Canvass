from .scroll_frame import ScrollFrame
import pymysql
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *


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
        self.new_survey_button.bind("<Button-1>", lambda e, main=self.parent: main.to_new_survey())

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

        self.survey_list = []

        self.scroll = ScrollFrame(self, values=[.35, .1, .1, .35, .1])
        self.scroll.pack(fill=BOTH, expand=True)

        # Get and place all surveys in the table
        self.refresh()

    def refresh(self):
        # Connect to the database
        connection = pymysql.connect(host='cs-database.cs.loyola.edu',
                                     user='tjdowd',
                                     password='1638385',
                                     db='tjdowd',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        # prepare a cursor object using cursor() method
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM survey_list;")
        data = cursor.fetchall()

        # disconnect from server
        connection.close()

        for widget in self.scroll.frame.winfo_children():
            widget.destroy()

        r = 0
        c = 0
        for row in data:
            c = 0
            survey_row = [None] * 5

            line = [row["name"], row["lastmod"], row["responses"], row["location"], row["eventdate"]]

            for col in line:
                l = Label(self.scroll.frame, text=line[c], bg="lightyellow", anchor="w", relief=RAISED)
                l.grid(column=c, row=r, sticky="nswe", pady=2)
                l.bind("<Button-1>", lambda e, link=line[0], main=self.parent: main.to_survey_entry(link))
                survey_row[c] = l
                c += 1

            for label in survey_row:
                label.bind("<Enter>", lambda e, x=survey_row: highlight_row(x, 'yellow'))
                label.bind("<Leave>", lambda e, x=survey_row: highlight_row(x, 'lightyellow'))
            r += 1

# end
