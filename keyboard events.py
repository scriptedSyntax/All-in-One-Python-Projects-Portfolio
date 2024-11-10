from tkinter import *

def doSomething(event):     #don't forget to include event
    # print("you pressed: "+ event.keysym)
    label.config(text=event.keysym)

window=Tk()

# window.bind("<y>", doSomething)     #wnidow.bind(event, function)
window.bind("<Key>", doSomething)   #responds to all keyevents
label =  Label(window, font=("Cambira",100))
label.pack()


window.mainloop()