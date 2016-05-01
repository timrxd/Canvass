import pymysql
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *


class AnalyzeSurvey(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        self.survey = "survey_list"
        self.questions = []
        self.data = []

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)

        for x in range(0, 20):
            self.grid_rowconfigure(x, weight=1)

        self.title = Label(self, text="Survey", font=("Times", 36))
        self.title.grid(row=1, columnspan=3, column=0, sticky="nswe")
        self.excel = Button(self, text="Export to Excel", font=("Times", 18), bg="steelblue")
        self.excel.grid(row=7, column=1, sticky="nswe")
        self.word = Button(self, text="Export to Word", font=("Times", 18), bg="steelblue")
        self.word.grid(row=9, column=1, sticky="nswe")

        self.excel.bind("<Button-1>", lambda e: self.write_to_excel())

        # Rewrite page with current survey
    def open_survey(self, name):

        self.title.config(text=name)
        try:
            # Get survey from db
            connection = pymysql.connect(host='cs-database.cs.loyola.edu',
                                         user='tjdowd',
                                         password='1638385',
                                         db='tjdowd',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)

            # prepare a cursor object using cursor() method
            cursor = connection.cursor()

            cursor.execute("DESCRIBE `" + self.survey + "`;")
            self.questions = cursor.fetchall()
            cursor.execute("SELECT * FROM `" + self.survey + "`;")
            self.data = cursor.fetchall()

            # disconnect from server
            connection.close()
        except pymysql.ProgrammingError as e:
            print e

    def write_to_excel(self):
        print self.questions
        print self.data

# end
