def fun(*args):
    print(args)
    total = 0
    for i in args:
        total += i
    return total


print(fun(1, 2, 3, 4, 5, 6))  # in args it takes input as tuples
# we can pass list or tuples
# but we need to unpack it

l = (1, 2, 3, 4, 5, 6)
# print(fun(l))      #error
print(fun(*l))  # unpacking using *

print(fun(1, 2, 3, 4, 5, 6))


def mySum(*args):
    sum = 0
    for i in range(0, len(args)):
        sum = sum + args[i]
    return sum


# Driver code
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))
