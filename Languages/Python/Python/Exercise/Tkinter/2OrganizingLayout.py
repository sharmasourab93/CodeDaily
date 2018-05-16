import tkinter as tk
class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.layOut()
        #self.title('YoU sUcK bIg TiMe')
    def layOut(self):
        var='NAME'
        self.topFrame=tk.Label(self,text=var)
        self.topFrame.pack(side='left')
        
root=tk.Tk()
app=Application(master=root)
app.mainloop()
