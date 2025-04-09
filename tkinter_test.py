from tkinter import *
from tkinter import ttk
import sqlite3
global role
role=""
global nameentered
nameentered=""
global citylbl,city_dropdown,clublbl,club_dropdown,courtlbl,courtbookbtn,courtnobook,bookedlbl,btnyes,Btnno, Rebookedlbl, yearbook,yearenter,monthbook,monthenter,daybook,dayenter,whenbook,datesubmit
global playerid, instructorid,cityid, clubid,totalCourts,avaibleCourts
connection=sqlite3.connect('Squashspace.db')
cursor=connection.cursor()
root=Tk()


root.title("Squashspace: Court finding app")

root.geometry('1100x700')



rolelbl=Label(root,text="Welcome to squashspace, are you a player or an Instructor: ")

def Player():
    global role
    namelbl.grid(column=1,row=2)
    Namentery.grid(column=1,row=3)
    namesubmit.grid(column=1,row=4)
    rolelbl.grid_remove()
    btnpl.grid_remove()
    btnin.grid_remove()
    role="player"


btnpl = Button(root, text = "Player" ,fg = "Black", command=Player)
def Instructor():
    global role
    namelbl.grid(column=1,row=2)
    Namentery.grid(column=1,row=3)
    namesubmit.grid(column=1,row=4)
    rolelbl.grid_remove()
    btnpl.grid_remove()
    btnin.grid_remove()
    role="instructor"


btnin = Button(root, text = "Instructor" ,fg = "Black", command=Instructor)

namelbl=Label(root,text="please enter your credentials: ")

Namentery=Entry(root, width=50)


def name_submit():
    global nameentered, citylbl,city_dropdown, playerid,role,instructorid
    nameentered=Namentery.get()
    namenotfound=Label(root,text="Name not found")
    if role == "player":
        pnamefind=cursor.execute("SELECT * FROM Player WHERE Player_name= ?",(nameentered,))
        pnameSQL=cursor.fetchall()
        if pnameSQL[0][1]==nameentered:
            playerid=pnameSQL[0]
            citylbl=Label(root,text="Welcome back "+nameentered+" Please enter The city you want to select")
            citylbl.grid(column=1,row=5)
            cityselected_option=StringVar()
            cityFind=cursor.execute("SELECT * FROM Cities")
            city=cursor.fetchall()
            cityoptions=[]
            for i in range(len(city)):
                cityoptions+=[city[i]]
            city_dropdown=ttk.Combobox(root, values=cityoptions, textvariable=cityselected_option)
            city_dropdown.set("Select a city")
            city_dropdown.bind("<<ComboboxSelected>>", City_select)
            city_dropdown.grid(column=1,row=6)
            namelbl.grid_remove()
            Namentery.grid_remove()
            namesubmit.grid_remove()
        else:
            namenotfound.grid(column=1,row=5) 
    elif role == "instructor":
        inamefind=cursor.execute("SELECT * FROM Instructor WHERE Instuctor_name= ?",(nameentered,))
        inameSQL=cursor.fetchall()
        if inameSQL[0][1]==nameentered:
            instructorid=inameSQL[0]
            citylbl=Label(root,text="Welcome back "+nameentered+" Please enter The city you want to select")
            citylbl.grid(column=1,row=5)
            cityselected_option=StringVar()
            cityFind=cursor.execute("SELECT * FROM Cities")
            city=cursor.fetchall()
            cityoptions=[]
            for i in range(len(city)):
                cityoptions+=[city[i]]
            city_dropdown=ttk.Combobox(root, values=cityoptions, textvariable=cityselected_option)
            city_dropdown.set("Select a city")
            city_dropdown.bind("<<ComboboxSelected>>", City_select)
            city_dropdown.grid(column=1,row=6)
            namelbl.grid_remove()
            Namentery.grid_remove()
            namesubmit.grid_remove()
        
        else:
            namenotfound.grid(column=1,row=5)




namesubmit=Button(root,text="Submit",command=name_submit)



def City_select(event):
    global citylbl,city_dropdown, clublbl ,club_dropdown, clublbl, cityid
    selected_city=city_dropdown.get()
    city_arr = selected_city.split(' ')
    cityid=city_arr[0]
    clublbl=Label(root,text="Please enter The club you want to select")
    clublbl.grid(column=1,row=7)
    clubFind=cursor.execute("SELECT * FROM Clubs WHERE City_id=?",(cityid,))
    ClubsSQL=cursor.fetchall()
    cluboptions=[]
    for j in range (len(ClubsSQL)):
        cluboptions+=[ClubsSQL[j][:2]]
    clubselected_option=StringVar()
    club_dropdown=ttk.Combobox(root, values=cluboptions, textvariable=clubselected_option)
    club_dropdown.set("Select a club")
    club_dropdown.bind("<<ComboboxSelected>>", club_select)
    club_dropdown.grid(column=1,row=8)
    citylbl.grid_remove()
    city_dropdown.grid_remove()





