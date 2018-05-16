import tkinter
from tkinter import *
class adder:
    "Hey this is class adder!"
    def __init__(self,master):
        "This is init class"
        frame=Frame(master)
        frame.pack()
        self.button=Button(frame,text="QUIT",fg="red",command=frame.quit)
        self.button.pack(side=LEFT)
        self.hi_there=Button(frame,text="Hello",command=self.say_hi)
    def say_hi(self):
               print("hey there everyone")


root=Tk()
#app=App(root)
root.mainloop()
#root.destroy() #optional;see description below


    
