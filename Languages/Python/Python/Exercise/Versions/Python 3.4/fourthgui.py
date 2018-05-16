#This program defines the functions and attributes of Button and Label
#Fourth GUI program 
import tkinter
from tkinter import *
x=Label(text="My GUI after a long time").pack(expand=YES, fill=BOTH)
y=Button(text="Click Me!",fg="red",command=exit)
y.pack(side=RIGHT)
y.mainloop()
