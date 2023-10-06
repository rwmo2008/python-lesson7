from tkinter import *

class MyFrame(Frame):
  def __init__(self):
     Frame.__init__(self)
     self.myCanvas = Canvas(width=1000, height = 1000)
     self.myCanvas.create_rectangle(10, 10, 200, 100, fill="blue")
     self.myCanvas.create_oval(10, 10, 200, 100, fill="white")
     self.myCanvas.create_oval(10, 10, 300, 1000, fill="red")
     self.myCanvas.create_rectangle(500, 400, 1000, 600, fill="green", outline="gray")
     self.myCanvas.create_rectangle(200, 300, 700, 800, fill="brown", outline = "yellow")
     self.myCanvas.grid()
    
frame01 = MyFrame()
frame01.mainloop()
