creditcardn=input("ENter the 12 digits of your credit card: ")

credit=list(creditcardn)




hid=input("would you like to hide this number (Y/N): ")


if hid=="Y":

    for e in range(8):
        credit[e]="*"

print()