def club_select(event):
    global courtlbl,courtbookbtn,courtnobook,clublbl, clubid,totalCourts,avaibleCourts
    selected_club=club_dropdown.get()
    club_arr = selected_club.split(' ')
    clubid=club_arr[0]
    courtfind=cursor.execute("SELECT * FROM Courts WHERE Club_id=?",(clubid,))
    courtSQL=cursor.fetchall()
    totalCourts=courtSQL[0][1]
    avaibleCourts=courtSQL[0][2]
    courtlbl=Label(root,text="There are "+str(totalCourts)+" courts in the club, out of which "+str(avaibleCourts)+" are avaible, yould you like to book a court")
    courtlbl.grid(column=1,row=9)
    courtbookbtn=Button(root, text = "Yes" , command=court_select)
    courtbookbtn.grid(column=0,row=10)
    courtnobook=Button(root, text = "No", command=Close_window)
    courtnobook.grid(column=2,row=10)
    clublbl.grid_remove()
    club_dropdown.grid_remove()





def court_select():
    global bookedlbl,role,btnyes,Btnno,Rebookedlbl,yearbook,yearenter,monthbook,monthenter,daybook,dayenter,whenbook, datesubmit
    if avaibleCourts != 0:
        courtlbl.grid_remove()
        courtbookbtn.grid_remove()
        courtnobook.grid_remove()
        whenbook=Label(root,text="When you want to book your court")
        whenbook.grid(column=1,row=11)
        yearbook=Label(root,text="Year")
        yearbook.grid(column=0,row=12)
        yearenter=Entry(root, width=50)
        yearenter.grid(column=0,row=13)
        monthbook=Label(root,text="Month:")
        monthbook.grid(column=1,row=12)
        monthenter=Entry(root, width=50)
        monthenter.grid(column=1,row=13)
        daybook=Label(root,text="Day:")
        daybook.grid(column=2,row=12)
        dayenter=Entry(root, width=50)
        dayenter.grid(column=2,row=13 )
        datesubmit=Button(root, text = "Book a court" , command=booking)
        datesubmit.grid(column=1,row=14)




def Close_window():
    root.destroy()

def  booking():
    global bookedlbl,btnyes,Btnno,Rebookedlbl
    if role== "player":
        whenbook.grid_remove()
        yearbook.grid_remove()
        yearenter.grid_remove()
        monthbook.grid_remove()
        monthenter.grid_remove()
        daybook.grid_remove()
        dayenter.grid_remove()
        datesubmit.grid_remove()
        bookedlbl=Label(root,text="your court has been booked")
        bookedlbl.grid(column=1,row=15)
    elif role=="instructor":
        whenbook.grid_remove()
        yearbook.grid_remove()
        yearenter.grid_remove()
        monthbook.grid_remove()
        monthenter.grid_remove()
        daybook.grid_remove()
        dayenter.grid_remove()
        datesubmit.grid_remove()
        Rebookedlbl=Label(root,text="your court has been booked, would you like to book another court:")
        Rebookedlbl.grid(column=1,row=15)
        btnyes = Button(root, text = "Yes" ,command=Re_book)
        Btnno=Button(root, text = "no", command=no_rebook)
        btnyes.grid(column=0,row=16)
        Btnno.grid(column=2,row=16)





def Re_book():
    Rebookedlbl.grid_remove()
    btnyes.grid_remove()
    Btnno.grid_remove()
    courtlbl.grid(column=1,row=9)
    courtbookbtn.grid(column=0,row=10)
    courtnobook.grid(column=2,row=10)


def no_rebook():
    global btnyes, Btnno,bookedlbl
    Rebookedlbl.grid_remove()
    btnyes.grid_remove()
    Btnno.grid_remove()
    root.destroy()



root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.rowconfigure(3,weight=1)
root.rowconfigure(4,weight=1)
root.rowconfigure(5,weight=1)
root.rowconfigure(6,weight=1)
root.rowconfigure(7,weight=1)
root.rowconfigure(8,weight=1)
root.rowconfigure(9,weight=1)
root.rowconfigure(10,weight=1)
root.rowconfigure(11,weight=1)
root.rowconfigure(12,weight=1)
root.rowconfigure(13,weight=1)
root.rowconfigure(14,weight=1)
root.rowconfigure(15,weight=1)
root.rowconfigure(16,weight=1)
root.rowconfigure(17,weight=1)



rolelbl.grid(column=1,row=0,sticky="n")
btnpl.grid(column=0, row=1)
btnin.grid(column=2, row=1)
root.mainloop()