import tkinter as tk
class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.func()
    def func(self):
        self.entry_1=tk.Entry(self).grid(row=0,column=1)
        self.entry_2=tk.Entry(self).grid(row=1,column=1)

        self.Label_1=tk.Label(self,text='Name')
        self.Label_1.grid(row=0)
        self.Label_2=tk.Label(self,text='Password')
        self.Label_2.grid(row=1)
        self.name=self.entry_1.get()
        self.pwd=self.entry_2.get()
        self.Button=tk.Button(self,text='To Print Name', command=lambda:self.retrieve_input()).grid(row=2, column=0)
        self.Button=tk.Button(self,text='To Print password',command=lambda:self.retrieve_input()).grid(row=2, column=1)
    def retrieve_input(self):
        print(self.name)

root=tk.Tk()
root.title("Manual Entry Field Window")
app=Application(master=root)
app.mainloop()
        
        
