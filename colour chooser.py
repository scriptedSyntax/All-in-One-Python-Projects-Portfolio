from tkinter import *
from tkinter import colorchooser #this is a submodule

# I have used the basic code for easier understanding.
# You can edit and compress the code into even single lines if you want!

def click():
    colour = colorchooser.askcolor()
    colourHex= colour[1]
    window.config(bg=colourHex) #changes colour

window = Tk()
window.geometry("420x420")

button=Button(text='click me', command=click)
button.pack()

window.mainloop()