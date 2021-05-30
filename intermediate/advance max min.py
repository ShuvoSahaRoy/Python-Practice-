# def func(item):
#     return len(item)
#
# names = [ 'shuvo', 'joy', 'munna' ]
# print(max(names, key=func ))

# names = [ 'shuvo', 'joy', 'munna' ]
# print(max(names, key=lambda item: len(item)))

# student = {
#     'shuvo' : {'score':60, 'age':24 },
#     'joy' : {'score':85, 'age':20},
#     'munna' : {'score':65, 'age':27},
# }
# print(max(student, key=lambda item : student[item]['score']))

student2 = [
    {'name': 'shuvo', 'score': 60, 'age': 24},
    {'name': 'joy', 'score': 85, 'age': 21},
    {'name': 'munna', 'score': 65, 'age': 26},
]
print(type(student2[0]))
print(max(student2, key=lambda item: item.get('score'))['name'])
