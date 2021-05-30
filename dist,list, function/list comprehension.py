# squares = []
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)
#
# squares2 = [i**2 for i in range(1,11)]
# print(squares2)
#
# negative =[-i for i in range(1,11)]
# print(negative)

# names = ['shuvo','munna','joy']
# #new_list=['s','m','j']
# # new_list = []
# # for name in names:
# #     new_list.append(name[0])
# # print(new_list)
# new_list = [name[0] for name in names]
# print(new_list)

#exercise
# def reverse(list):
#     reverse_word = [word[::-1] for word in list]
#     return reverse_word
# l = ['abc','tuv','xyz']
# print(reverse(l))
#
# #exercise
# numbers = list(range(1,11))
# print([i for i in numbers if i%2==0])
#
# print([i for i in range(1,11) if i%2==0])

#exercise

# def num_to_string(l):
#     return [str(i) for i in l if (type(i)== int or type(i)== float)]
#
# print(num_to_string([True,[1,2,30], 1,1.5]))

#exercise

# new_list = [i*2 if (i%2==0) else -i for i in range(1,11)]
# print(new_list)

#exercise

nested_list = [[i for i in range(3)] for i in range(3)]
print(nested_list)