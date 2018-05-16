import tkinter

root=tkinter.Tk()

canvas=tkinter.Canvas(root)
canvas.pack()

for i in range(10):
    canvas.create_line(50*i,0,50*i,400)
    canvas.create_line(0,50*i,400,50*i)
canvas.create_rectangle(100,100,200,200,fill="blue")

root.mainloop()
