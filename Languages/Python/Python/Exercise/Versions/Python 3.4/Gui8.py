#radio button creation
import tkinter
from tkinter import *
state=''
buttons=[]

def choose(i):
    global state #global variable
    state = i    #
    #for btn in buttons:
     #   btn.deselect()
    buttons[i].select()
root=Tk()
#Creates 4 radiobuttons
for i in range(4):
    radio=Radiobutton(root,text=str(i),value=str(i),command=(lambda i=i:choose(i)))

    radio.pack(side=BOTTOM)
    buttons.append(radio)
root.mainloop()

print("You chose the following numbers:",state)
