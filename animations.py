## downloading images was a hustle and we are just here to learn.  i will use just background colour
from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
VELOCITY_X = 4
VELOCITY_Y = 3

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

pic = PhotoImage(file='racecar.png')
my_image = canvas.create_image(0,0,image=pic,anchor=NW)

image_width = pic.width()
image_height = pic.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if (coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        VELOCITY_X = -VELOCITY_X
    if (coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        VELOCITY_Y = -VELOCITY_Y
    canvas.move(my_image, VELOCITY_X,VELOCITY_Y)
    window.update()     #will continously update the window
    time.sleep(0.01)

window.mainloop()

## now that I'm done with this I feel like I should have used the sony DVD logo (>_<)