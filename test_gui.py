try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *


# All methods required for main page
def key(event, window):
    window.quit

# Main page class
class MainPage:

    # Initialize main page window
    def __init__(self, window):

        # Settings
        self.master = window
        window.title("McCliff")
        window.state('zoomed')
        window.minsize(width=600, height=600)
        window.bind("<Escape>", key(window))

        self.label2 = Label(window, text="New one.")
        self.label2.pack()

        self.label = Label(window, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(window, text="Greet", command=window.quit)
        self.greet_button.pack()

        self.close_button = Button(window, text="Close", command=window.quit)
        self.close_button.pack()

# end mainPage

def run_mccliff():
    root = Tk()
    my_gui = MainPage(root)
    root.mainloop()

run_mccliff()