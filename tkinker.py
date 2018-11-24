from tkinter import *


class Interface:
    def __init__(self, container):
        """self.button = Button(container, text="Hello", width=78)
        self.check_button = Checkbutton(container, text="Are you ok?")
        self.entry = Entry(container)
        self.radio_button = Radiobutton(container, text="a man")"""
        self.l1 = Label(container, text="Label 1", fg="black", bg="white")
        self.l2 = Label(container, text="Label 2", fg="black", bg="gray")
        self.l3 = Label(container, text="Label 3", fg="black", bg="green")
        """self.button.pack()
        self.check_button.pack()
        self.entry.pack()
        self.radio_button.pack()"""
        self.l1.pack(side=TOP)
        self.l2.pack(side=RIGHT)
        self.l3.pack(side=BOTTOM, fill=X)


window = Tk()
my_interface = Interface(window)
window.mainloop()
