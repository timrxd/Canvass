try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

from Frames import *

class ScrollFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent)
        self.text = Text(self, *args, **kwargs)
        self.vsb = Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)

        # expose some text methods as methods on this object
        self.insert = self.text.insert
        self.delete = self.text.delete
        self.mark_set = self.text.mark_set
        self.get = self.text.get
        self.index = self.text.index
        self.search = self.text.search


# Main page class
class TestPage:

    # Initialize main page window
    def __init__(self, window):

        # Settings:
        self.master = window
        window.title("McCliff")
        window.state('normal')
        window.minsize(width=600, height=600)
        window.configure(background='aliceblue')
        # window.attributes('-zoomed', True)

        # Keybindings
        window.bind("<Escape>", lambda event: self.close_window())

        # Contents:

        # Title Bar
        title_bar = Frame(window, relief=RAISED, borderwidth=1, bg='steelblue')
        title = Label(title_bar, text="McCliff", font=("Times", 48), bg='steelblue')
        title.pack(side=LEFT)
        title_bar.pack(side=TOP, fill=X, ipady=10)

        # Content Frame
        view_frame = Frame(window, bg="white")
        view_frame.pack(fill=BOTH, expand=True)
        view_frame.grid_columnconfigure(0, weight=1)
        view_frame.grid_columnconfigure(1, weight=2)
        view_frame.grid_columnconfigure(2, weight=1)
        view_frame.grid_rowconfigure(0,weight=1)

        # Borders
        left_frame = Frame(view_frame, background="aliceblue")
        left_frame.grid(row=0, column=0, sticky="nswe")  # .pack(side=LEFT, fill=Y)
        right_frame = Frame(view_frame, background="aliceblue")
        right_frame.grid(row=0, column=2, sticky="nswe")  # .pack(side=RIGHT, fill=Y)

        # Main Frame
        self.main_frame = Frame(view_frame, bg="aliceblue")
        self.main_frame.grid(row=0, column=1, sticky="nswe")  # .pack(fill=BOTH, expand=1)

        # Main Frame Contents
        self.label = Label(self.main_frame, text="Survey Title", font=("Times", 48), bg=self.main_frame.cget('bg'))
        self.label.pack(ipady=15)

        content_frame = Frame(self.main_frame, bg="white")
        content_frame.pack(fill=BOTH, expand=True, padx=25)
        scroll = MainPage(content_frame)
        scroll.pack(fill=BOTH, expand=True)

    def close_window(self):
        self.master.quit()


# end mainPage

# Start up program
def run_mccliff():
    root = Tk()
    my_gui = TestPage(root)
    root.mainloop()

run_mccliff()