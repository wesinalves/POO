"""
4 demo class components (subframes) on one window;
there are 5 Quitter buttons on this one window too, and each kills entire gui;
GUIs can be reused as frames in container, independent windows, or processes;
"""
from tkinter import *
from quitter import Quitter
demoModules = ['3-dialog2', '8-demo_checks', '10-demo_radio', '12-sliders']
parts = []

def addComponents(root):
    for demo in demoModules:
        module = __import__(demo) 
        part = module.Demo(root) 
        part.config(bd=2, relief=GROOVE) # or pass configs to Demo()
        part.pack(side=LEFT, expand=YES, fill=BOTH) # grow, stretch with window
        parts.append(part)

def dumpState():
    for part in parts: 
        print(part.__module__ + ':', end=' ')
        if hasattr(part, 'report'):
            part.report()
        else:
            print('none')

root = Tk() 
root.title('Frames')
Label(root, text='Multiple Frame demo', bg='white').pack()
Button(root, text='States', command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
addComponents(root)
root.mainloop()   