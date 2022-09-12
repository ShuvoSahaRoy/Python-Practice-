# print(22/7)
# x , y = 5 , 6
# print(x+y)
# #a,b = input("enter value ").split()
# #print(int(a)+int(b))
#
# st ,num = "shuvo", 5
# #print(st+ num)   error
# name = 'shuvo'
# age = 25
# print(f"Hello {name} ur age is {age}")
# print(type(age))
# f = 5/6
# print("%0.2f"%f)
#
# number =[11,111,1111]
# print(min(number))
# print(max(number))


# largest = None
# smallest = None
# while True:
#     try:
#         num = input("Enter a number: ")
#         if num == "done":
#             break
#         num = int(num)
#         if largest is None or largest < num:
#             largest = num
#         elif smallest is None or smallest > num:
#             smallest = num
#     except ValueError:
#         print("Invalid input")
#
# print("Maximum is", largest)
# print("Minimum is", smallest)

# import numpy as np
# old = np.array([[1, 1, 1],
#                 [1, 1, 1]])
#
# new = old
# new[0, :2] = 0
#
# print(old)

# l='/home/student-bal'
# print(l[6:])
#
# print(f"hello {'shuvo'.upper()}")

# a, b, c = 3, 4, 5
# print((a + b + c) / 3)

# lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
# map_testing = map(lambda str: "Fruit: " + str, lst_check)
# print(next(map_testing))
# print(next(map_testing))
# print(next(map_testing))
# print(next(map_testing))

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
lst2 = [i+i for i in lst]