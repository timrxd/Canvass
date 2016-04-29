from Frames import *

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

__author__ = 'Tim'


class McCliff:

    # Initialize main page window
    def __init__(self, window):

        # Settings:
        self.master = window
        window.title("McCliff: Survey Data Management Software")
        window.minsize(width=600, height=600)
        window.configure(background='aliceblue')  # Debug red
        try:
            window.state('zoomed')
        except TclError:
            window.minsize(width=1280, height=1000)  # window.attributes('-zoomed', True)

        # Keybindings
        window.bind("<Escape>", lambda event: self.close_window())

        # >> CONTENTS:

        # Title Bar
        title_bar = Frame(window, relief=RAISED, borderwidth=1, bg='steelblue')
        # img = Image.open("logo.pgm")
        logo = PhotoImage(file="logo.pgm")
        title = Label(title_bar, image=logo)
        title.image = logo
        # title = Label(title_bar, text="McCliff", font=("Times", 48), bg='steelblue')
        title.pack(side=LEFT)
        title_bar.pack(side=TOP, fill=X, ipady=10)

        # Content Frame
        view_frame = Frame(window, bg="white")
        view_frame.pack(fill=BOTH, expand=True)
        view_frame.grid_columnconfigure(0, weight=1)
        view_frame.grid_columnconfigure(1, weight=5)
        view_frame.grid_columnconfigure(2, weight=1)
        view_frame.grid_rowconfigure(0, weight=1)

        # Borders
        left_frame = Frame(view_frame, background="aliceblue")
        left_frame.grid(row=0, column=0, sticky="nswe")
        right_frame = Frame(view_frame, background="aliceblue")
        right_frame.grid(row=0, column=2, sticky="nswe")

        self.back_button = Button(left_frame, text="<<")
        self.back_button.pack(anchor='ne', padx=10, pady=10)
        self.right_space = Label(right_frame, width=7, bg='aliceblue')
        self.right_space.pack(anchor='nw', padx=10, pady=10)

        # Initialize with MainPage
        self.main_frame = MainPage(view_frame, bg="white")
        self.main_frame.survey_button.configure(command=self.to_survey_select)
        self.main_frame.grid(row=0, column=1, sticky="nswe")

        # Setup all other pages
        self.surveys = SelectSurvey(view_frame, self, bg="white")
        self.survey_entry = SurveyEntry(view_frame, bg="white")
        self.new_survey = NewSurvey(view_frame, bg="white")

        # Hide all sub-frames
        self.surveys.grid_forget()
        self.survey_entry.grid_forget()
        self.new_survey.grid_forget()

    def close_window(self):
        self.master.quit()

    def to_main_menu(self):
        self.surveys.grid_forget()
        self.main_frame.grid(row=0, column=1, sticky="nswe")

    def to_survey_select(self):
        self.main_frame.grid_forget()
        self.survey_entry.grid_forget()
        self.new_survey.grid_forget()
        self.surveys.grid(row=0, column=1, sticky="nswe")
        self.back_button.bind("<Button-1>", lambda e: self.to_main_menu())

    def to_survey_entry(self, survey):
        self.surveys.grid_forget()
        self.survey_entry.grid(row=0, column=1, sticky="nswe")
        self.survey_entry.open_survey(survey)
        self.back_button.bind("<Button-1>", lambda e: self.to_survey_select())

    def to_new_survey(self):
        self.surveys.grid_forget()
        self.new_survey.grid(row=0, column=1, sticky="nswe")
        self.new_survey.reset()
        self.back_button.bind("<Button-1>", lambda e: self.to_survey_select())


# end McCliff


# Start up program
def run_mccliff():
    root = Tk()
    gui = McCliff(root)
    root.mainloop()

run_mccliff()
