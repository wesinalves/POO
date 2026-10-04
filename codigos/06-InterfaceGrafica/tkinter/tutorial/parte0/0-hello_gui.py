from tkinter import *
root = Tk()


def button_clicked():
    text = my_entry.get()
    my_label.config(text=text)

my_label = Label(text="Hello GUI!")
my_button = Button(text="Clica aqui", command=button_clicked)
my_entry = Entry(width=20)

my_label.pack()
my_entry.pack()
my_button.pack()

root.geometry("320x240")
root.minsize(320, 240)

root.mainloop()