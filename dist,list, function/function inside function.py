def greater(a,b):
    if a>b:
        return a
    return b
# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c

def greatest(a,b,c):
    # bigger = greater(5,66)
    # return greater(bigger,c)
    return greater(greater(5,66), c)

print(greatest(10,20,200))