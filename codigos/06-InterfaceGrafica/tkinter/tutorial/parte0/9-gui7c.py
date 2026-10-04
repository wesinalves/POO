import standalone_container
from tkinter import *

class HelloPackage(standalone_container.HelloPackage):
    def __getattr__(self, name):
        return getattr(self.top, name) # pass off to a real widget

if __name__ == '__main__': HelloPackage().mainloop() # invokes __getattr__!