"""
use StringVar variables
lay out by columns: this might not align horizontally everywhere (see entry2)
"""
from tkinter import *
from quitter import Quitter
fields = 'Name', 'Job', 'Pay'

def fetch(variables):
    for variable in variables:
        print('Input => "%s"' % variable.get()) 


def makeform(root, fields):
    form = Frame(root) 
    left = Frame(form) 
    rite = Frame(form)
    form.pack(fill=X)
    left.pack(side=LEFT)
    rite.pack(side=RIGHT, expand=YES, fill=X) # make outer frame

    variables = []
    for field in fields:
        lab = Label(left, width=5, text=field) # add to columns
        ent = Entry(rite)
        lab.pack(side=TOP)
        ent.pack(side=TOP, fill=X) # grow horizontal
        var = StringVar()
        ent.config(textvariable=var) # link field to var
        var.set('enter here')
        variables.append(var)
    return variables

if __name__ == '__main__':
    root = Tk()
    vars = makeform(root, fields)
    Button(root, text='Fetch', command=(lambda: fetch(vars))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: fetch(vars)))
    root.mainloop()