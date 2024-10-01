from tkinter import *

def submit():
    # print("you have chosen: " + listbox.get(listbox.curselection()))

    food=[]
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    for index in food:
        print("you have chosen: " + index)

def add():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())

def delete():
    # listbox.delete(listbox.curselection())
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,font=('arial', 32),
                  selectmode=MULTIPLE)
listbox.insert(1, "pizza")
listbox.insert(2, "cake")
listbox.insert(3, "milk")
listbox.insert(4, "chicken")
listbox.insert(5, "cookies")
listbox.config(height=listbox.size())

entry_box = Entry(window)
entry_box.pack()

submit_button = Button(window, text="submit", command=submit)
submit_button.pack()

add_button = Button(window, text="add", command=add)
add_button.pack()

delete_button = Button(window, text="delete", command=delete)
delete_button.pack()

listbox.pack()
window.mainloop()