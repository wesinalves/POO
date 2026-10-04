from tkinter import *
from reusable_gui import Hello

class HelloExtender(Hello):
    def make_widgets(self): # extend method here
        super().make_widgets()
        Button(self, text='Extend', command=self.quit).pack(side=RIGHT)
    def message(self):
        print('hello', self.data) # redefine method here

if __name__ == '__main__': 
    HelloExtender().mainloop()