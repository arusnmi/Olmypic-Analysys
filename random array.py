import random


RandomM=[6,2,1,3,5,6,4,8,7,9,0]


for n in RandomM:
    RandomM[n]=random.randrange(10)
    print(RandomM[n])
    print(RandomM)