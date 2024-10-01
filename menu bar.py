from tkinter import *

# if you want to add an image just use (image=photoImage you have) and compound command!

def open():
    print("this should open a file! Add the commands to do so ;)")
def save():
    print("this should save a file! Add the commands to do so ;)")
def exit():
    print("this should exit the program!")
    quit()

def copy():
    print("this should copy a file! Add the commands to do so ;)")
def cut():
    print("this should cut a file! Add the commands to do so ;)")
def paste():
    print("this should paste a file! Add the commands to do so ;)")

window = Tk()

menubar= Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=open)
fileMenu.add_command(label="Save",command=save)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=exit)

editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="copy",command=copy)
editMenu.add_command(label="paste",command=paste)
editMenu.add_command(label="cut",command=cut)

window.mainloop()