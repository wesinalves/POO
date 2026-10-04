from tkinter import *
from tkinter.messagebox import askokcancel  

class Quitter(Frame): 
    def __init__(self, parent=None): # subclass our GUI
        # constructor method
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)
    
    def quit(self):
        ans = askokcancel('Verify exit', "Really quit?")
        if ans: Frame.quit(self)

if __name__ == "__main__":
    Quitter().mainloop()