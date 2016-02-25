from Tkinter import Tk, Label, Button


class Basic:
    def __init__(self, window):
        self.master = window
        window.title("A simple GUI")

        self.label2 = Label(window, text="New one.")
        self.label2.pack()

        self.label = Label(window, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(window, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(window, text="Close", command=window.quit)
        self.close_button.pack()

        window.minsize(width=600, height=600)

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = Basic(root)
root.mainloop()