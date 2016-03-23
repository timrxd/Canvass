__author__ = 'Tim'

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

from Frames.main_page import *


class McCliff:

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



    def close_window(self):
        self.master.quit()


# end McCliff

# Start up program
def run_mccliff():
    root = Tk()
    my_gui = McCliff(root)
    root.mainloop()

run_mccliff()