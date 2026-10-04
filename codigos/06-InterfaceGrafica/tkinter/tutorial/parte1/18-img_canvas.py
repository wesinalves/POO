from pathlib import Path
from tkinter import *

gifdir = Path("~/Pictures").expanduser()

win = Tk()
img = PhotoImage(file=gifdir / "logo.png")
can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=img.width(), height=img.height()) 
can.create_image(2, 2, image=img, anchor=NW) # x, y coordinates
win.mainloop()