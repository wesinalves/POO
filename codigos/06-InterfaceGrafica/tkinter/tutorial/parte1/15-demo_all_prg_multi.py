"""
4 demo classes run as independent program processes: multiprocessing;
multiprocessing allows us to launch named functions with arguments,
but not lambdas, because they are not pickleable on Windows (Chapter 5);
multiprocessing also has its own IPC tools like pipes for communication;
"""
from tkinter import *
from multiprocessing import Process
demoModules = ['3-dialog2', '8-demo_checks', '10-demo_radio', '12-sliders']

def runDemo(modname): 
    module = __import__(modname) 
    module.Demo().mainloop()

if __name__ == '__main__':
    for modname in demoModules: 
        Process(target=runDemo, args=(modname,)).start()

    root = Tk() # parent process GUI
    root.title('Processes')
    Label(root, text='Multiple program demo: multiprocessing', bg='white').pack()
    root.mainloop()