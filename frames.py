# rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window, bg="pink",pady=20,padx=20,relief=SUNKEN)
frame.pack(side=TOP)

Button(frame, text="W", font=50).pack(side=TOP)
Button(frame, text="A", font=50).pack(side=LEFT)
Button(frame, text="S", font=50).pack(side=LEFT)
Button(frame, text="D", font=50).pack(side=LEFT)

window.mainloop()