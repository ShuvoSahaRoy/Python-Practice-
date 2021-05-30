x=5

def fun():
    global x
    x=7
    return x

print(x)
print(fun())
print(x)