def add(x,y):
    z= x+y
    zsub = x-y
    return z,zsub

a = int(input("Please Enter a Value"))
b= int(input("Plz enter 2nd value"))
c,d = add(a,b)

print(c,d)
print(c)
print(d)

#swap number

'''def swap(x,y):
    temp = y
    y=x
    x= temp
    print("1st value", x , "\n2nd value",y)

a = int(input("Please Enter a Value"))
b= int(input("Plz enter 2nd value"))

swap(a,b)'''
