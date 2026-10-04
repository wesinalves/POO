import sys
from tkinter import *
makemodal = (len(sys.argv) > 1)

def dialog():
    win = Toplevel() # make a new window
    Label(win, text='Hard drive reformatted!').pack() # add a few widgets
    Button(win, text='OK', command=win.destroy).pack() # set destroy callback
    if makemodal:
        win.focus_set() 
        win.grab_set() 
        win.wait_window() 
    print('dialog exit') # take over input focus,

root = Tk()
Button(root, text='popup', command=dialog).pack()
root.mainloop()


# from tkinter import *
# def dialog():
#     win = Toplevel() # make a new window
#     Label(win, text='Hard drive reformatted!').pack() # add a few widgets
#     Button(win, text='OK', command=win.quit).pack() # set quit callback
#     win.protocol('WM_DELETE_WINDOW', win.quit) # quit on wm close too!
#     win.focus_set() 
#     win.grab_set() 
#     win.mainloop() 
#     win.destroy()
#     print('dialog exit')
# # take over input focus,
# # disable other windows while I'm open,
# # and start a nested event loop to wait
# root = Tk()
# Button(root, text='popup', command=dialog).pack()
# root.mainloop()