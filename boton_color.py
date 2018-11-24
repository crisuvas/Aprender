from tkinter import *


class Interface:

    def __init__(self, container):
        self.l1 = Label(container, text="My background will change", fg="black", width=30)
        self.b1 = Button(container, text="Red", fg="black", width=10, command=self.color_red)
        self.b2 = Button(container, text="Blue", fg="black", width=10, command=self.color_blue)
        self.b3 = Button(container, text="Yellow", fg="black", width=10, command=self.color_yellow)
        self.l1.grid(column=0, row=0, columnspan=3)
        self.b1.grid(column=0, row=1)
        self.b2.grid(column=1, row=1)
        self.b3.grid(column=2, row=1)

    def color_red(self):
        self.l1["bg"] = "red"

    def color_blue(self):
        self.l1["bg"] = "blue"

    def color_yellow(self):
        self.l1["bg"] = "yellow"


window = Tk()
my_interface = Interface(window)
window.mainloop()
