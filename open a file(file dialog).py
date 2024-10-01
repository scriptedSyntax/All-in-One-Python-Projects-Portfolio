import fileinput
from tkinter import *
from tkinter import filedialog

# def openFile():
#     filepath = filedialog.askopenfilename()
#     file = open(filepath, 'r')
#     print(file.read())
#     file.close()

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\PlayerX\\PycharmProjects\\pythonProject",  #change this directory 
                                          title="open a file",
                                          filetypes=(("text","*.txt"),("all files","*.*")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(text="open", command=openFile)
button.pack()

window.mainloop()