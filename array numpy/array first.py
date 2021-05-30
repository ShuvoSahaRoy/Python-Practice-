from array import *

vals = array('i',[1,4,7,99])

vals.reverse()

print(vals)
print(vals.buffer_info())
print(vals.typecode)

for i in range(len(vals)):
    print(vals[i])

for i in vals:
    print(i)