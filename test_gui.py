try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

from frames.main_page import *


# Main page class
class MainPage:

    # Initialize main page window
    def __init__(self, window):

        # Settings:
        self.master = window
        window.title("McCliff")
        window.state('zoomed')
        window.minsize(width=600, height=600)
        window.configure(background='red')  # Debug red

        # Keybindings
        window.bind("<Escape>", lambda event: self.close_window())

        # Contents:

        # Title Bar
        title_bar = Frame(window, relief=RAISED, borderwidth=1, bg='steelblue')
        title = Label(title_bar, text="McCliff", font=("Times", 48), bg='steelblue')
        title.pack(side=LEFT)
        title_bar.pack(side=TOP, fill=X, ipady=10)

        # Borders
        left_frame = Frame(window, background="aliceblue", width=window.winfo_screenwidth()/6)
        left_frame.pack(side=LEFT, fill=Y)
        right_frame = Frame(window, background="aliceblue", width=window.winfo_screenwidth()/6)
        right_frame.pack(side=RIGHT, fill=Y)

        # Main Frame

        self.main_frame = Frame(window, bg="aliceblue")
        self.main_frame.pack(fill=BOTH, expand=True)


        # Main Frame Contents

        self.label = Label(self.main_frame, text="Survey Title", font=("Times", 48), bg=self.main_frame.cget('bg'))
        self.label.pack(ipady=15)

        content_frame = Frame(self.main_frame, bg="lightsteelblue")
        content_frame.pack(fill=BOTH, expand=True, padx=25)
        scroll = ScrollFrame(content_frame)
        scroll.pack(fill=BOTH, expand=True)

        # self.close_button = Button(self.main_frame, text="Close", command=window.quit)
        # self.close_button.pack()

    def close_window(self):
        self.master.quit()


# end mainPage

# Start up program
def run_mccliff():
    root = Tk()
    my_gui = MainPage(root)
    root.mainloop()

run_mccliff()