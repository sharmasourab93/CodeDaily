import tkinter
from tkinter import *
root=Tk()
#Below code not working
#labelfont=('times',72,'italic') #setting the family size and style
widget=Label(root, text="eat at Joes",bg='blue',fg='red',padding="30%") #Setting label text
#or another alternate here
#widget.config(bg='blue',fg='red') #setting the bacl and foreground colors
widget.pack(expand=YES,fill=BOTH)
root.mainloop()

