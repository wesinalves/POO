from tkinter import *

root = Tk()

root.geometry("320x240")
#root.minsize(320, 240)
root.title("Converte milhas para quilometros")
root.config(padx=20, pady=20)

def calculate():
    miles = int(input_miles.get())
    km = miles * 1.609
    lresult.config(text=f"{km:.2f}")

l1 = Label(text="Is equal to")
l2 = Label(text="Miles")
l3 = Label(text="KM")
lresult = Label(text="0")

l1.grid(row=1,column=0)
l2.grid(row=0,column=2)
l3.grid(row=1,column=2)
lresult.grid(row=1,column=1)


input_miles = Entry(width=4)
input_miles.grid(row=0, column=1)
bt1 = Button(text="Calculate", command=calculate)
bt1.grid(row=2, column=1)

root.mainloop()