from tkinter import *

def create_window():
    new_window = Tk()   # new independent window
    # new_window = Toplevel()     #new window ón top'of other window,linked together.
    old_window.destroy()   # close out of old window

old_window = Tk()

Button(old_window,text="open new window :)",font=50,command=create_window).pack()

old_window.mainloop()