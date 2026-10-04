# import sys
# from tkinter import Toplevel, Button, Label
# win1 = Toplevel() 
# win2 = Toplevel() # two independent windows
# # but part of same process
# Button(win1, text='Spam', command=sys.exit).pack()
# Button(win2, text='SPAM', command=sys.exit).pack()
# Label(text='Popups').pack() 
# win1.mainloop()


# import tkinter
# from tkinter import Tk, Button
# tkinter.NoDefaultRoot()
# win1 = Tk() 
# win2 = Tk()
# # two independent root windows
# Button(win1, text='Spam', command=win1.destroy).pack()
# Button(win2, text='SPAM', command=win2.destroy).pack()
# win1.mainloop()

from tkinter import *
root = Tk() # explicit root
trees = [
    ('The Larch!', 'light blue'),
    ('The Pine!', 'light green'),
    ('The Giant Redwood!', 'red')
]

for (tree, color) in trees:
    win = Toplevel(root) # new window
    win.title('Sing...') # set border
    win.protocol('WM_DELETE_WINDOW', lambda:None) # ignore close
    win.iconbitmap('py-blue-trans-out.ico') # not red Tk
    msg = Button(win, text=tree, command=win.destroy) 
    msg.pack(expand=YES, fill=BOTH)
    msg.config(padx=10, pady=10, bd=10, relief=RAISED)
    msg.config(bg='black', fg=color, font=('times', 30, 'bold italic'))

# kills one win
root.title('Lumberjack demo')
Label(root, text='Main window', width=30).pack()
Button(root, text='Quit All', command=root.quit).pack() 
root.mainloop()