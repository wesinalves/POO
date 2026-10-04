from tkinter import * # get a widget object
widget = Label(None, text='Hello GUI world!') # make one
widget.pack() # arrange it
widget.mainloop() # start event loop

#### ALTERNATIVES ######
# import tkinter
# widget = tkinter.Label(None, text='Hello GUI world!')
# widget.pack()
# widget.mainloop()

# from tkinter import *
# root = Tk()
# Label(root, text='Hello GUI world!').pack(side=TOP)
# root.mainloop()

# from tkinter import *
# Label(text='Hello GUI world!').pack()
# mainloop()