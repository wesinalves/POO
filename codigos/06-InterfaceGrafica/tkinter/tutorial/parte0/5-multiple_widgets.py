from tkinter import *

def greeting():
    print('Hello stdout world!...')

win = Frame()
win.pack()
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='Hello', command=greeting).pack(side=LEFT)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT)
win.mainloop()

# win = Frame()
# win.pack(side=TOP, expand=YES, fill=BOTH)
# Button(win, text='Hello', command=greeting).pack(side=LEFT, fill=Y)
# Label(win, text='Hello container world').pack(side=TOP)
# Button(win, text='Quit', command=win.quit).pack(side=RIGHT, expand=YES,fill=X)

# Button(win, text='Hello', command=greeting).pack(side=LEFT, anchor=N)