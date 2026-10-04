from pathlib import Path
from tkinter import *

gifdir = Path("~/Pictures").expanduser()
win = Tk()
igm = PhotoImage(file=gifdir / "logo.png")
Button(win, image=igm).pack()
win.mainloop()