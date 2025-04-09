import time
import random
def bublesort(arr):

    

    for n in range(len(arr)-1,0,-1):

        swapped=False

        for i in range (n) :
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1]=arr[i+1],arr[i] 
                swapped=True
        if not swapped:
            break 


stat_time=time.time()
arr=[random.randrange(500) for i in range(5000)]
print("before")
print(arr)
bublesort(arr)
print("after")
print(arr)
end_time=time.time()
print("time taken: ",end_time-stat_time)