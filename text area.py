from tkinter import *

def submit():
    input = text.get("1.0",END) #grab text from first index to last
    print(input)

window = Tk()

text = Text(window,
            font=('ink free', 25),
            padx=10,
            pady=10,
            height=10,
            width=15,
            bg="light yellow",
            fg='black')
text.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()