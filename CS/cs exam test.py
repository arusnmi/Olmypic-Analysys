def SumOdd(N):
    number=1
    SumNumber=0
    if N>0 :
        for i in range(N):
            SumNumber=SumNumber+number
        number+=2
        return SumNumber
    else:
        return -1
N=4
print(SumOdd(N))  # Output: 25
