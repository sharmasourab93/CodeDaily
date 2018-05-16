import tkinter as tk
class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.widgets()
    def widgets(self):
        self.hello_there=tk.Button(self)
        self.hello_there["text"]="This is my 2nd Hello World"
        x=0
        self.hello_there["command"]=self.add(x)
        self.hello_there.pack(side="top")
        
        #self.hey_there=tk.Button(self)
        #self.hey_there["text"]=self.add(x)
        #self.hey_there.pack(side="right")

        self.quit=tk.Button(self,text="Sorry to say Good Bye?", bg="red", command=root.destroy)
        self.quit.pack(side="bottom")
    def add(self,x):
        print(x+1)

root=tk.Tk()
app=Application(master=root)
app.mainloop()
