from array import *

def search(arr,e):
    for i in range(len(arr)):
        if arr[i] == e :
            print("The position of the element ", i+1)
            break
    else:
        print("Not Found")

arr = array('i',[])

x = int(input("How many element want to keep?"))

for i in range (x):
    y = int(input())
    arr.append(y)

print(arr)

e = int(input("Which element you want to search?"))

search(arr,e)