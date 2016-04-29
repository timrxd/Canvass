import pymysql
import tkMessageBox
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

        # Background color of questions
        self.bg_color = "gray90"

        # List containing frames with question text and answer entry field
        self.q_list = []

        # Parent container is self.scroll.frame !!!
        self.scroll = ScrollFrame(self, values=[1])
        self.title = Label(self.scroll.frame, text="", font=("Times", 36), bg=self.bg_color)
        self.title.grid(column=0, row=0, sticky='nswe', pady=20, ipady=10)

        self.submit_button = Button(self.scroll.frame, text="Submit", bg="gold")
        self.submit_button.bind("<Button-1>", lambda e: self.submit_survey())

        self.error_label = Label(self.scroll.frame, text="[!] Some entries are missing.", fg="red")

    def test(self):
        print "cool"

    # Rewrite page with current survey
    def open_survey(self, name):
        self.title.config(text=name)

        # Clear old survey
        for q in self.q_list:
            q.grid_forget()
        del self.q_list[:]

        self.submit_button.grid_forget()

        # Get survey from db
        connection = pymysql.connect(host='cs-database.cs.loyola.edu',
                                     user='tjdowd',
                                     password='1638385',
                                     db='tjdowd',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        # prepare a cursor object using cursor() method
        cursor = connection.cursor()
        try:
            cursor.execute("DESCRIBE `" + name + "`;")

            data = cursor.fetchall()

            r = 1
            for q in data:
                panel = Frame(self.scroll.frame, bg=self.bg_color)
                panel.grid(column=0, row=r, sticky='nswe', pady=20, ipadx=15, ipady=10)

                question = Label(panel, text="Question " + str(r) + ": " + q["Field"], anchor=W, bg=self.bg_color)
                question.pack(fill=X, pady=20, padx=15)
                panel.q = q["Field"]

                answer = Entry(panel)
                answer.pack(fill=X, pady=0, padx=15)
                panel.a = answer
                answer.bind("<Return>", lambda e: self.submit_survey())
                answer.bind("<FocusOut>", lambda e: self.check_entries())

                r += 1
                self.q_list.append(panel)

            self.submit_button.grid(column=0, row=r, pady=10)

        except pymysql.err.ProgrammingError:
            self.title.config(text="Survey not found.")

        # disconnect from server
        connection.close()

    # Check for any issues with the entries
    def check_entries(self):
        for q in self.q_list:
            if q.a.get() == "":
                return False

        self.error_label.grid_forget()
        return True

    # Clear all entries and reposition cursor at Q1
    def clear_entries(self):
        for q in self.q_list:
            q.a.delete(0,END)

        self.q_list[0].a.focus_set()

    # Submit a survey response
    def submit_survey(self):

        if not self.check_entries():
            self.error_label.grid(column=0, row=(int(self.submit_button.grid_info()["row"])+1))
            return

        # Connect to the database
        connection = pymysql.connect(host='cs-database.cs.loyola.edu',
                                          user='tjdowd',
                                          password='1638385',
                                          db='tjdowd',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

        # prepare a cursor object using cursor() method
        cursor = connection.cursor()

        # Build insert statement from entries
        insert = "INSERT INTO `" + self.title.cget("text") + "` ("
        for q in self.q_list:
            insert += "`" + q.q + "`,"
        insert = insert[:-1] + ") VALUES("
        for q in self.q_list:
            insert += "\"" + q.a.get() + "\","
        insert = insert[:-1] + ");"

        cursor.execute(insert)
        connection.commit()

        # disconnect from server
        connection.close()

        tkMessageBox.showinfo("Success", "Survey submitted successfully.")
        self.clear_entries()

        # end class
