from array import *

vals = array('i',[3,5,2,5,6,57,7,3])

#copy array

narr= array(vals.typecode,(a for a in vals))
print(narr)
print("new array")
for i in narr:
    print(i)

#we can change (square or add anything to all index number)

#copy array

narr= array(vals.typecode,(a*a for a in vals))
print(narr)
print("new array")
for i in narr:
    print(i)

