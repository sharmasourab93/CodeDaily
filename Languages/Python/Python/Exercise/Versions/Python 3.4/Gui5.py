from tkinter import *
def result():
    print("the sum of 2+2 is",2+2)

win=Frame()#parent
win.pack()
#children
Label(win, text="Click to add to get the sum or quit to exit").pack(side=TOP)
Button(win, text="Add",command=result).pack(side=LEFT)
#Here the function is used as a command=result instead of result()
Button(win, text="Quit",command=win.quit).pack(side=RIGHT)
#Only parent widgets can be added to the mainloop
win.mainloop()

