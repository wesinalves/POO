from tkinter import *

def showPosEvent(event):
    print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))
def showAllEvent(event):
    print(event)
    for attr in dir(event):
        if not attr.startswith('__'):
            print(attr, '=>', getattr(event, attr))
def onKeyPress(event):
    print('Got key press:', event.char)
def onArrowKey(event):
    print('Got up arrow key press')
def onReturnKey(event):
    print('Got return key press')
def onLeftClick(event):
    print('Got left mouse button click:', end=' ')
    showPosEvent(event)
def onRightClick(event):
    print('Got right mouse button click:', end=' ')
    showPosEvent(event)
def onMiddleClick(event):
    print('Got middle mouse button click:', end=' ')
    showPosEvent(event)
    showAllEvent(event)
def onLeftDrag(event):
    print('Got left mouse button drag:', end=' ')
    showPosEvent(event)
def onDoubleLeftClick(event):
    print('Got double left mouse click', end=' ')
    showPosEvent(event)
    tkroot.quit()

tkroot = Tk()
labelfont = ('courier', 20, 'bold') 
widget = Label(tkroot, text='Hello bind world')
widget.config(bg='red', font=labelfont) 
widget.config(height=5, width=20) 
widget.pack(expand=YES, fill=BOTH)

widget.bind('<Button-1>', onLeftClick) # mouse button clicks
widget.bind('<Button-3>', onRightClick)
widget.bind('<Button-2>', onMiddleClick) # middle=both on some mice
widget.bind('<Double-1>', onDoubleLeftClick) # click left twice
widget.bind('<B1-Motion>', onLeftDrag) # click left and move
widget.bind('<KeyPress>', onKeyPress) # all keyboard presses
widget.bind('<Up>', onArrowKey) # arrow button pressed
widget.bind('<Return>', onReturnKey) # return/enter key pressed
widget.focus() # or bind keypress to tkroot
tkroot.title('Click Me')
tkroot.mainloop()

"""
<ButtonRelease> fires when a button is released (<ButtonPress> is run when the
button first goes down).

<Motion> is triggered when a mouse pointer is moved.

<Enter> and <Leave> handlers intercept mouse entry and exit in a window’s display
area (useful for automatically highlighting a widget).

<Configure> is invoked when the window is resized, repositioned, and so on (e.g.,
the event object’s width and height give the new window size). We’ll make use of
this to resize the display on window resizes in the PyClock example of Chapter 11.

<Destroy> is invoked when the window widget is destroyed (and differs from the
protocol mechanism for window manager close button presses). Since this inter-
acts with widget quit and destroy methods, I’ll say more about the event later in
this section.

<FocusIn> and <FocusOut> are run as the widget gains and loses focus.

<Map> and <Unmap> are run when a window is opened and iconified.

<Escape>, <BackSpace>, and <Tab> catch other special key presses.

<Down>, <Left>, and <Right> catch other arrow key presses.
"""
