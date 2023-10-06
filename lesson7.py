#from tkinter import*
#frame01 = Frame()
#frame01.mainloop()


#inheritance

from tkinter import *
from time import *

class MyFrame(Frame):
  def __init__(self):
    Frame.__init__(self)

     #self.myCanvas = Canvas(width=300, height=200, bg="blue")
     #self.myCanvas = Canvas(width=150, height=150)
     #self.myCanvas.create_rectangle(10, 10, 200, 100, fill="blue")
     #self.myCanvas.create_oval(10, 10, 200, 100, fill="white")
     #self.myCanvas.create_line(1, 1, 200, 200, arrow="first")
     #self.myCanvas.create_line(50,0,50,100)
     #self.myCanvas.create_line(0,50,1000,50)
     #self.myCanvas.create_text(50,50, text="Hello world")
     #self.myCanvas.create_text(50,50, text= "Hi there!", anchor="nw")
     #self.myCanvas.create_text(50,50, text= "Hi there!", anchor="se")

     #for text font: <font name>, <size>

     #self.myCanvas.create_text(1,1, text="Hello world", width=70, fill="blue",
      #                         anchor="nw",justify="center",font=("Times", 16))

    self.myCanvas = Canvas(width=300, height=200, bg="white")
    self.myCanvas.grid()

    #self.myCanvas.create_rectangle(10, 10, 50, 50)
    #self.myCanvas.update()

    #sleep(1)

    #self.myCanvas.create_rectangle(20, 20, 60, 60)

    my_rect_id = self.myCanvas.create_rectangle(10, 10, 50, 50)
    self.myCanvas.update()
    for count in range(10):
      increment = 10*count
      self.myCanvas.coords(my_rect_id,
        10 + increment, 10 + increment,
	50 + increment, 50 + increment)
      self.myCanvas.update()
      sleep(1)

    #for count in range(10):
      #increment = 10*count
      #self.myCanvas.create_rectangle(10 + increment,
           # 10 + increment, 50 + increment, 50 + increment)
     # self.myCanvas.update()
      #sleep(1)
     # self.myCanvas.create_rectangle(10 + increment,
	#    10 + increment, 50 + increment, 50 + increment,
	#    outline="white")
   
     

frame01 = MyFrame()
frame01.mainloop()

