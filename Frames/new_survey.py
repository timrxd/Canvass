import pymysql
import tkMessageBox
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

from .scroll_frame import ScrollFrame


class NewSurvey(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        # Background color of questions
        self.bg_color = "gray90"

        # List containing frames with question text and answer entry field
        self.q_list = []

        # Parent container is self.scroll.frame !!!
        self.scroll = ScrollFrame(self, values=[1])
        self.scroll.frame.config(bg="lightblue")
        self.title = Entry(self.scroll.frame, font=("Times", 36), bg=self.bg_color, justify=CENTER)
        self.title.grid(column=0, row=0, sticky='nswe', pady=20, ipady=10)

        self.add_button = Button(self.scroll.frame, text="+ Add Question")
        self.add_button.bind("<Button-1>", lambda e: self.add_question())

        self.create_button = Button(self.scroll.frame, text="Create Survey", bg="gold")
        self.create_button.bind("<Button-1>", lambda e: self.create_survey())

    def reset(self):
        self.title.delete(0, END)
        self.title.insert(0, "< Title goes here >")

        # TODO clear other stuff
        for q in self.q_list:
            q.grid_forget()
        del self.q_list[:]

        self.add_button.grid(row=1, pady=20)

    def add_question(self):
        panel = Frame(self.scroll.frame, bg=self.bg_color, relief=RIDGE)
        self.q_list.append(panel)

        panel.label = Label(panel, text="Question " + str(len(self.q_list)), anchor="w", font=("Times", 18),
                            bg=self.bg_color)
        panel.label.pack(pady=5, fill=X)

        panel.question = Text(panel, height=3)
        panel.question.pack(pady=5, ipady=10, fill=X)

        panel.label2 = Label(panel, text="Question Type:", anchor="w", bg=self.bg_color)
        panel.label2.pack(pady=5, fill=X)

        panel.q_type = StringVar(panel)
        panel.q_type.set("String")
        panel.type_select = OptionMenu(panel, panel.q_type, "String", "Number", "True/False")
        panel.type_select.pack(pady=5, side=LEFT)

        r = self.add_button.grid_info()["row"]
        self.add_button.grid_forget()
        panel.grid(row=r, sticky='nswe', pady=10)
        self.add_button.grid(row=int(r)+1, pady=20)
        self.create_button.grid(row=int(r)+2, pady=20)

    # Create a table from the questions in this form
    def create_survey(self):
        create = "CREATE TABLE `" + self.title.get() + "`("
        for q in self.q_list:
            create += "`" + q.question.get(1.0, END)[:-1] + "` VARCHAR(255),"
        create = create[:-1] + ");"
        print create

        # Connect to the database
        connection = pymysql.connect(host='cs-database.cs.loyola.edu',
                                          user='tjdowd',
                                          password='1638385',
                                          db='tjdowd',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

        # prepare a cursor object using cursor() method
        cursor = connection.cursor()
        cursor.execute(create)
        connection.commit()

        # disconnect from server
        connection.close()

# end class
