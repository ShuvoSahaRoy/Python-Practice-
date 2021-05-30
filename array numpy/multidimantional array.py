from numpy import *

arr1 = array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(arr1)
print(arr1.dtype)
print(arr1.size)
print(arr1.shape)
print(arr1.ndim)

print(arr1.max())
print(arr1.min())

#convert 2d array into 1d array
arr2 = arr1.flatten()
print(arr2)

arr3 = arr2.reshape(3,3)
print(arr3)

#convert into matrix

m = matrix(arr1)
print(m)

m1 = matrix('1 2 3;4 5 6;7 8 9')
print(m1)
print(diagonal(m))

m2 = m * m1

print(m2)