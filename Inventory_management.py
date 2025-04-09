from tkinter import *
from tkinter import ttk
import pandas as pd

invenManager=pd.read_csv("inventory.csv")
options=invenManager['Ingredient'].tolist()
root=Tk()
root.geometry('1100x700')

root.title("Inventory Management")

def City_select(event):
    selected_city = cityselected_option.get()
    selected_rows = invenManager.loc[invenManager['Ingredient'] == selected_city]
    Resualtvarible=Label(root,text=selected_rows)
    Resualtvarible.grid(row=2,column=1)

def submit():
    entered=inentery.get()
    selected_rows = invenManager.loc[invenManager['Ingredient'] == entered]
    Resualtvarible=Label(root,text=selected_rows)
    Resualtvarible.grid(row=2,column=1)

quantitylbl=Label(root, text="Quantity(grms):")
quantitylbl.grid(row=1,column=1)
button=Button(root, text="submit",  command=submit)
button.grid(row=3,column=1)
cityselected_option=StringVar()
dropdownlbl=Label(root, text="Select Ingredient from dropdown")
dropdownlbl.grid(row=0,column=0)
city_dropdown=ttk.Combobox(root, values=options, textvariable=cityselected_option)
city_dropdown.bind("<<ComboboxSelected>>", City_select)
city_dropdown.grid(row=1,column=0)
orlbl=Label(root, text="Or")
orlbl.grid(row=2,column=0)
inentery=Entry(root, width=50)
inentery.grid(row=3,column=0)

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.rowconfigure(3,weight=1)
root.mainloop()