from logging import warning
from tkinter import *
from tkinter import messagebox  #import messagebox library

def click():
    # messagebox.showinfo(title='You have been informed!',message='just kidding though ;)')
    # messagebox.showerror(title='You have been error!', message='just kidding though ;)')
    # messagebox.showwarning(title='You have been warned!', message='just kidding though ;)')

    # if messagebox.askyesno(title='askyesno', message='do you want to do the thing?'):
    #     print('did he thing!')
    # else:
    #     print("no thing done :(")
    #
    # if messagebox.askokcancel(title='ask ok cancel', message='do you want to do the thing?'):
    #     print('did he thing!')
    # else:
    #     print("no thing done :(")
    #
    # if messagebox.askretrycancel(title='ask retry cancel', message='do you want to do the thing?'):
    #     print('did he thing!')
    # else:
    #     print("no thing done :(")

    answer = messagebox.askyesnocancel(title='yes no cancel',message='pick one. this is a test ;)',icon='warning')
    if (answer==True):
        print('you passed the test')
    elif (answer==False):
        print('maybe passed the test')
    elif (answer==None):
        print('you failed terribly :(')

window = Tk()

button = Button(window, text='click me!',command=click)
button.pack()

window.mainloop()