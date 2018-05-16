import tkinter as tk
from tkinter import *
class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.writetext()
		self.tw=''
	def writetext(self):
		self.text=tk.Text()
		self.text.pack(side="top")
		tw=get_input()
		#self.b=tk.Button(command=tw)
		self.b["command"]=tw
		self.b.pack(side="top")
		
	def get_input(self):
                i=self.myTextBox.get("1.0",END)
                return i
		
root=tk.Tk()
app=Application(master=root)
app.mainloop()

