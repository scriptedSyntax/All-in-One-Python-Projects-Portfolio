from tkinter import *

def doSomething(event):
    print("Mouse coordinates: " + str(event.x)+" , "+str(event.y))

window=Tk()

window.bind("<Button-1>", doSomething)  #Button-1 = LMB, Button-2 = MMB, Button-3 = RMB
window.bind("<ButtonRelease>", doSomething)  #on button release
window.bind("<Enter>", doSomething)  #on entering the window
window.bind("<Leave>", doSomething)  #on leaving the window
window.bind("<Motion>", doSomething)  #as long as cursor in motion

window.mainloop()