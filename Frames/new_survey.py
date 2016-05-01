import pymysql
import tkMessageBox
import datetime
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

from .scroll_frame import ScrollFrame


class NewSurvey(Frame):
    def __init__(self, parent, top, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        self.parent = top

        # Background color of questions
        self.bg_color = "lightblue"

        # List containing frames with question text and answer entry field
        self.q_list = []

        # Parent container is self.scroll.frame !!!
        self.scroll = ScrollFrame(self, values=[1])
        self.scroll.frame.config(bg="white")

        # Top panel with survey details
        self.top_panel = Frame(self.scroll.frame, bg=self.bg_color)
        self.top_panel.grid(column=0, row=0, sticky='nswe', pady=10, ipady=10)

        # Survey details (name, location, date)
        self.title = Entry(self.top_panel, font=("Times", 36), bg=self.bg_color, justify=CENTER)
        self.title.pack(fill=X, pady=20, ipady=10)

        self.loc_panel = Frame(self.top_panel, bg=self.bg_color)
        self.loc_panel.pack()
        self.loc_label = Label(self.loc_panel, text="Location: ", bg=self.bg_color)
        self.loc_label.pack(side=LEFT)
        self.location = Entry(self.loc_panel)
        self.location.pack(side=RIGHT)

        self.date_panel = Frame(self.top_panel, bg=self.bg_color)
        self.date_panel.pack()
        self.date_label = Label(self.date_panel, text="Event Date: ", bg=self.bg_color)
        self.date_label.pack(side=LEFT)

        # Month
        self.month = IntVar(self)
        self.month.set(datetime.datetime.now().month)
        self.month_select = OptionMenu(self.date_panel, self.month,
                                       "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
        self.month_select.pack(pady=5, side=LEFT)
        Label(self.date_panel, text=" / ", bg=self.bg_color).pack(side=LEFT)

        # Day
        self.day = IntVar(self)
        self.day.set(datetime.datetime.now().day)
        self.day_select = OptionMenu(self.date_panel, self.day,
                                     "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                                     "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                                     "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
        self.day_select.pack(pady=5, side=LEFT)
        Label(self.date_panel, text=" / ", bg=self.bg_color).pack(side=LEFT)

        # Year
        self.year = IntVar(self)
        self.year.set(datetime.datetime.now().year)
        self.year_select = OptionMenu(self.date_panel, self.year,
                                      "2014", "2015", "2016", "2017", "2018", "2019", "2020")
        self.year_select.pack(pady=5, side=LEFT)

        # Other buttons
        self.add_button = Button(self.scroll.frame, text="+ Add Question", bg="white")
        self.add_button.bind("<Button-1>", lambda e: self.add_question())

        self.create_button = Button(self.scroll.frame, text="Create Survey", bg="gold")
        self.create_button.bind("<Button-1>", lambda e: self.create_survey())

    def reset(self):
        self.title.delete(0, END)
        self.title.insert(0, "< Title goes here >")
        self.location.delete(0, END)
        self.month.set(datetime.datetime.now().month)
        self.day.set(datetime.datetime.now().day)
        self.year.set(datetime.datetime.now().year)

        # TODO clear other stuff
        for q in self.q_list:
            q.grid_forget()
        del self.q_list[:]

        self.add_button.grid(row=1, pady=20)

    def valid_fields(self):
        try:
            datetime.datetime(year=self.year.get(),month=self.month.get(),day=self.day.get())
        except ValueError:
            print("Failed")
            return False

        return True

    def add_question(self):
        panel = Frame(self.scroll.frame, bg=self.bg_color, relief=RIDGE)
        self.q_list.append(panel)

        panel.label = Label(panel, text="Question " + str(len(self.q_list)), anchor="w", font=("Times", 18),
                            bg=self.bg_color)
        panel.label.pack(pady=5, fill=X, padx=15)

        panel.question = Text(panel, height=3)
        panel.question.pack(padx=15, pady=5, ipady=10, fill=X)

        type = Frame(panel)

        panel.label2 = Label(panel, text="Question Type:", anchor="w", bg=self.bg_color)
        panel.label2.pack(pady=5, fill=X, padx=15, side=LEFT)

        panel.q_type = StringVar(panel)
        panel.q_type.set("String")
        panel.type_select = OptionMenu(panel, panel.q_type, "String", "Number", "True/False")
        panel.type_select.pack(pady=15, side=LEFT)

        r = self.add_button.grid_info()["row"]
        self.add_button.grid_forget()
        panel.grid(row=r, sticky='nswe', pady=10, ipadx=15)
        self.add_button.grid(row=int(r)+1, pady=20)
        self.create_button.grid(row=int(r)+2, pady=20)

    # Create a table from the questions in this form
    def create_survey(self):

        if not self.valid_fields():
            return

        create = "CREATE TABLE `" + self.title.get() + "`("
        for q in self.q_list:
            create += "`" + q.question.get(1.0, END)[:-1] + "` VARCHAR(255),"
        create = create[:-1] + ");"
        print create

        add = "INSERT INTO survey_list(name, lastmod, responses, location, eventdate) " \
              "VALUES(\""+ self.title.get() + "\",CURDATE(),0,\"" + self.location.get() + "\",\"" + \
              str(self.year.get()) + "-" + str(self.month.get()) + "-" + str(self.day.get()) + "\");"
        print add

        try:
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
            cursor.execute(add)
            connection.commit()

            # disconnect from server
            connection.close()

            tkMessageBox.showinfo("Success", "Survey created successfully.")
            self.parent.to_survey_select()

        except:
            tkMessageBox.showinfo("Error", "Cannot connect to server (create_survey).")

# end class
