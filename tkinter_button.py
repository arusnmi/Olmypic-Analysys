from tkinter import *
from tkinter import ttk

global test
test=""

root=Tk()


root.title("test")

def button_click():
    global test
    test="Button clicked"
    label=ttk.Label(root, text=test)
    label.grid(row=0, column=0)

button=Button(root, text="click this",command=button_click)

root.rowconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)

button.grid(row=0, column=1)

root.mainloop()