from tkinter import *


class Interface:
    def __init__(self, container):
        self.l1 = Label(container, text="Label 1", fg="black", bg="white")
        self.l2 = Label(container, text="Label 2", fg="black", bg="gray")
        self.l3 = Label(container, text="Label 3", fg="black", bg="green")
        self.l4 = Label(container, text="Label 4", fg="black", bg="blue")
        self.l5 = Label(container, text="Label 5", fg="black", bg="yellow")
        self.l6 = Label(container, text="LAbel 6", fg="black", bg="red")
        self.l1.grid(column=0, row=0)
        self.l2.grid(column=0, row=1)
        self.l3.grid(column=0, row=2)
        self.l4.grid(column=1, row=0)
        self.l5.grid(column=1, row=1)
        self.l6.grid(column=1, row=2)


window = Tk()
my_interface = Interface(window)
window.mainloop()
