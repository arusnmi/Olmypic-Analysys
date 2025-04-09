import time
import random
def mergesort(arr):
    if len(arr)>1:
        middle=len(arr)//2

        subarr=arr[:middle]

        subarr1=arr[middle:]

        mergesort(subarr)

        mergesort(subarr1)

        i=j=k=0


        while i < len(subarr) and j<len(subarr1):
            if subarr[i]<subarr1[j] :
                arr[k]=subarr[i] 
                i+=1
            else:
                arr[k]=subarr1[j]
                j+=1
            k+=1

        while i< len(subarr):
            arr[k]=subarr[i]
            i+=1
            k+=1
        while j<len(subarr1):
            arr[k]=subarr1[j]
            j+=1
            k+=1
start_mtime=time.time()
arr=[random.randrange(500) for i in range(5000)]
mergesort(arr)

print(arr)
end_mtime=time.time()
print("execution time: ", end_mtime-start_mtime, " seconds")
start_btime=time.time()
x=59

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

low=0

high=len(arr)

yes= binary_search(arr,low,high,x)
print(yes)
if yes!=-1:
    print("the value " +str(x)+" is in index "+ str(yes))
else:
    print("this value is not thwere in this array")
end_btime=time.time()
print("execution time: ", end_btime-start_btime, " seconds")