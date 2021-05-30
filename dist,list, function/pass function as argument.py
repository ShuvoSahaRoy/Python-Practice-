def square(a):
    return a ** 2


def myfun(func, l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list


# def myfun(func,l):
#     return [func(item) for item in l]

print(myfun(square, [1, 2, 3, 4, 5]))
