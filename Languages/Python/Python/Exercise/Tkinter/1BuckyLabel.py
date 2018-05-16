import tkinter as tk
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.papp()
    def papp(self):
        self.label=tk.Label()
        self.label["text"]="Hello Label"
        self.label.pack()
root=tk.Tk()
root.title("Tkinter Tuts")
app=Application(master=root)
app.mainloop()
