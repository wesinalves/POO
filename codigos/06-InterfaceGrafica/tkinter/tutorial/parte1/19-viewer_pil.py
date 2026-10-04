"""
show one image with PIL photo replacement object
handles many more image types; install PIL first: placed in Lib\site-packages
"""
from pathlib import Path
import os, sys
from tkinter import *
from PIL.ImageTk import PhotoImage 

imgdir = Path("~/Pictures").expanduser()
imgfile = 'music-cover.jpeg' 

if len(sys.argv) > 1:
    imgfile = sys.argv[1]

imgpath = os.path.join(imgdir, imgfile)

win = Tk()
win.title(imgfile)
imgobj = PhotoImage(file=imgpath) 

Label(win, image=imgobj).pack()

win.mainloop()
print(imgobj.width(), imgobj.height()) 