from array import *

arr = array('i',[])

n = int(input("Please the length of the array"))

for i in range(n):
    x=int(input("pleaes enter the next value\n"))
    arr.append(x)

print(arr)

val=int(input("Enter the number want to search"))

'''k=0
for e in arr:
    if e==val:
        print("the index number",k)
        break
    k+=1
else:
    print("not found")'''

print(arr.index(val))