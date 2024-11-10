#we will be moving images with keyboard keys
from cProfile import label
from tkinter import *

##functions for moving in window
# def up(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y()-10)
# def down(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y()+10)
# def left(event):
#     label.place(x=label.winfo_x()-10, y=label.winfo_y())
# def right(event):
#     label.place(x=label.winfo_x()+10, y=label.winfo_y())

##function for moving in canvas
def up(event):
    canvas.move(theimage, 0,-10)
def down(event):
    canvas.move(theimage,0,10)
def left(event):
    canvas.move(theimage, -10, 0)
def right(event):
    canvas.move(theimage, 10, 0)

window = Tk()
window.geometry("500x500")
myimage = PhotoImage(file="racecar.png")

##define your keys
window.bind("<w>", up)
window.bind("<s>", down)
window.bind("<a>", left)
window.bind("<d>", right)

window.bind("<Up>", up)
window.bind("<Down>", down)
window.bind("<Left>", left)
window.bind("<Right>", right)

##within the window
# label = Label(window,
#               image = myimage)
# label.place(x=0,y=0)

##within the canvas
canvas = Canvas(window,width=500,height=500)
theimage = canvas.create_image(0,0,image=myimage,anchor=NW)      #places it at 0,0 or NorthWest(NW)
canvas.pack()


window.mainloop()
