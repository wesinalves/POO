# radio buttons, the easy way
from tkinter import *

root = Tk() 
var = IntVar(value=0) # IntVars work too

for i in range(10):
    rad = Radiobutton(root, text=str(i), value=i, variable=var)
    rad.pack(side=LEFT)

root.mainloop()
print(var.get()) # show state on exit