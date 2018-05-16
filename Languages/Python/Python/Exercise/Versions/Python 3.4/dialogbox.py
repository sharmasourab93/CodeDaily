import sys
from tkinter import *
popupper=(len(sys.argv)>1)

def dialog():
    win=Toplevel()
    Label(win,text="Do you always do what you are told?").pack90
    Button(win, text="Now click this one",command=win.destroy).pack()
    if popupper:
        win.focus_set()
        win.grab_set()
        win.wait_window()
    print('You better obey me..')
root=Tk()
Button(root, text='Click Me',command=dialog).pack()
root.mainloop()
