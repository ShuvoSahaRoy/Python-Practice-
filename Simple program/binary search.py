from array import *

def search(arr,x):
    l = 0
    u = len(arr)-1

    while l<=u:
        mid = (l + u) // 2
        if x==arr[mid]:
            print("Element found in ",mid+1,"th position")
            return True
        else:
            if arr[mid]<x:
                l=mid+1
            else:
                u=mid-1
    print("Not Found")
    return False

arr= array('i',[1,2,3,4,5,6,7,8,9])
x=int(input("Which element you want to search"))

search(arr,x)