# import numpy as np
from array import *
arr = array([1, 2, 3, 4, 5])

NewAr = arr + 5
print(NewAr)

newAr = arr + NewAr  # vectorize operation
print(newAr)

# triconmetig operation

print(sin(arr))
print(cos(arr))
print(log(newAr))

print(sum(arr))
print(min(arr))
print(max(arr))

print(concatenate([arr, NewAr]))
