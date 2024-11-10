#canvas = widget that is used to draw graphs, plots, images in a window

from tkinter import *
from turtledemo.penrose import start

window = Tk()

canvas= Canvas(window, height=500,width=500)

# canvas.create_line(0,0,500,500,width=5,fill="blue")
# canvas.create_line(0,500,500,0,width=5,fill="red")
# canvas.create_rectangle(50,50,250,250,fill="pink")
# canvas.create_polygon(250,0,500,500,0,500,fill="purple",width=5, outline="black")
# canvas.create_arc(10,10,500,500,style=PIESLICE,
#                   start=180,    #defines starting angle of the arc
#                   width=5)
#you can check out other .create_* functions

#LET'S MAKE A POKEMON BALL FOR THIS! DOWN BELOW:

canvas.create_arc(10,10,500,500,fill="red",extent=180,width=5)
canvas.create_arc(10,10,500,500,fill="white",extent=180,start=180,width=5)
canvas.create_oval(190,190,310,310, fill="white",width=5)

canvas.pack()
# canvas.place()    #same as .pack()

window.mainloop()