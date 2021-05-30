#
# s= {1,2,3,4,1,2,3}
# print(s)
# # l = [1,2,3,4,5,6,7,8,9,1,5,5,5,5,2,3,4,5,6,7,8,9]
# #
# # #s2 = set(l)
# # s2 = list(set(l))
# # print(s2)
#
# s.add(7)
# s.remove(2) #if value is not present in set we can't use that value for removing
# print(s)
# #s.clear()
# #s1 = s.copy()
#
# #we can't store tuples, list or dictionaries
#
# s3 = {1,2.2,'string',1.0} # here 1 and 1.0 is same for set
# print(s3)

# s= {'a','b','c'}
# if 'a' in s:
#     print("yes")
#
# for i in s:
#     print(i)

#union set and intersection

s1 = {1,2,4,5}
s2 = {1,2,3,5,7,8,9}

union = s1 | s2
print(union)

print(s1&s2)


