from importlib.metadata import files
from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ("text",".txt"),
                                        ("HTML", ".html"),
                                        ("all files",".*")
                                    ])

    if file is None:        #helps remove errors when you cancel saving file as
        return
    filetext = str(text.get(1.0,END))
    filetext = input("put some text on the console: ")  #add text to save via console
    file.write(filetext)
    file.close()

window = Tk()        #creates a window

text = Text(window)
text.pack()
button=Button(window, text='save',command=saveFile)
button.pack()
window.mainloop()
