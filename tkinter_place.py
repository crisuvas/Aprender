from tkinter import *


class Interface:
    def __init__(self, container):
        self.l1 = Label(container, text="Label 1", fg="black", bg="white")
        self.l2 = Label(container, text="Label 2", fg="black", bg="gray")
        self.l3 = Label(container, text="Label 3", fg="black", bg="green")
        self.l4 = Label(container, text="Label 4", fg="black", bg="blue")
        self.l5 = Label(container, text="Label 5", fg="black", bg="yellow")
        self.l6 = Label(container, text="LAbel 6", fg="black", bg="red")
        self.l1.place(x=5, y=12, width=120, height=100)
        self.l2.place(x=12, y=13, width=120, height=100)
        self.l3.place(x=3, y=20, width=120, height=100)
        self.l4.place(x=20, y=13, width=120, height=100)
        self.l5.place(x=0, y=4, width=120, height=100)
        self.l6.place(x=-12, y=-1, width=120, height=100)


window = Tk()
my_interface = Interface(window)
window.mainloop()
