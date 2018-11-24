from tkinter import *


class Interface:
    def __init__(self, container):
        self.text = StringVar()
        self.l1 = Label(container, text="Convert Celsius to Fahrenheit", fg="black")
        self.l2 = Label(container, text="Celsius", fg="black")
        self.l3 = Label(container, text="Fahrenheit", fg="black")
        self.l4 = Button(container, text="Convert", fg="black", bg="cyan", command=self.make_conversion)
        self.l5 = Entry(container, fg="black", bg="white")
        self.l6 = Label(container, text="", fg="black", textvariable=self.text)
        self.l1.grid(column=0, row=0, columnspan=2)
        self.l2.grid(column=0, row=1)
        self.l3.grid(column=0, row=2)
        self.l4.grid(column=0, row=3, columnspan=2)
        self.l5.grid(column=1, row=1)
        self.l6.grid(column=1, row=2)

    def make_conversion(self):
        cel = float(self.l5.get())
        fahr = cel * 1.8 + 32
        self.text.set(fahr)


window = Tk()
my_interface = Interface(window)
window.mainloop()
