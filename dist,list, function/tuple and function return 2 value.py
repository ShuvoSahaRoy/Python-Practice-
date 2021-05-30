def fun(a,b):
    add = a+b
    multiply = a*b
    return add, multiply
#print(fun(4,6))      it will return a tuple
add , multiply = fun(4,6)
print("{}\n{}".format(add,multiply))

t = (1,2,3,4)
for i in t:
    print(i)