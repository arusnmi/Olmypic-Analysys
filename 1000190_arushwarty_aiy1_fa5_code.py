courts={'Mumbai':["bombay gymkahan", "CCI"], 'Dehli':["JP morgan", "Grand hyatt"], 'Chennai':["JW marriot","chennai gymakhana"]}


count=0
entry=courts.keys()


for e in entry:
    countstring=str(count)
    print(countstring+" "+list(courts.keys())[count])
    count=count+1

book=input("Using the numbers on the side of the cities which city do you live in: ")
bookint=int(book)
city=list(courts.keys())[bookint]
print("the courts in "+city+" are "+str(courts[city]))

stopbool=False

stop=input("Would you like to add a court to this database (Y/N): ")

if stop=="Y":
    stopbool=True

if stop=="N":
    stopbool=False

while stopbool==True:

    newcourt=input("What is the name of the court you want to add: ")

    courts[city].append(newcourt)

    print("Now the courts in "+city+" are "+str(courts[city]))

    stopwhile=input("would you like to add another court (Y/N):")

    if stopwhile=="Y":
        stopbool=True
    if stopwhile=="N":
        stopbool=False 