from numpy import *
arr1=array([1,2,3,4,5])
'''
arr2=arr1

print(arr1)
print(arr2)
#address of both array will be same
print(id(arr1))
print(id(arr2))

#for different address

arr2=arr1.view()
print(id(arr1))
print(id(arr2))
'''
#arr2= arr1.view()  #shallow copy
arr2 = arr1.copy()
arr1[1] = 7

print(arr1)
print(arr2)

