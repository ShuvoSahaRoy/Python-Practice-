# user_id = ['user1','user2','user3']
# names = [ 'shuvo', 'joy', 'munna' ]
#
# print(list(zip(user_id,names)))

l = [(1,2),(3,4),(5,6)]
l1,l2 = list(zip(*l))
print(l1,l2)

# new_list = []
# for i in zip(l1,l2):
#     new_list.append(max(i))
#
# print(new_list)

# def average_finder(*args):
#     #print(args)
#     average = []
#     for pair in zip(*args):
#         print(pair)
#         average.append(sum(pair)/len(pair))
#     return average
# print(average_finder([1,2,3],[4,5,6],[7,8,9]))

# average = lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
# print(average([1,2,3],[4,5,6],[7,8,9]))

#unpaking

list1 = [1,2,3,4,5]
print(*list1)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = list(filter(lambda n: n%2 == 0, nums))
print(evens)