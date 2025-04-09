import sqlite3


connection=sqlite3.connect('Squashspace.db')

cursor=connection.cursor()
role=input("Are you a Player or an Instructor: ")
def city():
    print("Welcome back, here is a list of cities that we have:")
    cityFind=cursor.execute("SELECT * FROM Cities")
    city=cursor.fetchall()
    for i in  city:
        print(i)
    citychose=input("Enter the name of the city you chose: ")
    cityfind=cursor.execute("SELECT * FROM Cities WHERE City_name =?",(citychose,))
    citySQL=cursor.fetchall()
    return citySQL, citychose




def club(citySQL):
    print("Here are the clubs that are in "+citySQL[0][1])
    cityid=citySQL[0][0]

    clubFind=cursor.execute("SELECT * FROM Clubs WHERE City_id=?",(cityid,))
    ClubsSQL=cursor.fetchall()

    for j in ClubsSQL:
        print(j)
    clubchose=input("Which club do you chose: ")
    clubfind=cursor.execute("SELECT * FROM CLubs WHERE Club_name =?",(clubchose,))
    clubSQL=cursor.fetchall()
    return cityid,clubSQL,clubchose

def court(clubSQL):
    clubid=clubSQL[0][0]
    courtfind=cursor.execute("SELECT * FROM Courts WHERE Club_id=?",(clubid,))
    courtSQL=cursor.fetchall()
    totalCourts=courtSQL[0][1]
    avaibleCourts=courtSQL[0][2]
    print("There are "+str(totalCourts)+" courts in the club, out of which "+str(avaibleCourts)+" are avaible")
    return courtSQL,totalCourts,avaibleCourts,clubid

def pcourtbook(clubid, avaibleCourts,cityid,courtid,playerid):
    cursor.execute("UPDATE Courts SET Courts_avaible = ? WHERE Club_id = ?", (avaibleCourts-1, clubid))
    connection.commit()
    date=input("When do you wnat to book the court:")
    cursor.execute("INSERT INTO Bookings VALUES(NULL,?,?,?,?,?,?)", (date,cityid,clubid,courtid,playerid,0))
    connection.commit()
    print("your court has been booked")


def icourtbook(clubid, avaibleCourts,cityid,courtid,Instructorid):
    cursor.execute("UPDATE Courts SET Courts_avaible = ? WHERE Club_id = ?", (avaibleCourts-1, clubid))
    connection.commit()
    date=input("When do you wnat to book the court:")
    cursor.execute("INSERT INTO Bookings VALUES(NULL,?,?,?,?,?,?)", (date,cityid,clubid,courtid,0,Instructorid))
    connection.commit()
    print("your court has been booked")
    rerebook=input("would you like to book another court (Y/N): ")
    return rerebook





if role=="Player":
    pName=input("Welcome to the daily court booking app, please enter a name: ")



    pnamefind=cursor.execute("SELECT * FROM Player WHERE Player_name= ?",(pName,))



    pnameSQL=cursor.fetchall()
    playerid=pnameSQL[0][0]

    if pnameSQL[0][1]==pName:
        citySQL,citychose=city()
    else:
        print("Opps, your name is not there in the database.")


    if citySQL[0][1]==citychose:
        cityid,clubSQL,clubchose=club(citySQL)
        
    else:
        print("this city is not in our database.")
        
        

    
    if clubSQL[0][1]==clubchose:
        
        courtSQL,totalCourts,avaibleCourts,clubid=court(clubSQL)
        
    else:
        print("this secion of code doe not work because iam dumb")
    courtbook=input("would you like to book a court(Y/N): ")
    courtid=courtSQL[0][0]
    if courtbook=="Y" and avaibleCourts > 0:
        pcourtbook(clubid, avaibleCourts,cityid,courtid,playerid)
    elif avaibleCourts == 0:
        print("there are no courts available")

if role=="Instructor":
    IName=input("Welcome to the daily court booking app, please enter a name: ")



    Inamefind=cursor.execute("SELECT * FROM Instructor WHERE Instructor_name= ?",(IName,))



    InameSQL=cursor.fetchall()
    Instructorid=InameSQL[0][0]

    if InameSQL[0][1]==IName:
        citySQL,citychose=city()
    else:
        print("Opps, your name is not there in the database.")



    if citySQL[0][1]==citychose:
        cityid,clubSQL,clubchose=club(citySQL)
        
    else:
        print("this city is not in our database.")
        
        



    if clubSQL[0][1]==clubchose:
        
        courtSQL,totalCourts,avaibleCourts,clubid=court(clubSQL)
    else:
        print("this secion of code doe not work because iam dumb")
    courtbook=input("would you like to book a court(Y/N): ")
    courtid=courtSQL[0][0]

    rebook="No"
    if courtbook=="Y" and avaibleCourts > 0:
        rebook="Yes"
    elif avaibleCourts == 0:
        print("there are no courts available")
    
    while rebook=="Yes":
        rerebook=icourtbook(clubid, avaibleCourts,cityid,courtid,Instructorid)
        if rerebook=="N":
            rebook="No"
            print("thank you for booking the courts")





