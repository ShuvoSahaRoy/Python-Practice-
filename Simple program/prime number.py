import math
for i in range(1,10):
    x= int(input("Enter a number\n"))
    y = math.floor(math.sqrt(x))
    print(y)
    for i in range(2,y+1):
        if x%i==0:
            print("Not Prime")
            break
    else:
        print("prime")