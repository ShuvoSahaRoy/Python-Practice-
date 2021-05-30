# user = {'name':'shvuo','age': 24}
# print(user)
#
# user1 = dict(name = 'Shuvo', age = 24)
# #user1 = dict(name = input(), age = input())
# print(user1)
#
# print(user1['name'])
#
#
user2 ={
    'name' : 'Shuvo',
    'Age' : 24,
    'fav_movie' : ['Marvel Series','Harry Potter']
}
#
# print(user2)
#
# #we can store dictionary into dictionary
# #
# users ={
#     'u1' : {'name' : 'Rony', 'age' : '25'},
#     'u2' : {'name' : 'Munna', 'age' : '26'},
#     'u3' : {'name' : 'Joy', 'age' : '23'}
# }

#
# #how to add data in dictionary
# user_info = {}
# user_info['name'] = 'Shuvo'
# print(user_info)
#
# #existence of key
# if 'name' in user_info:
#     print("yes")
# else:
#     print("No")
#
# #existence of values
# if 'Shuvo' in user_info.values():
#     print("yes")
#
# print(user1.keys())
#
# for i in user2:
#     print(i)
#
# for i in user2.values():
#     print(i)
#
# print(user2.items())
#
# #add data
# user1['fav_movies'] = ['dr strange','x-man','harry poter']
# print(user1)
#
# #pop method
# #user2.pop('key')
#
# #uapdate method
#
# more_user2 = {'name' : 'shuvo saha roy','address' : 'kalmakanda','university' : 'nstu'}
#
# user2.update(more_user2)
# print(user2)
# print(user2.items())

#fromkeys_get_copy_clear

#d = {'name' : 'unknown' , 'age' : 'unknown' }
#if all keys have same value then we can write this in this way

#d= dict.fromkeys(['name','age','height'] , 'unknown')    #ok
#d = dict.fromkeys(('name','age','height') , 'unknown')

#d = dict.fromkeys(range(1,11), 'unknown')

#print(d)

#get method
# d = {'name' : 'unknown' , 'age' : 'unknown' }

#print(d.get('names'))  #there is no key like name so it will return none

#change non to any string
# print(d.get('names' , 'not found!'))
# print(d.get('name' , 'not found!'))

# if d.get('name'):
#     print("yes")

#clear method
#print(d.clear())

#copy dictionary

# d1 = d.copy()     #copy create another dictionary but = sign means same dictionary
# print(d1)
#
# example = [('a',1), ('b',2)]  # we can change such type of list in dictionaries
# print(dict(example))
